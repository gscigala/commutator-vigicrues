import logging
import math

import pyvigicrues

SAMPLES_PER_HOUR=6
EPSILON=0.10

logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger(__name__)

class VigicruesData:
    """The class for handling the data retrieval."""

    def __init__(self, stationid):
        """Initialize the data object."""
        self.stationid = stationid
        self.water_level_value = ''
        self.water_level_tendency = ''
        self.flow_value = ''
        self.flow_tendency = ''

    def computeMean(self, data, firstSampleIndex, lastSampleIndex):
        cnt = 0
        mean = 0
    
        for i in range(firstSampleIndex, lastSampleIndex):
            cnt += 1
            mean += float(data['Serie']['ObssHydro'][i]['ResObsHydro'])
        mean = mean / cnt

        return mean

    def computeStandardDeviation(self, data, firstSampleIndex, lastSampleIndex, mean):
        cnt = 0
        variance = 0

        for i in range(firstSampleIndex, lastSampleIndex):
            cnt += 1
            value = float(data['Serie']['ObssHydro'][i]['ResObsHydro'])
            variance += (value - mean) ** 2
        variance = variance / cnt
        standard_deviation = math.sqrt(variance)

        return standard_deviation

    def getTendency(self, data):
        totalPtsNb = len(data['Serie']['ObssHydro'])
        _LOGGER.debug("totalPtsNb = {}".format(totalPtsNb))

        meanH6H5 = self.computeMean(data,
                               totalPtsNb - 6 * SAMPLES_PER_HOUR,
                               totalPtsNb - 5 * SAMPLES_PER_HOUR)
        _LOGGER.debug("meanH6H5 = {}".format(meanH6H5))

        sdH6H5 = self.computeStandardDeviation(data,
                                          totalPtsNb - 6 * SAMPLES_PER_HOUR,
                                          totalPtsNb - 5 * SAMPLES_PER_HOUR,
                                          meanH6H5)
        _LOGGER.debug("sdH6H5 = {}".format(sdH6H5))

        meanH1H0 = self.computeMean(data,
                               totalPtsNb - 1 * SAMPLES_PER_HOUR,
                               totalPtsNb)
        _LOGGER.debug("meanH1H0 = {}".format(meanH1H0))

        sdH1H0 = self.computeStandardDeviation(data,
                                totalPtsNb - 1 * SAMPLES_PER_HOUR,
                                totalPtsNb,
                                meanH1H0)
        _LOGGER.debug("sdH1H0 = {}".format(sdH1H0))

        limitMax = meanH6H5 + 2 * sdH6H5
        limitMin = meanH6H5 - 2 * sdH6H5

        if (meanH1H0 > (limitMax + EPSILON)):
            _LOGGER.debug("Increasing")
            tendency = "Increasing"
        elif(meanH1H0 < (limitMin - EPSILON)):
            _LOGGER.debug("Decreasing")
            tendency = "Decreasing"
        else:
            _LOGGER.debug("Stable")
            tendency = "Stable"

        return tendency

    def update(self):
        """Get the latest data from Vigicrues."""

        try:
            client = pyvigicrues.VigicruesClient(self.stationid, 'H')
            data_water_level = client.get_data()

            client = pyvigicrues.VigicruesClient(self.stationid, 'Q')
            data_flow = client.get_data()

        except Exception as e:
            _LOGGER.error("Connection error: {}".format(e))
            self.data = None
            return

        totalPtsNb = len(data_water_level['Serie']['ObssHydro'])
        self.water_level_value = str(data_water_level['Serie']['ObssHydro'][totalPtsNb-1]['ResObsHydro'])
        _LOGGER.info("water_level_value = {}".format(self.water_level_value))
        self.water_level_tendency = self.getTendency(data_water_level)
        _LOGGER.info("water_level_tendency = {}".format(self.water_level_tendency))

        totalPtsNb = len(data_flow['Serie']['ObssHydro'])
        self.flow_value = str(data_flow['Serie']['ObssHydro'][totalPtsNb-1]['ResObsHydro'])
        _LOGGER.info("flow_value = {}".format(self.flow_value))
        self.flow_tendency = self.getTendency(data_flow)
        _LOGGER.info("flow_tendency = {}".format(self.flow_tendency))

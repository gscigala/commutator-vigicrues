import unittest
from unittest.mock import patch, MagicMock
from commutator_vigicrues.vigicrues_dbus_service import VigicruesDBusService

class TestVigicruesDBusService(unittest.TestCase):

    @patch('commutator_vigicrues.vigicrues_dbus_service.VigicruesData')
    def test_update(self, mock_vigicrues_data):
        # Mock the SytadinData instance
        mock_instance = MagicMock()
        mock_instance.water_level_value = 'Level 1'
        mock_instance.water_level_tendency = 'Tendency 1'
        mock_instance.flow_value = '1.23'
        mock_instance.flow_tendency = 'Tendency 2'
        mock_vigicrues_data.return_value = mock_instance

        # Create an instance of SytadinDBusService
        bus_name = MagicMock()
        vigicrues_service = VigicruesDBusService(bus_name, 'F664000104')

        # Call the update method
        vigicrues_service.update()

        # Check if the update method of VigicruesData was called
        mock_instance.update.assert_called_once()

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
from commutator_vigicrues.vigicrues_data import VigicruesData

class TestVigicruesData(unittest.TestCase):

    @patch('commutator_vigicrues.vigicrues_data.pyvigicrues.VigicruesClient')
    def test_update(self, mock_vigicrues_client):
        # Mock the response from pyvigicrues.VigicruesClient
        mock_client_instance = MagicMock()
        mock_vigicrues_client.return_value = mock_client_instance

        # Mock the data returned by get_data
        mock_data = {
            'Serie': {
                'ObssHydro': [
                    {'ResObsHydro': '1.0'},
                    {'ResObsHydro': '1.1'},
                    {'ResObsHydro': '1.2'},
                    {'ResObsHydro': '1.3'},
                    {'ResObsHydro': '1.4'},
                    {'ResObsHydro': '1.5'},
                    {'ResObsHydro': '2.0'},
                    {'ResObsHydro': '2.1'},
                    {'ResObsHydro': '2.2'},
                    {'ResObsHydro': '2.3'},
                    {'ResObsHydro': '2.4'},
                    {'ResObsHydro': '2.5'},
                    {'ResObsHydro': '3.0'},
                    {'ResObsHydro': '3.1'},
                    {'ResObsHydro': '3.2'},
                    {'ResObsHydro': '3.3'},
                    {'ResObsHydro': '3.4'},
                    {'ResObsHydro': '3.5'},
                    {'ResObsHydro': '4.0'},
                    {'ResObsHydro': '4.1'},
                    {'ResObsHydro': '4.2'},
                    {'ResObsHydro': '4.3'},
                    {'ResObsHydro': '4.4'},
                    {'ResObsHydro': '4.5'},
                    {'ResObsHydro': '5.0'},
                    {'ResObsHydro': '5.1'},
                    {'ResObsHydro': '5.2'},
                    {'ResObsHydro': '5.3'},
                    {'ResObsHydro': '5.4'},
                    {'ResObsHydro': '5.5'},
                ]
            }
        }
        mock_client_instance.get_data.return_value = mock_data

        # Create an instance of VigicruesData
        vigicrues_data = VigicruesData('F664000104')
        vigicrues_data.update()

        # Check the updated values
        self.assertEqual(vigicrues_data.water_level_value, '5.5')
        self.assertEqual(vigicrues_data.water_level_tendency, 'Stable')
        self.assertEqual(vigicrues_data.flow_value, '5.5')
        self.assertEqual(vigicrues_data.flow_tendency, 'Stable')

if __name__ == '__main__':
    unittest.main()

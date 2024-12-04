import unittest
from unittest.mock import patch, MagicMock
from commutator_vigicrues.vigicrues_dbus_service import VigicruesDBusService

class TestVigicruesDBusService(unittest.TestCase):

    @patch('commutator_vigicrues.vigicrues_dbus_service.VigicruesData')
    def test_properties_changed(self, mock_vigicrues_data):
        # Mock the VigicruesData instance
        mock_instance = MagicMock()
        mock_instance.water_level_value = 'Level 1'
        mock_instance.water_level_tendency = 'Tendency 1'
        mock_instance.flow_value = '1.23'
        mock_instance.flow_tendency = 'Tendency 2'
        mock_vigicrues_data.return_value = mock_instance

        # Create an instance of VigicruesDBusService
        bus_name = MagicMock()
        vigicrues_service = VigicruesDBusService(bus_name, 'F664000104', 300)

        # Mock the PropertiesChanged signal
        properties_changed_signal = MagicMock()
        vigicrues_service.PropertiesChanged = properties_changed_signal

        # Simulate the properties_changed method being called
        vigicrues_service.properties_changed({
            'water_level_value': 'Level 1',
            'water_level_tendency': 'Tendency 1',
            'flow_value': '1.23',
            'flow_tendency': 'Tendency 2'
        })

        # Check if the PropertiesChanged signal was emitted
        properties_changed_signal.assert_called_once_with(
            'com.commutator.Vigicrues',
            {
                'water_level_value': 'Level 1',
                'water_level_tendency': 'Tendency 1',
                'flow_value': '1.23',
                'flow_tendency': 'Tendency 2'
            },
            []
        )

    @patch('commutator_vigicrues.vigicrues_dbus_service.VigicruesData')
    def test_get_method(self, mock_vigicrues_data):
        # Mock the VigicruesData instance
        mock_instance = MagicMock()
        mock_instance.water_level_value = 'Level 1'
        mock_instance.water_level_tendency = 'Tendency 1'
        mock_instance.flow_value = '1.23'
        mock_instance.flow_tendency = 'Tendency 2'
        mock_vigicrues_data.return_value = mock_instance

        # Create an instance of VigicruesDBusService
        bus_name = MagicMock()
        vigicrues_service = VigicruesDBusService(bus_name, 'F664000104', 300)

        # Test the Get method
        self.assertEqual(vigicrues_service.Get('com.commutator.Vigicrues', 'water_level_value'), 'Level 1')
        self.assertEqual(vigicrues_service.Get('com.commutator.Vigicrues', 'water_level_tendency'), 'Tendency 1')
        self.assertEqual(vigicrues_service.Get('com.commutator.Vigicrues', 'flow_value'), '1.23')
        self.assertEqual(vigicrues_service.Get('com.commutator.Vigicrues', 'flow_tendency'), 'Tendency 2')

    @patch('commutator_vigicrues.vigicrues_dbus_service.VigicruesData')
    def test_get_all_method(self, mock_vigicrues_data):
        # Mock the VigicruesData instance
        mock_instance = MagicMock()
        mock_instance.water_level_value = 'Level 1'
        mock_instance.water_level_tendency = 'Tendency 1'
        mock_instance.flow_value = '1.23'
        mock_instance.flow_tendency = 'Tendency 2'
        mock_vigicrues_data.return_value = mock_instance

        # Create an instance of VigicruesDBusService
        bus_name = MagicMock()
        vigicrues_service = VigicruesDBusService(bus_name, 'F664000104', 300)

        # Test the GetAll method
        properties = vigicrues_service.GetAll('com.commutator.Vigicrues')
        self.assertEqual(properties, {
            'water_level_value': 'Level 1',
            'water_level_tendency': 'Tendency 1',
            'flow_value': '1.23',
            'flow_tendency': 'Tendency 2'
        })

if __name__ == '__main__':
    unittest.main()

import dbus
import dbus.service
from .vigicrues_data import VigicruesData

class VigicruesDBusService(dbus.service.Object):
    def __init__(self, bus_name, stationid, object_path='/com/commutator/Vigicrues'):
        dbus.service.Object.__init__(self, bus_name, object_path)
        self.data = VigicruesData(stationid)

    @dbus.service.method('com.commutator.Vigicrues', in_signature='', out_signature='')
    def update(self):
        self.data.update()
        self.PropertiesChanged(
            'com.commutator.Vigicrues',
            {
                'water_level_value': self.data.water_level_value,
                'water_level_tendency': self.data.water_level_tendency,
                'flow_value': self.data.flow_value,
                'flow_tendency': self.data.flow_tendency
            },
            []
        )

    @dbus.service.signal('org.freedesktop.DBus.Properties', signature='sa{sv}as')
    def PropertiesChanged(self, interface_name, changed_properties, invalidated_properties):
        pass

    @dbus.service.method('org.freedesktop.DBus.Properties', in_signature='ss', out_signature='v')
    def Get(self, interface_name, property_name):
        try:
            return getattr(self.data, property_name)
        except AttributeError:
            raise dbus.exceptions.DBusException(
                f"Property '{property_name}' does not exist on interface '{interface_name}'",
                name='org.freedesktop.DBus.Error.UnknownProperty'
            )

    @dbus.service.method('org.freedesktop.DBus.Properties', in_signature='s', out_signature='a{sv}')
    def GetAll(self, interface_name):
        return {
            'water_level_value': self.data.water_level_value,
            'water_level_tendency': self.data.water_level_tendency,
            'flow_value': self.data.flow_value,
            'flow_tendency': self.data.flow_tendency
        }

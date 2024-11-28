import sys
import argparse
import signal
import dbus
import dbus.mainloop.glib
from gi.repository import GLib
from commutator_vigicrues.vigicrues_dbus_service import VigicruesDBusService

def signal_handler(signum, frame):
    print("SIGINT received, stopping the service...")
    loop.quit()

def main():
    parser = argparse.ArgumentParser(description='Vigicrues Data Service')
    parser.add_argument('--session', action='store_true', help='Use DBus session bus instead of system bus')
    parser.add_argument('--stationid', type=str, required=True, help='Station ID (Ex: F664000104)')
    args = parser.parse_args()

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus_name = dbus.service.BusName('com.commutator.Vigicrues', dbus.SystemBus() if not args.session else dbus.SessionBus())
    vigicrues_service = VigicruesDBusService(bus_name, stationid=args.stationid)

    global loop
    loop = GLib.MainLoop()

    signal.signal(signal.SIGINT, signal_handler)

    loop.run()

if __name__ == "__main__":
    sys.exit(main())

# Communator-Vigicrues

Commutator-Vigicrues is an application that provides a DBus interface for accessing real-time water level and flow information from Vigicrues. It allows you to fetch and monitor water levels, trends, and values, making it easy to integrate hydrological data into other applications or services.

## Dependencies

This application uses [pyvigicrues](https://github.com/Mickaelh51/pyVigicrues), a Python module to get level and flow data from many French rivers. For more information, visit the pyVigicrues GitHub repository or the [Vigicrues website](https://www.vigicrues.gouv.fr/).

## Installation

	pip install .

## Usage

To start the program, run:

	commutator-vigicrues --stationid F664000104

You can also use the --session flag to use the DBus session bus instead of the system bus:

	commutator-sytadin --session --stationid F664000104
	
## DBus Interface

### Methods

    update(): Fetches the latest water level and flow information from Vigicrues.

### Properties

    water_level_value: The current water level value.
    water_level_tendency: The current trend of the water level.
    flow_value: The current flow value.
    flow_tendency: The current trend of the flow.

### Possible Values

#### **Water level tendency**

- **Increasing**
- **Decreasing**
- **Stable**

#### **Flow tendency**

- **Increasing**
- **Decreasing**
- **Stable**

## Systemd Service

The project includes a systemd service file to manage the service using systemd. The service file is located at systemd/commutator-vigicrues.service. You need to replace %%STATIONID%% with your stationid.

## DBus Configuration

The project includes a DBus configuration file to set the necessary permissions for the DBus service. The configuration file is located at dbus/com.commutator.Vigicrues.conf.

## Testing

To run the tests, use the following command:

```sh
python -m unittest discover -s tests

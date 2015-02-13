#!/usr/bin/python
# -- Content-Encoding: UTF-8 --


import subprocess
from time import sleep

import pelix.framework
from pelix.ipopo.constants import use_ipopo
import pelix.shell
import pifacecad
import modbus.minimalmodbus as modbus




# Standard library
import logging

GET_IP_CMD = "hostname --all-ip-addresses"
SENSOR = modbus.Instrument('/dev/ttyUSB0', 104)


def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')


def get_my_ip():
    return run_cmd(GET_IP_CMD)[:-1]


def get_co2_value():
    try:
        value = SENSOR.read_register(3, 1, 4)
        return str(value * 10)
    except IOError:
        return 'Capteur indisponible'


class StopListener(object):
    """
    Framework stop listener
    """

    def framework_stopping(self):
        # Log the fact that the framework is stopping.
        # If an exception caused the stop, it is logged here
        logging.exception("Framework stopping !")


def main():
    """
    Starts a Pelix framework and waits for it to stop
    """
    # Prepare the framework, with iPOPO and the shell console
    # Warning: we only use the first argument of this method, a list of bundles
    logging.info("Preparing framework")
    print("Preparing framework")
    framework = pelix.framework.create_framework((
        "pelix.ipopo.core",  # iPOPO
        "pelix.shell.core",  # Shell core (engine)  # "pelix.shell.console",# Text console
        "pelix.shell.remote",
        "pelix.http.basic",
    ))

    # Start the framework, and the pre-installed bundles
    logging.info("Starting framework")
    print("Starting framework")
    framework.start()

    # Get the bundle context of the framework, i.e. the link between the
    # framework starter and its content.
    context = framework.get_bundle_context()
    context.add_framework_stop_listener(StopListener())

    with use_ipopo(context) as ipopo:
        ipopo.instantiate(pelix.shell.FACTORY_REMOTE_SHELL,
                          'remote-shell',
            {})
        ipopo.instantiate('pelix.http.service.basic.factory',
                          'http-server',
                          {
                              'pelix.http.address': '192.168.1.101',  # TODO Utiliser un fichier de conf
                              'pelix.http.port': 3737  # TODO Utiliser un fichier de conf
                          })

    logging.info("Installing PV bundle")
    print("Installing PV bundle")
    context.install_bundle("pvPanelsServlet").start()
    logging.info("PV bundle installed")
    print("PV bundle installed")

    cad = pifacecad.PiFaceCAD()

    while True:
        cad.lcd.clear()
        cad.lcd.cursor_off()
        cad.lcd.blink_off()
        cad.lcd.backlight_off()

        co2 = get_co2_value()

        cad.lcd.write("IP:{}\n".format(run_cmd(GET_IP_CMD)[:-1]))
        cad.lcd.write("CO2:" + co2 + "\n")

        # TODO Utiliser les interruptions pour capter l'appui
        if cad.switches[4].value == 1:
            cad.lcd.backlight_on()

        sleep(5)  # TODO Utiliser une variable + fichier de conf

        # Wait for the framework to stop
        # framework.wait_for_stop()  # Classic entry point...


if __name__ == "__main__":
    FORMAT = '%(asctime)s  %(message)s'
    logging.basicConfig(level=logging.DEBUG, filename='pvService.log', format=FORMAT)
    logging.info('Launching main')
    print('Launching main')
    main()

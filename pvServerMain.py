#!/usr/bin/python
# -- Content-Encoding: UTF-8 --


import pelix.framework
from pelix.ipopo.constants import use_ipopo
import pelix.shell

# Standard library
import logging


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
                              'pelix.http.address': '192.168.1.61',
                              'pelix.http.port': 3737
                          })

    logging.info("Installing PV bundle")
    print("Installing PV bundle")
    context.install_bundle("pvPanelsServlet").start()
    logging.info("PV bundle installed")
    print("PV bundle installed")

    # Wait for the framework to stop
    framework.wait_for_stop()

# Classic entry point...
if __name__ == "__main__":
    FORMAT = '%(asctime)s  %(message)s'
    logging.basicConfig(level=logging.DEBUG, filename='pvService.log', format=FORMAT)
    logging.info('Launching main')
    print('Launching main')
    main()

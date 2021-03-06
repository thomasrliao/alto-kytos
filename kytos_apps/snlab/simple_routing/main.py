"""Main module of snlab/simple_routing Kytos Network Application.

simple intra-domain routing app
"""

import json

from kytos.core import KytosNApp, log, rest
from kytos.core.helpers import listen_to
from pyof.foundation.basic_types import HWAddress
from pyof.foundation.network_types import Ethernet
from pyof.v0x01.controller2switch.stats_request import StatsTypes

from napps.snlab import network_monitor.Main

from napps.snlab.simple_routing import settings

class Main(KytosNApp):
    """Main class of snlab/simple_routing NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        """Replace the '__init__' method for the KytosNApp subclass.

        The setup method is automatically called by the controller when your
        application is loaded.

        So, if you have any setup routine, insert it here.
        """
        #pass
        log.info("simple routing was setup")

    def execute(self):
        """This method is executed right after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        #pass
        x = network_monitor.Main()






    def shutdown(self):
        """This method is executed when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        pass

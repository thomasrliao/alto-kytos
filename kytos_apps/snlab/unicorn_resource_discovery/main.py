"""Main module of snlab/unicorn_resource_discovery Kytos Network Application.

unicorn cross-domain resource discovery
"""

from kytos.core import KytosNApp, log

from napps.snlab.unicorn_resource_discovery import settings

import connexion
from napps.snlab.unicorn_resource_discovery.encoder import JSONEncoder


class Main(KytosNApp):
    """Main class of snlab/unicorn_resource_discovery NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        """Replace the '__init__' method for the KytosNApp subclass.

        The setup method is automatically called by the controller when your
        application is loaded.

        So, if you have any setup routine, insert it here.
        """
        #pass
        log.info("unicorn resource discovery napp is loaded!")

    def execute(self):
        """This method is executed right after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        #pass
        self.initREST()

    def shutdown(self):
        """This method is executed when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        pass

    #@staticmethod
    def initREST(self):
        log.info("we are starting our own restful api")
        app = connexion.App(__name__, specification_dir='./swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml', arguments={'title': 'Cross-domain path and resource discovery'})
        app.run(port=8080)






"""Main module of openalto/unicorn Kytos Network Application.

Unicorn
"""

import connexion
import threading

from kytos.core import KytosNApp, log

from napps.openalto.unicorn import settings
from napps.openalto.unicorn.swagger_server.encoder import JSONEncoder


class Main(KytosNApp):
    """Main class of openalto/unicorn NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        swaggerPort = 8080
        self.swaggerServerThread = SwaggerServerThread(swaggerPort)
        self.swaggerServerThread.start()
        log.info("Unicorn swagger HTTP server start at: http://0.0.0.0:"
                 + str(swaggerPort))

    def execute(self):
        """This method is executed right after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        pass

    def shutdown(self):
        """This method is executed when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """


class SwaggerServerThread(threading.Thread):
    def __init__(self, port=8080):
        threading.Thread.__init__(self, daemon=True)
        self.port = port

    def run(self):
        app = connexion.App(
            __name__, specification_dir=".//swagger_server/swagger")
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml', arguments={'title': "Unicorn"})
        app.run(port=self.port)

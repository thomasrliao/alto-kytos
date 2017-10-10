"""Main module of snlab/unicorn_resource_discovery Kytos Network Application.

unicorn cross-domain resource discovery
"""

from kytos.core import KytosNApp, log

from napps.snlab.unicorn_resource_discovery import settings

import connexion
import threading
from multiprocessing import Process

from napps.snlab.unicorn_resource_discovery.encoder import JSONEncoder

class SwaggerServerThread(threading.Thread):
    def __init__(self, port=8080):
        threading.Thread.__init__(self, daemon=True)
        self.port = port

    def run(self):
        app = connexion.App(
            __name__, specification_dir="./swagger")
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml', arguments={'title': "Unicorn Cross-Domain Resource Discovery"})
        app.run(port=self.port)

class Main(KytosNApp):
    """Main class of snlab/unicorn_resource_discovery NApp.

    This class is the entry point for this napp.
    """
    #swaggerPort = 8080
    #swaggerServerThread = SwaggerServerThread(swaggerPort)
    #server

    def setup(self):
        """Replace the '__init__' method for the KytosNApp subclass.

        The setup method is automatically called by the controller when your
        application is loaded.

        So, if you have any setup routine, insert it here.
        """
        #pass
        #swaggerPort = 8080
        #self.swaggerServerThread = SwaggerServerThread(swaggerPort)
        #self.__class__.swaggerServerThread.start()
        self.server = Process(target=self.initREST)
        self.server.start()
        log.info("unicorn resource discovery napp is loaded!")

    def execute(self):
        """This method is executed right after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        #pass
        #self.initREST()

    def shutdown(self):
        """This method is executed when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        #self.__class__.swaggerServerThread.join()
        #pass
        self.server.terminate()

    #@staticmethod
    def initREST(self):
        log.info("we are starting our own restful api")
        app = connexion.App(__name__, specification_dir='./swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml', arguments={'title': 'Cross-domain path and resource discovery'})
        app.run(port=8080)
#





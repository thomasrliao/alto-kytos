"""Main module of snlab/network_monitor Kytos Network Application.

monitor stats of topology, flows, and etc.
"""
import json

from kytos.core import KytosNApp, log, rest
from kytos.core.helpers import listen_to
from pyof.foundation.basic_types import HWAddress
from pyof.foundation.network_types import Ethernet
from pyof.v0x01.controller2switch.stats_request import StatsTypes

from napps.snlab.network_monitor.stats import Description, FlowStats, PortStats
from napps.snlab.network_monitor.stats_api import FlowStatsAPI, PortStatsAPI, StatsAPI
from napps.snlab.network_monitor import settings, constants


class Main(KytosNApp):
    """Main class of snlab/network_monitor NApp.

    This class is the entry point for this napp.
    """

    def setup(self):
        """Replace the '__init__' method for the KytosNApp subclass.

        The setup method is automatically called by the controller when your
        application is loaded.

        So, if you have any setup routine, insert it here.
        """
        """Initialize all statistics and set their loop interval."""
        log.info("network_monitor app is loaded.")
        self.execute_as_loop(settings.STATS_INTERVAL)

        # Initialize statistics
        msg_out = self.controller.buffers.msg_out
        self._stats = {StatsTypes.OFPST_DESC.value: Description(msg_out),
                       StatsTypes.OFPST_PORT.value: PortStats(msg_out),
                       StatsTypes.OFPST_FLOW.value: FlowStats(msg_out)}

        # Give Description and StatsAPI the controller
        Description.controller = self.controller
        StatsAPI.controller = self.controller


    def execute(self):
        """This method is executed right after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        
        """Query all switches sequentially and then sleep before repeating."""

        log.info("network_monitor app is executed periodically.")
        switches = list(self.controller.switches.values())
        for switch in switches:
            if not (switch.is_connected() and
                    switch.connection.protocol.version == 0x01):
                continue
            self._update_stats(switch)
        #pass

    @staticmethod
    @listen_to('kytos/of_core.v0x01.messages.in.ofpt_packet_in')
    def update_links(event):
        """Receive a kytos event and update links interface.

        Get the event kytos/of_core.messages.in.ofpt_packet_in and update
        the interface endpoints, ignoring the LLDP packages.

        Parameters:
            event (KytosEvent): event with Ethernet packet.
        """
        ethernet = Ethernet()
        ethernet.unpack(event.message.data.value)
        if ethernet.ether_type != constants.LLDP_ETHERTYPE:
            port_no = event.message.in_port
            hw_address = ethernet.source
            switch = event.source.switch
            interface = switch.get_interface_by_port_no(port_no.value)

            if interface is not None and \
               not interface.is_link_between_switches():
                interface.update_endpoint(hw_address)

    @staticmethod
    @listen_to('kytos/of_core.v0x01.messages.in.ofpt_port_status')
    def update_port_stats(event):
        """Receive a Kytos event and update port.

        Get the event kytos/of_core.messages.in.ofpt_port_status and update the
        port status.

        Parameters:
            event (KytosEvent): event with port_status content.
        """
        port_status = event.message
        reasons = ['CREATED', 'DELETED', 'MODIFIED']
        dpid = event.source.switch.dpid
        port_no = port_status.desc.port_no
        port_name = port_status.desc.name
        reason = reasons[port_status.reason.value]
        msg = 'The port %s (%s) from switch %s was %s.'
        log.debug(msg, port_no, port_name, dpid, reason)

    def shutdown(self):
        """This method is executed when your napp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        pass

    @rest('topology')
    def get_json_topology(self):
        """Return a json with topology details.

        Method responsible to return a json in /kytos/topology route.
        Returns:
            topology (string): json with topology details.
        """
        log.info("trying to get the topology")
        nodes, links = [], []
        switches = self.controller.switches

        switches_mac_address = []
        for switch in switches.values():
            for interface in switch.interfaces.values():
                switches_mac_address.append(interface.address)

        for _, switch in switches.items():
            nodes.append(switch.as_dict())
            for _, interface in switch.interfaces.items():
                link = {'source': switch.id,
                        'target': interface.id,
                        'type': 'interface'}
                nodes.append(interface.as_dict())
                links.append(link)

                for endpoint, _ in interface.endpoints:
                    if isinstance(endpoint, HWAddress):
                        if endpoint in switches_mac_address:
                            continue

                        link = {'source': interface.id,
                                'target': endpoint.value,
                                'type': 'link',
                                'link_speed': interface.get_hr_speed()}
                        host = {"type": 'host',
                                "id": endpoint.value,
                                "name": endpoint.value,
                                "mac": endpoint.value}
                        if host not in nodes:
                            nodes.append(host)
                        if not interface.is_link_between_switches():
                            links.append(link)
                    else:
                        link = {'source': interface.id,
                                'target': endpoint.id,
                                'type': 'link',
                                'link_speed2': interface.get_hr_speed()}
                        links.append(link)

        output = {'nodes': nodes, 'links': links}
        return json.dumps(output)

    def _update_stats(self, switch):
        for stats in self._stats.values():
            if switch.connection is not None:
                stats.request(switch.connection)

    @listen_to('kytos/of_core.v0x01.messages.in.ofpt_stats_reply')
    def listener(self, event):
        """Store switch descriptions."""
        msg = event.content['message']
        if msg.body_type.value in self._stats:
            stats = self._stats[msg.body_type.value]
            stats.listen(event.source.switch.dpid, msg.body)
        else:
            log.debug('No listener for %s in %s.', msg.body_type.value,
                      list(self._stats.keys()))

    # RESTful API for statistics

    @rest('<dpid>/ports/<int:port>')
    #@staticmethod
    def get_port_stats(self, dpid, port):
        """Return statistics for ``dpid`` and ``port``."""
        return PortStatsAPI.get_port_stats(dpid, port)

    @rest('<dpid>/ports')
    #@staticmethod
    def get_ports_list(self, dpid):
        """Return ports of ``dpid``."""
        return PortStatsAPI.get_ports_list(dpid)

    @rest('<dpid>/flows/<flow_hash>')
    #@staticmethod
    def get_flow_stats(self, dpid, flow_hash):
        """Return statistics of a flow in ``dpid``."""
        return FlowStatsAPI.get_flow_stats(dpid, flow_hash)

    @rest('<dpid>/flows')
    #@staticmethod
    def get_flow_list(self, dpid):
        """Return all flows of ``dpid``."""
        log.info("get_flow_list is called")
        return FlowStatsAPI.get_flow_list(dpid)


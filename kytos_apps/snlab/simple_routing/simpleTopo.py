from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI



class NetworkTopo(Topo):
	""" A simple network topology for testing purposes """
	def build(self, **_opts):
		rA, rB = [self.addNode(name) for name in ['rA', 'rB']]
		net1 = '10.0.0.0/24'
		net2 = '10.0.1.0/24'
		s1, s2 = [self.addSwitch(s) for s in ['s1','s2']]
		h1 = self.addHost('h1', ip='172.16.0.1')
		
		# link switches to routers
		self.addLink(s1, rA, params2={'ip': net1})
		self.addLink(s1, rB, params2={'ip': net1})
		self.addLink(s2, rA, params2={'ip': net2})
		self.addLink(s2, rB, params2={'ip': net2})
		
		self.addLink(h1, rB)


def run():
	topo = NetworkTopo()
	net = Mininet(topo=topo)
	net.start()

	info( '***Routing Table on Router:\n')
	info(net['rA'].cmd('route'))
	CLI(net)

	net.stop()


if __name__ == '__main__':
	setLogLevel('info')
	run()
	

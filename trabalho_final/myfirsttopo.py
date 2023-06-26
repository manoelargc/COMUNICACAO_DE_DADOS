
# TRABALHO FINAL - QUESTAO 1 (ENTREGA 21/06)

# Comunicacao de dados 23.1
# Manoela Resende 2210100235
# Eduarda Sifuentes 2210100446

#------------------------------------------------------------------------------
# 1 - implemente a topologia descrita no arquivo no Mininet. A
# topologia tem 50 switch/roteador. Cada linha do arquivo representa as
# arestas/enlaces entre os switches/roteadores. Adicione 1 host em cada switch
#------------------------------------------------------------------------------


#=================================
#CRIA 246 LINKS
#=================================

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class MyFirstTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Le o arquivo de topologia
        with open('hs1.txt', 'r') as file:
            lines = file.readlines()

            # Cria os switches
            switches = {}
            for line in lines:
                switch1, switch2, _ = line.strip().split(' ')
                switches[switch1] = self.addSwitch('s{}'.format(switch1))
                switches[switch2] = self.addSwitch('s{}'.format(switch2))

                # Cria a ligacao entre os switches
                self.addLink(switches[switch1], switches[switch2])

            # Cria os hosts e adiciona uma ligacao a cada switch
            for switch in switches.values():
                host = self.addHost('h{}'.format(switch.replace('s', '')))
                self.addLink(host, switch)


topos = {'myfirsttopo': MyFirstTopo}


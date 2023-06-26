# TRABALHO FINAL - QUESTAO 2 (ENTREGA 28/06)

# Comunicacao de dados 23.1
# Manoela Resende 2210100235
# Eduarda Sifuentes 2210100446

#------------------------------------------------------------------------------
# 2 - Configure regras de encaminhamento (como realizado no Lab 5)
# na topologia acima de forma que: todos os hosts possam se comunicar atraves de 
# um caminho minimo. Um caminho minimo em um grafo pode ser implementado de
# varias maneiras (por exemplo, atraves do algoritmo de Dijkstra).
#------------------------------------------------------------------------------

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from myfirsttopo import MyFirstTopo

def configure_routing(topology):
    # Obtem uma lista de switches do objeto de topologia
    switches = topology.switches()

    # Obtem uma lista de hosts do objeto de topologia
    hosts = topology.hosts()

    # Cria um dicionario vazio para armazenar as tabelas de encaminhamento
    routing_tables = {}

    # Inicializa todas as tabelas de encaminhamento com um dicionario vazio
    for switch in switches:
        routing_tables[switch] = {}

    # Percorre cada host e determina o caminho minimo para todos os outros hosts
    for src_host in hosts:
        src_switch = src_host.defaultIntf().node1  # Obtem o switch ao qual o host esta conectado
        routing_tables[src_switch][src_host] = src_host  # Define o host atual como o proximo hop para si mesmo

        # Inicializa as distancias com infinito para todos os switches
        distances = {switch: float('inf') for switch in switches}
        distances[src_switch] = 0

        # Inicializa a lista de switches visitados
        visited = set()

        # Executa o algoritmo de Dijkstra
        while len(visited) < len(switches):
            # Encontra o switch nao visitado com a menor distancia
            min_distance = float('inf')
            min_switch = None
            for switch in switches:
                if switch not in visited and distances[switch] < min_distance:
                    min_distance = distances[switch]
                    min_switch = switch

            visited.add(min_switch)

            # Atualiza as distancias dos switches adjacentes ao switch atual
            for neighbor in topology.neighbors(min_switch):
                distance = distances[min_switch] + 1  # A distancia entre switches eh considerada 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    routing_tables[src_switch][neighbor] = routing_tables[src_switch][min_switch]

    # Configura as regras de encaminhamento nos switches
    for switch, routing_table in routing_tables.items():
        for destination, next_hop in routing_table.items():
            command = 'ovs-ofctl add-flow {} dl_dst={} actions=output:{}'.format(switch, destination.MAC(), next_hop.defaultIntf().port)
            switch.cmd(command)

if __name__ == '__main__':
    topo = MyFirstTopo()
    net = Mininet(topo)
    net.start()

    # Configura as regras de encaminhamento usando o algoritmo de Dijkstra
    configure_routing(topo)

    CLI(net)
    net.stop()

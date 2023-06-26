# TRABALHO FINAL - QUESTAO 3 (ENTREGA 05/07)

# Comunicacao de dados 23.1
# Manoela Resende 2210100235
# Eduarda Sifuentes 2210100446

#------------------------------------------------------------------------------
# 3 - Configure regras de encaminhamento (como realizado no Lab 5)
# na topologia acima de forma que: todos os hosts possam se comunicar
# atraves de caminhos disjuntos. Um caminho eh disjunto se nao compartilha
# enlaces/arestas. Se nao for possivel criar um caminho disjunto, a comunicacao 
# nao deve ser permitida. Apos computar os caminhos disjuntos entre todos 
# os hosts, indicar quantos pares de comunicacoes sao viaveis
#------------------------------------------------------------------------------

# obs: fiz esse arquivo separado do script pois nao sabia se teria que ser junto ou separado

from myfirsttopo import MyFirstTopo

def configure_forwarding_paths(topo):
    # Obtem a lista de switches
    switches = topo.switches()

    # Obtem a lista de hosts
    hosts = topo.hosts()

    # Obtem todos os pares de comunicações possíveis
    communication_pairs = [(h1, h2) for h1 in hosts for h2 in hosts if h1 != h2]

    # Inicializa o contador de comunicacoes viaveis
    viable_communications = 0

    # Configura as regras de encaminhamento para cada par de hosts
    for h1, h2 in communication_pairs:
        # Obtem o switch associado a cada host
        switch1 = topo.node_to_node[h1]
        switch2 = topo.node_to_node[h2]

        # Verifica se é possível criar caminhos disjuntos entre os switches
        if is_disjoint_path_available(topo, switch1, switch2):
            viable_communications += 1
            print("Comunicação viável entre {} e {}".format(h1, h2))
            # Adiciona regras de encaminhamento nos switches
            add_forwarding_rules(topo, switch1, switch2)
        else:
            print("Comunicação inviável entre {} e {}".format(h1, h2))

    print("Número de comunicações viáveis: {}".format(viable_communications))


def is_disjoint_path_available(topo, switch1, switch2):
    # Verifica se existe pelo menos um caminho disjunto entre os switches

    # Cria uma cópia da topologia para simular caminhos
    simulated_topo = topo.copy()

    # Remove a ligação entre os switches para simular a indisponibilidade do link
    simulated_topo.remove_link(switch1, switch2)

    # Obtem todos os caminhos possíveis entre os switches na topologia simulada
    paths = simulated_topo.all_simple_paths(switch1, switch2)

    # Verifica se existem caminhos disjuntos (sem compartilhar enlaces/arestas)
    for path in paths:
        if len(path) > len(set(path)):
            return False

    return True


def add_forwarding_rules(topo, switch1, switch2):
    # Adiciona as regras de encaminhamento nos switches para direcionar o trafego entre os hosts

    # Obtem a lista de switches
    switches = topo.switches()

    # Percorre cada switch e adiciona a regra de encaminhamento para os pares de hosts
    for switch in switches:
        for h1 in topo.hosts():
            for h2 in topo.hosts():
                if h1 != h2 and h1 != switch1 and h2 != switch2:
                    command = 'ovs-ofctl add-flow {} dl_dst={} actions=output:{}'.format(switch, h2.MAC(), h1.defaultIntf().port)
                    switch.cmd(command)


if __name__ == '__main__':
    topo = MyFirstTopo()
    configure_forwarding_paths(topo)


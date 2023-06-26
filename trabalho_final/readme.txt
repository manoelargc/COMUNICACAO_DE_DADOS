# README 
# Trabalho Final - Comunicação de Dados - 3º Semestre - Ciência da Computação - 23.1
- Manoela Resende
- Eduarda Sifuentes

Este projeto é propriedade do perfil do GitHub de Manoela Resende (manoelargc). Ele foi desenvolvido como parte do Trabalho Final da disciplina de Comunicação de Dados do 3º Semestre de Ciência da Computação - 23.1.


## Código 1 - Implementação da Topologia

O primeiro código implementa a topologia descrita no arquivo no Mininet. A topologia consiste em 50 switch/roteador, onde cada linha do arquivo representa as arestas/enlaces entre os switches/roteadores. Além disso, adiciona 1 host em cada switch.

Antes de executar o código, certifique-se de ter o arquivo `hs1.txt` disponível. Ele contém o link para o grafo da topologia a ser utilizado. Você pode baixar o arquivo de topo por meio do seguinte link: [hs1.txt](https://www.dropbox.com/s/eesdxvin964v0os/hs1.txt?dl=0). Faça o download e coloque-o no mesmo diretório em que o código `myfirsttopo.py` está localizado.

Para executar o código, siga as etapas abaixo:

1. Certifique-se de ter o Mininet instalado.
2. Abra um terminal e navegue até o diretório onde o arquivo do código está localizado.
3. Execute o seguinte comando: `sudo mn --custom myfirsttopo.py --topo myfirsttopo --controller remote --arp`

Isso criará a topologia definida no arquivo `myfirsttopo.py`, onde cada switch/roteador terá um host associado. O parâmetro `--controller remote` define o controlador como remoto, e `--arp` permite que os hosts executem o protocolo ARP para resolução de endereços.

Isso criará a topologia definida no arquivo `hs1.txt`, onde cada switch/roteador terá um host associado.


## Código 2 - Configuração de Roteamento

O segundo código calcula as tabelas de roteamento com base no algoritmo de Dijkstra, para encontrar o caminho minimo no grafo, e adiciona as regras de encaminhamento nos switches da topologia. Cada switch será configurado para encaminhar pacotes para os destinos corretos de acordo com a tabela de roteamento.

Para executar o código, siga as etapas abaixo:

1. Certifique-se de ter o Mininet instalado.
2. Abra um terminal e navegue até o diretório onde o arquivo do código está localizado.
3. Execute o seguinte comando: `sudo python minimo_q2.py`

Isso calculará as tabelas de roteamento usando o algoritmo de Dijkstra e configurará as regras de encaminhamento nos switches da topologia.


## Código 3 - Configuração de Caminhos de Encaminhamento Disjuntos

O terceiro código verifica se é possível criar caminhos disjuntos entre pares de hosts na topologia e adiciona regras de encaminhamento nos switches para direcionar o tráfego. Ele simula a indisponibilidade de links e verifica se existem caminhos disjuntos entre os switches.

Para executar o código, siga as etapas abaixo:

1. Certifique-se de ter o Mininet instalado.
2. Abra um terminal e navegue até o diretório onde o arquivo do código está localizado.
3. Execute o seguinte comando: `sudo python disjunto_q3.py`

Certifique-se de ter as dependências do Mininet instaladas, que o arquivo `hs1.txt` esteja no mesmo diretório do arquivo `myfirsttopo.py` e de seguir as instruções específicas de cada código.

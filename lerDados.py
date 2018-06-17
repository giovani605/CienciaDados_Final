import pickle
import csv

print(dict)
dados = open("dados2.csv",'r')
csv_partidas = csv.DictReader(dados)
fields = ['accountId','matchId','visionScore']
rankPlayers = open('listPlayers.csv','r')
rank_csv = csv.DictReader(rankPlayers)
print(rank_csv.fieldnames)
# tenho que colocar o resultado do csv do rank em um dicionario pq vou consultar ele muitas vezes
lista = list(rank_csv)

def procurarRank(contaId):
    for entry in lista:
        if entry["summonerId"] == contaId:
            return entry
    print("nao encontrei")


fields = ['summonerId','accountId','tier','rank','matchId']
tabela = open('saida.csv', 'w')
csv_writer = csv.DictWriter(tabela, fieldnames=fields, delimiter=',')
csv_writer.writeheader()

def processar(player,matchId):
    ## chegando aqui cosnegui pogar o stat do meu player
    linha = {}
    linha[fields[0]] = player['summonerId']
    linha[fields[1]] = player['accountId']
    linha[fields[2]] = player['tier']
    linha[fields[3]] = player['rank']
    linha[fields[4]] = matchId
    print("salvei")
    print(linha)
    csv_writer.writerow(linha)

for match in csv_partidas:
    ## carregar o dado do match inteiro
    arquivo = open("dados/" + str(match["matchId"]) + ".pkl", 'rb')
    partida = pickle.load(arquivo)
    ## a variavel dict eh aquele json match
    ## o match account id eh na vdd o summoner id
    playerRank = procurarRank(match["accountId"])
    for participante in partida["participantIdentities"]:
        teste = participante["player"]
        if str(participante["player"]["summonerId"]) == match["accountId"]:
            participanteId = participante["participantId"]
            for dados in partida["participants"]:
                if dados["participantId"] is participanteId:
                    processar(playerRank, match["matchId"])
                    print("cheguei")

import riotwatcher
import csv


fields = ['accountId','matchId','visionScore']


tabela = open('dados2.csv','w')
csv_writer = csv.DictWriter(tabela, fieldnames=fields, delimiter=',')
csv_writer.writeheader()
def processar(dados,accountId,matchId):
    ## chegando aqui cosnegui pogar o stat do meu player

    linha = {}
    linha[fields[0]] = accountId
    linha[fields[1]] = matchId
    linha[fields[2]] = dados["stats"]["visionScore"]
    print(linha)
    csv_writer.writerow(linha)
    ## qual dados separar



arq = open("key.txt")

key = arq.readline()
watcher = riotwatcher.RiotWatcher(key)

perfil = watcher.summoner.by_name(region="br1",summoner_name="GuaxininAtomico")


myId = perfil["accountId"]
myIdSum = perfil["id"]
myNick = perfil["name"]

## criar uma lista com os jogadores que vai comecar

partidas = watcher.match.matchlist_by_account(region="br1", account_id=myId)

cont = 0
for match in partidas["matches"]:
    if cont == 10:
        break
    else:
        cont += 1
    partida = watcher.match.by_id(region="br1", match_id=match["gameId"])
    for participante in partida["participantIdentities"]:
            if participante["player"]["summonerId"] == myIdSum:
                participanteId = participante["participantId"]
                for dados in partida["participants"]:
                    if dados["participantId"] is participanteId:
                        processar(dados=dados,accountId=myIdSum,matchId=match["gameId"])




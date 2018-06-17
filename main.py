from http.client import HTTPException

import riotwatcher
import csv
import time
import pickle

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
    print("salvei")
    print(linha)
    csv_writer.writerow(linha)
    ## qual dados separar



arq = open("key.txt")


key = arq.readline()
watcher = riotwatcher.RiotWatcher(key)
## criar uma lista com os jogadores que vai comecar
players = open("listPlayers.csv")
fields2 = ['summonerId','accountId','tier','rank']
csv_reader = csv.DictReader(players)
## parametros
partidasPorPlayer = 10
regiao = "br1"
# fila 5x5 solo
fila=420

print("comecei em ")
print(time.asctime(time.localtime(time.time())))
for player in csv_reader:
    print(player)
    idSum = player["summonerId"]
    idConta = player["accountId"]
    try:
        partidas = watcher.match.matchlist_by_account(region=regiao,account_id=idConta,queue=fila)
        cont = 0
        for match in partidas["matches"]:
            if cont == partidasPorPlayer:
                break
            else:
                cont += 1
            partida = watcher.match.by_id(region=regiao, match_id=match["gameId"])
            try:
                arquivo = open(str("dados/" + str(match["gameId"])+".pkl"), 'wb')
                pickle.dump(partida, arquivo)
                arquivo.close()
            except:
                arquivo = open(str("dados/" + str(match["gameId"])+".pkl"), 'wb+')
                pickle.dump(partida, arquivo)
                arquivo.close()


            for participante in partida["participantIdentities"]:
                    teste = participante["player"]
                    if str(participante["player"]["summonerId"]) == idSum or str(participante["player"]["accountId"]) == idConta:
                        participanteId = participante["participantId"]
                        for dados in partida["participants"]:
                            if dados["participantId"] is participanteId:
                                processar(dados=dados, accountId=idSum, matchId=match["gameId"])
    except Exception as e:
        print(e)

print("terminei em ")
print(time.asctime(time.localtime(time.time())))



#perfil = watcher.summoner.by_name(region="br1",summoner_name="GuaxininAtomico")
#myId = perfil["accountId"]
#myIdSum = perfil["id"]
#myNick = perfil["name"]




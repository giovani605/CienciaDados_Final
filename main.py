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
## criar uma lista com os jogadores que vai comecar
players = open("playersStart.txt")
## parametros
partidasPorPlayer = 2
regiao = "br1"

for idSum in players.readlines():
    idSum = idSum.strip()
    print(idSum)
    partidas = watcher.match.matchlist_by_account(region=regiao,account_id=idSum)
    cont = 0
    for match in partidas["matches"]:
        if cont == partidasPorPlayer:
            break
        else:
            cont += 1
        partida = watcher.match.by_id(region=regiao, match_id=match["gameId"])
        for participante in partida["participantIdentities"]:
                if participante["player"]["summonerId"] == idSum:
                    participanteId = participante["participantId"]
                    for dados in partida["participants"]:
                        if dados["participantId"] is participanteId:
                            processar(dados=dados, accountId=idSum, matchId=match["gameId"])



#perfil = watcher.summoner.by_name(region="br1",summoner_name="GuaxininAtomico")
#myId = perfil["accountId"]
#myIdSum = perfil["id"]
#myNick = perfil["name"]




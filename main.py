import riotwatcher

def processar(dados):
    ## chegando aqui cosnegui pogar o stat do meu player
    print(dados)



arq = open("key.txt")

key = arq.readline()
watcher = riotwatcher.RiotWatcher(key)

perfil = watcher.summoner.by_name(region="br1",summoner_name="GuaxininAtomico")


myId = perfil["accountId"]
myIdSum = perfil["id"]
myNick = perfil["name"]

partidas = watcher.match.matchlist_by_account(region="br1", account_id=myId)

for match in partidas["matches"]:
    partida = watcher.match.by_id(region="br1", match_id=match["gameId"])
    for participante in partida["participantIdentities"]:
            if participante["player"]["summonerId"] == myIdSum:
                participanteId = participante["participantId"]
                for dados in partida["participants"]:
                    if dados["participantId"] is participanteId:
                        processar(dados)




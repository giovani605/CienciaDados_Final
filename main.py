import riotwatcher

arq = open("key.txt")

key = arq.readline()
watcher = riotwatcher.RiotWatcher(key)

perfil = watcher.summoner.by_name(region="br1",summoner_name="GuaxininAtomico")


myId = perfil["accountId"]

partidas = watcher.match.matchlist_by_account(region="br1", account_id=myId)

for match in partidas["matches"]:
    print(match)
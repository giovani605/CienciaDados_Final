import riotwatcher
import csv

## esse scirpt gera uma lista dos players pra gente procurar os amtch
fields = ['summonerId','accountId','tier','rank']


tabela = open('listPlayers.csv','w')
csv_writer = csv.DictWriter(tabela, fieldnames=fields, delimiter=',')
csv_writer.writeheader()
# Dicionario que guarda os players que eu ja dd no csv
playersConhecidos = {}


def testarPlayer(numero):
    if numero in playersConhecidos.keys():
        return False
    else:
        playersConhecidos[numero] = numero
        return True



def salvarPlayer(IdSummoner,IdAccount,tier,rank):
    ## chegando aqui cosnegui pogar o stat do meu player

    linha = {}
    linha[fields[0]] = IdSummoner
    linha[fields[1]] = IdAccount
    linha[fields[2]] = tier
    linha[fields[3]] = rank
    if testarPlayer(IdAccount):
        print("salvando player")
        print(linha)
        csv_writer.writerow(linha)


arq = open("key.txt")


key = arq.readline()
watcher = riotwatcher.RiotWatcher(key)
## criar uma lista com os jogadores que vai comecar
players = open("playersStart.txt")
## parametros
partidasPorPlayer = 5
regiao = "br1"

for nome in players.readlines():
    nome = nome.strip()
    playerDados = watcher.summoner.by_name(region=regiao,summoner_name=nome)
    print(playerDados)
    idSum = playerDados["accountId"]
    try:
        partidas = watcher.match.matchlist_by_account(region=regiao,account_id=idSum,queue=420)
        cont = 0
        for match in partidas["matches"]:
            if cont == partidasPorPlayer:
                break
            else:
                cont += 1
            partida = watcher.match.by_id(region=regiao, match_id=match["gameId"])
            for participante in partida["participantIdentities"]:
                    IdSummoner = participante['player']['summonerId']
                    IdAccount = participante['player']['accountId']
                    ranked = watcher.league.positions_by_summoner(region=regiao,summoner_id=IdSummoner)
                    print(ranked)
                    for a in ranked:
                        if a["queueType"] == 'RANKED_SOLO_5x5':
                            tier = a["tier"]
                            rank = a["rank"]
                            salvarPlayer(IdSummoner,IdAccount,tier,rank)
    except:
        print("erro")

         #       if participante["player"]["summonerId"] == idSum:
          #          participanteId = participante["participantId"]
           #         for dados in partida["participants"]:
            #            if dados["participantId"] is participanteId:
             #               processar(dados=dados, accountId=idSum, matchId=match["gameId"])



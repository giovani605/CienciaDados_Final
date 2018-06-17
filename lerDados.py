import pickle
import csv

print(dict)
dados = open("dados2.csv",'r')
csv_reader = csv.DictReader(dados)
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



for match in csv_reader:
    ## carregar o dado do match inteiro
    arquivo = open("dados/"+str(match["matchId"])+".pkl", 'rb')
    dict = pickle.load(arquivo)
    ## a variavel dict eh aquele json match
    ## o match account id eh na vdd o summoner id
    rank = procurarRank(match["accountId"])
    print(rank)
    print(dict)
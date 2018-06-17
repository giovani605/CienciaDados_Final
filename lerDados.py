import pickle
import csv

print(dict)
dados = open("dados2.csv",'r')
csv_reader = csv.DictReader(dados)
fields = ['accountId','matchId','visionScore']


for match in csv_reader:
    ## carregar o dado do match inteiro
    arquivo = open("dados/"+str(match["matchId"])+".pkl", 'rb')
    dict = pickle.load(arquivo)
    ## a variavel dict eh aquele json match
    print(dict)
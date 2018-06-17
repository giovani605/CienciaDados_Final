import pickle

arquivo = open("dados/1398002458.pkl",'rb')
dict = pickle.load(arquivo)
print(dict)
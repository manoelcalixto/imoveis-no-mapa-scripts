from geopy import geocoders
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection.mydb
tipos = db.tipos

listaTipoAluguel = db.imoveis.find({"operacao": "Aluguel"}).distinct("tipo")

print (listaTipoAluguel)

listaTipoVenda = db.imoveis.find({"operacao": "Venda"}).distinct("tipo")

print (listaTipoVenda)

for tipoAluguel in listaTipoAluguel:

	oTipoAluguel = {"operacao": "Aluguel", "tipo": tipoAluguel}
	idTipoAluguel = tipos.insert_one(oTipoAluguel).inserted_id

for tipoVenda in listaTipoVenda:

	oTipoVenda = {"operacao": "Aluguel", "tipo": tipoVenda}
	idTipoAluguel = tipos.insert_one(oTipoVenda).inserted_id
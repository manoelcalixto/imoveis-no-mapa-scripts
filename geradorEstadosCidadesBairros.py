# -*- coding: utf-8 -*-

from geopy import geocoders
from pymongo import MongoClient

geolocator = geocoders.GoogleV3("AIzaSyCehc38dmsov9olbD7XBLiumKHuv6TbW0A")

connection = MongoClient('localhost', 27017)
db = connection.mydb
imoveis = db.imoveis
estados = db.estados
cidades = db.cidades
bairros = db.bairros

db.estados.drop()
db.cidades.drop()
db.bairros.drop()

print(db.imoveis.distinct("estado"))

listaEstados = db.imoveis.distinct("estado")

for estado in listaEstados:
    print(estado)
    listaCidades = db.imoveis.find({"estado": estado}).distinct("cidade")
    location = geolocator.geocode(estado)
    print(location.latitude, location.longitude)

    oEstado = {"estado": estado, "latitude": location.latitude, "longitude": location.longitude}
    post_id = estados.insert_one(oEstado).inserted_id
    print(post_id)


    for cidade in listaCidades:
        #print(cidade)
        listaBairros = db.imoveis.find({"estado": estado, "cidade": cidade}).distinct("bairro")
        location = geolocator.geocode(estado + ' ' + cidade)
        print(location.latitude, location.longitude)

        oCidade = {"cidade": cidade, "estado": estado, "latitude": location.latitude, "longitude": location.longitude}
        post_id = cidades.insert_one(oCidade).inserted_id
        print(post_id)

        for bairro in listaBairros:
            location = geolocator.geocode(estado + ' ' + cidade + ' ' + bairro)
            print(location.latitude, location.longitude)

            oBairro = {"bairro": bairro, "cidade": cidade, "estado": estado, "latitude": location.latitude, "longitude": location.longitude}
            post_id = bairros.insert_one(oBairro).inserted_id
            print(post_id)

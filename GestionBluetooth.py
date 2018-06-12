#!/usr/bin/env python3

import json
import pickle
import subprocess

def lecturejsonfic(file):
	try:
		with open(file, 'r') as fic:
			data = fic.read()
	except:
		print('Erreur dans le fichier JSON')
		exit(1)
	config = json.loads(data)
	return config

def ecriturejsonfic(file , data):
	try:
		with open(file, 'w') as fic:
	except:
		print('Erreur dans l ouverture du fichier JSON')
		exit(1)
	
	
def lecturebinfic(file):
	with open(file, 'rb') as fic:
		return fic

def ecriturebinfic(file):
	with open(file, 'wb') as fic:
		return fic

def recupsession(file):	##Prend un fichier binaire et Renvoi un objet
	recup = pickle.Unpickler(file)
	return recup.load()

def svgsession(object, fic): ##Prend l'objet et le fichier de sortie
	ecriturebinfic(fic)
	svg = pickle.Pickler(fic)
	svg.dump(object)

if __name__ == '__main__':
	###Récupération du fichier de configuration
	config = lecturejsonfic(enceinteJSON)
	mac = 
	indexNouveau = config.index(mac)
	###Recupération de l'existant
	session = lecturebinfic(session.binaire)
	objsession = recupsession(session)
	###Si Vérification de la priorité du péripherique et des exceptions
	if session.indexobj > indexNouveau:
		###Suppression de la session en cours et des services bloquants
		for services in fsgfugz<sf:
			subprocess.run(["systemctl", "stop", services])
		session.kill()
		###Création de l'objet
		session = subprocess.Popen(['bluealsa-aplay', mac], shell=True, check=False)
		session.indexobj = indexNouveau
		###Ecriture de la session courante dans le fichier
		ficsession = ecriturebinfic(session.binaire)
		svgsession(session, ficsession)

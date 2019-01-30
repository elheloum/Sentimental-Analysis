#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 8 14:45:36 2018

@author: myriamelhelou & juliecoletti
"""
import treetaggerwrapper
import csv
import re
import nltk



def liste_uni():
	
	""" 

	:param liens:
    :return:

	"""

#Fichier d'entrée
	lecture_csv = csv.reader(open('sortie_liens.csv', mode="r", encoding="utf8"), delimiter=",")

#Fichiers de sorties
	csv_unigrams = csv.writer(open("notes_unigrams_ajout.csv", mode="w", encoding="utf8", newline=''), delimiter=",")
	csv_unigrams_SMO = csv.writer(open("notes_unigrams_SMO.csv", mode="w", encoding="utf8", newline=''), delimiter=",")
	csv_bigrams = csv.writer(open("notes_bigrams.csv", mode="w", encoding="utf8", newline=''), delimiter=",")
	csv_bigrams_SMO = csv.writer(open("notes_bigrams_SMO.csv", mode="w", encoding="utf8", newline=''), delimiter=",")
	csv_trigrams = csv.writer(open("notes_trigrams.csv", mode="w", encoding="utf8", newline=''), delimiter=",")
	csv_trigrams_SMO = csv.writer(open("notes_trigrams_SMO.csv", mode="w", encoding="utf8", newline=''), delimiter=",")

#Paramètres utilisés (français)
	tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')

#Création de la liste 'liste_commentaires' contenant la liste de tous les commentaires
	liste_commentaires = []
	
	for row in lecture_csv:
		liste_commentaires.append(row[2])

#Etiquettage des commenataires
		for comm in liste_commentaires:
			comm = re.sub(r'\.(\w+)', r'. \1', comm)
			tagged = tagger.tag_text(comm)
			tags = treetaggerwrapper.make_tags(tagged)

#Créations des listes 'liste_unigrams' et 'liste_unigrams_SMO' contenant respectivement (pour chaque commentaire)
#la liste des unigrams et la liste des unigrams sans les mots outils
			liste_unigrams = []
			liste_unigrams_SMO = []
			
			#'liste_etiquettes_mot_outil' est la liste qui contient les étiquettes des catégories considérées comme mots outils
			liste_etiquettes_mot_outil = ["ABR", "DET:ART", "DET:POS", "INT", "KON", "NAM", "PRO",
										  "PRO:DEM", "PRO:IND", "PRO:PER", "PRO:POS", "PRO:REL",
										  "PRP", "PRP:det", "PUN", "PUN:cit", "SENT", "SYM"]
			for elt in tags:
				if elt.pos:
					liste_unigrams.append(elt.word)
					if elt.pos not in liste_etiquettes_mot_outil:
						liste_unigrams_SMO.append(elt.word)

#Création des fichiers : 

	#UNIGRAMS
		str_unigrams= " ".join(liste_unigrams)
		row.insert(1,str_unigrams)   
		csv_unigrams.writerow((row[0],row[1]))

	#UNIGRAMS SANS MOTS-OUTILS
		str_unigrams_SMO= " ".join(liste_unigrams_SMO)
		row.insert(1,str_unigrams_SMO)   
		csv_unigrams_SMO.writerow((row[0],row[1]))

	#BIGRAMS
		liste_bigrams = []
		nltk_bigrams = nltk.bigrams(liste_unigrams)
		for grams in nltk_bigrams:
			bigrams='_'.join(grams)
			liste_bigrams.append(bigrams)
		str_bigrams= " ".join(liste_bigrams)
		row.insert(1,str_bigrams)   
		csv_bigrams.writerow((row[0],row[1]))

	#BIGRAMS SANS MOTS-OUTILS
		liste_bigrams_SMO = []
		nltk_bigrams_SMO = nltk.bigrams(liste_unigrams_SMO)
		for grams in nltk_bigrams_SMO:
			bigrams_SMO='_'.join(grams)
			liste_bigrams_SMO.append(bigrams_SMO)
		str_bigrams_SMO= " ".join(liste_bigrams_SMO)
		row.insert(1,str_bigrams_SMO)   
		csv_bigrams_SMO.writerow((row[0],row[1]))

	#TRIGRAMS
		liste_trigrams = []
		nltk_trigrams = nltk.trigrams(liste_unigrams)
		for grams in nltk_trigrams:
			trigrams='_'.join(grams)
			liste_trigrams.append(trigrams)
		str_trigrams= " ".join(liste_trigrams)
		row.insert(1,str_trigrams)   
		csv_trigrams.writerow((row[0],row[1]))

	#TRIGRAMS SANS MOTS-OUTILS
		liste_trigrams_SMO = []
		nltk_trigrams_SMO = nltk.trigrams(liste_unigrams_SMO)
		for grams in nltk_trigrams_SMO:
			trigrams_SMO='_'.join(grams)
			liste_trigrams_SMO.append(trigrams_SMO)
		str_trigrams_SMO= " ".join(liste_trigrams_SMO)
		row.insert(1,str_trigrams_SMO)   
		csv_trigrams_SMO.writerow((row[0],row[1]))


if __name__ == '__main__':
    liste_uni()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 10:15:36 2018

@author: myriamelhelou & juliecoletti
"""

import os
import csv


def create_folder():
    newpath = r'../Projet_M2_ELHELOU_COLETTI/txt_sentoken_unigram/neg'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath2 = r'../Projet_M2_ELHELOU_COLETTI/txt_sentoken_unigram/pos'
    if not os.path.exists(newpath2):
        os.makedirs(newpath2)


def create_files_pos(csvfile):
    csv_comments = csv.reader(open(csvfile, mode="r", encoding="utf8"))
    filename_log = "texto_POS_" + csvfile
    fichier_log = open(filename_log + ".log", mode='w', encoding='UTF-8')
    fichier_log.write("Le nombre total de fichier traité est : 1000 fichiers")
    fichier_log.write("\n")
    nb = 0
    for row in csv_comments:
        if nb == 1000:
            break
        else:
            if int(row[0]) > 30:
                filename = "cv{:03}".format(nb)
                outFileName = "../Projet_M2_ELHELOU_COLETTI/txt_sentoken_trigram/pos/" + \
                              filename+".txt"
                outFile = open(outFileName, "w")
                outFile.write(row[1])
                fichier_log.write(" Nom du fichier: " + filename + ":")
                fichier_log.write("\n")
                fichier_log.write("nombre de mots: {0}".format(len(row[1].split(' '))))
                fichier_log.write("\n")
                outFile.close()
                nb += 1
    fichier_log.close()


def create_files_neg(csvfile):
    csv_comments = csv.reader(open(csvfile, mode="r", encoding="utf8"))
    filename_log = "texto_NEG_"+csvfile
    fichier_log = open(filename_log+".log", mode='w', encoding='UTF-8')
    fichier_log.write("Le nombre total de fichier traité est : 1000 fichiers")
    fichier_log.write("\n")
    nb = 0
    for row in csv_comments:
        if nb == 1000:
            break
        else:
            if int(row[0]) <= 30:
                filename = "cv{:03}".format(nb)
                outFileName = "../Projet_M2_ELHELOU_COLETTI/txt_sentoken_trigram/neg/" + \
                              filename+".txt"
                outFile = open(outFileName, "w")
                outFile.write(row[1])
                outFile.close()
                fichier_log.write(" Nom du fichier: " + filename + ":")
                fichier_log.write("\n")
                fichier_log.write("nombre de mots: {0}".format(len(row[1].split(' '))))
                fichier_log.write("\n")
                nb += 1
    fichier_log.close()


if __name__ == '__main__':
    # create_folder()
    create_files_pos("notes_trigrams.csv")
    create_files_neg("notes_trigrams.csv")


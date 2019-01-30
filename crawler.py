#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:30:36 2018

@author: myriamelhelou & juliecoletti
"""

import urllib
import urllib.request
import re
import time
import html
import csv


def crawler(liens):
    """

    :param liens:
    :return:
    """
    # les regex pour rechercher le commentaire et la note associée
    re_commentaire = r'</div><DIV class="prw_rup prw_reviews_text_summary_hsx" ' \
                     r'data-prwidget-name="reviews_text_summary_hsx" data-prwidget-init="handlers">' \
                     r'<div class="entry"><p class="partial_entry">([^<]+)(?:<span ' \
                     r'class="taLnk ulBlueLinks" onclick="widgetEvCall\(\'handlers.clickExpand\',' \
                     r'event,this\);">Plus</span>)?</p>'
    re_note = r'<div class="rating reviewItemInline"><span class="ui_bubble_rating bubble_([0-9]{2})">' \
              r'</span>'
    re_quote = r'<span class=\'noQuotes\'>([^<]+)</span>'

    # ouverture du fichier contenant les pages qu'on souhaite aspirer
    fichier_liens = liens
    fichier_url = open(fichier_liens, mode='r', encoding='UTF-8')
    lien_page = fichier_url.readlines()
    # print(lien_page)
    fichier_url.close()
    # début de l'aspiraaageeeeee
    fichier_sortie = open("sortie_liens.csv", mode="w")
    csv_writer = csv.writer(fichier_sortie, quoting=csv.QUOTE_ALL)
    for i in range(len(lien_page)):
        url = lien_page[i]
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        page = response.read().decode('UTF-8')
        res_regex_note = re.findall(re_note, page)
        res_regex_comm = re.findall(re_commentaire, page)
        res_regex_quote = re.findall(re_quote, page)
        if len(res_regex_comm) == len(res_regex_note):
            for j in range(len(res_regex_note)):
                csv_writer.writerow([res_regex_note[j], html.unescape(res_regex_quote[j]),
                                     html.unescape(res_regex_comm[j])])
        else:
            print("les résultats des regex ne sont pas identiques")
        time.sleep(3)
    fichier_sortie.close()


if __name__ == '__main__':
    crawler("lien_tripadvisor.txt")

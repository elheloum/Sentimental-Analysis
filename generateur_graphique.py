#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 2 17:39:13 2019

@author: myriamelhelou
"""

import matplotlib.pyplot as plt


def graph():

    plt.plot(['unigram', 'unigram_SMO', 'bigram', 'bigram_SMO', 'trigram', 'trigram_SMO'],
             [0.90, 0.88, 0.85, 0.84, 0.82, 0.76], 'r+')
    plt.xlabel('Modèle d\'apprentissage')
    plt.ylabel('Précision')
    plt.title('Results for SVC(kernel=rbf)')
    plt.show()


if __name__ == '__main__':
    graph()
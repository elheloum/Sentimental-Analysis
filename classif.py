#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:05:42 2018

@author: myriamelhelou & juliecoletti

this script is inspired by Marco Bonzanini's tutorial : https://marcobonzanini.com/2015/01/19/sentiment-analysis-with-python-and-scikit-learn/
"""
import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report


def usage():
    print("Usage:")
    print("python %s <data_dir>" % sys.argv[0])


if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    data_dir = sys.argv[1]
    classes = ['pos', 'neg']

    # Read the data
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    for curr_class in classes:
        dirname = os.path.join(data_dir, curr_class)
        for fname in [x for x in os.listdir(dirname) if x.endswith(".txt")]:
            with open(os.path.join(dirname, fname), 'r') as f:
                content = f.read()
                if fname.startswith('cv9'):
                    test_data.append(content)
                    test_labels.append(curr_class)
                else:
                    train_data.append(content)
                    train_labels.append(curr_class)

    # Create feature vectors
    # min_df=5, discard words appearing in less than 5 documents
    # max_df=0.8, discard words appering in more than 80% of the documents
    # sublinear_tf=True, use sublinear weighting
    # use_idf=True, enable IDF
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df=0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    #  fit_transform() will create the vocabulary (i.e. the list of words/features) and the feature weights from the training data
    train_vectors = vectorizer.fit_transform(train_data)
    # transform(will create the feature weights for the test data, using the same vocabulary as the training data.
    test_vectors = vectorizer.transform(test_data)

    # Perform classification with SVM, kernel=rbf
    classifier_rbf = svm.SVC()
    t0 = time.time()
    # The fit() method will perform the training and it requires the training data processed by the vectorizer as well as the correct class labels.
    classifier_rbf.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_rbf = classifier_rbf.predict(test_vectors)
    t2 = time.time()
    time_rbf_train = t1-t0
    time_rbf_predict = t2-t1

    # Perform classification with SVM, kernel=linear
    classifier_linear = svm.SVC(kernel='linear')
    t0 = time.time()
    classifier_linear.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_linear = classifier_linear.predict(test_vectors)
    t2 = time.time()
    time_linear_train = t1-t0
    time_linear_predict = t2-t1

    # Perform classification with SVM, kernel=linear
    classifier_liblinear = svm.LinearSVC()
    t0 = time.time()
    classifier_liblinear.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_liblinear = classifier_liblinear.predict(test_vectors)
    t2 = time.time()
    time_liblinear_train = t1-t0
    time_liblinear_predict = t2-t1

    # Print results in a nice table
    print("Results for SVC(kernel=rbf)")
    print("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
    print(classification_report(test_labels, prediction_rbf))
    print("Results for SVC(kernel=linear)")
    print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
    print(classification_report(test_labels, prediction_linear))
    print("Results for LinearSVC()")
    print("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
    print(classification_report(test_labels, prediction_liblinear))

    # création fichiers log enregistrant les résultats des différentz algorithmes d'apprentissage machine

    filename = "test{0}".format(sys.argv[1])
    fichier_log = open(filename+".log", mode='w', encoding='UTF-8')
    fichier_log.write("Les résultats pour le dossier {0}".format(sys.argv[1]))
    fichier_log.write("\n")
    fichier_log.write("Results for SVC(kernel=rbf)")
    fichier_log.write("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
    fichier_log.write(classification_report(test_labels, prediction_rbf))
    fichier_log.write("Results for SVC(kernel=linear)")
    fichier_log.write("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
    fichier_log.write(classification_report(test_labels, prediction_linear))
    fichier_log.write("Results for LinearSVC()")
    fichier_log.write("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
    fichier_log.write(classification_report(test_labels, prediction_liblinear))
    fichier_log.close()

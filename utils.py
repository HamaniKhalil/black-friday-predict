# -*- coding: UTF-8 -*-
#!/anaconda3/bin/python

from time import time
from statistics import mean

# Mesures
from sklearn.metrics import average_precision_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, precision_recall_fscore_support

def train_model(clf, X_train, y_train):
    time_consumption = time()
    clf.fit(X_train, y_train)

    # Time formating to hours, minutes and seconds
    time_consumption = time() - time_consumption
    hours = int(time_consumption / 3600)
    minutes = int((time_consumption - int(hours * 3600)) / 60)
    seconds = time_consumption - minutes * 60 - hours * 360

    print("Model entrainé en : %02d:%02d:%02d" % (hours, minutes, seconds))

    return clf


def show_performances(clf, X_test, y_test):
    time_consumption = time()
    predictions = clf.predict(X_test)

    # Time formating to hours, minutes and seconds
    time_consumption = time() - time_consumption
    hours = int(time_consumption / 3600)
    minutes = int((time_consumption - int(hours * 3600)) / 60)
    seconds = time_consumption - minutes * 60 - hours * 360

    print("Prédictions faites en  : %02dh%02dm%02ds" % (hours, minutes, seconds))

    accuracy = accuracy_score(y_test, predictions)
    print ("accuracy: {:.2%}.\n".format(accuracy))

    precision, recall, fscore, support = precision_recall_fscore_support(y_test, predictions)

    print("precision: {}.\n".format(precision))
    print("recall: {}.\n".format(recall))

    print("precision moyenne: {}.\n".format(mean(precision)))
    print("recall moyen: {}.\n".format(mean(recall)))

    ones_in_precision = 0
    zeros_in_precision = 0

    for i in range(0, len(precision)):
        if precision[i] == 1.:
            ones_in_precision += 1

        if precision[i] == 0.:
            zeros_in_precision += 1

    ones_in_recall = 0
    zeros_in_recall = 0

    for i in range(0, len(precision)):
        if precision[i] == 1.:
            ones_in_recall += 1

        if precision[i] == 0.:
            zeros_in_recall += 1

    print("1. in precision : ", ones_in_precision)
    print("0. in precision : ", zeros_in_precision)
    print("1. in recall : ", ones_in_recall)
    print("0. in recall : ", zeros_in_recall)
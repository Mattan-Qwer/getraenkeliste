#!/usr/bin/env python3
#import

import os
import codecs
import sys
import signal #Fenstergroessenaenderung
import csv
import collections

if sys.version_info <(3, 4):
        safe_input = raw_input
elif sys.version_info >=(3, 4):
        safe_input = input

#Farbdefinition
class Farben(object):
    GruenBg ='\033[42m'
    Gruen = '\033[32m'
    HEVORHEBEN = '\033[4m'
    ROT ='\033[31m'
    RESET = '\033[0m'


def more_decimals_than(number, allowed_decimals_cnt):
    """
    returns true if the count of decimals (numbers after the dot) is more than decimals
    """
    # e.g. 5.67 - 5 = 0.67 -> '67' (round: because float is bitter)
    decimals = str(round(number-int(number), allowed_decimals_cnt+1))[2:]
    cnt = 0 if decimals == '0' else len(decimals)
    return False if cnt < 0 else cnt > allowed_decimals_cnt

#Farbdefinition
class Farben(object):
	GruenBg ='\033[42m'
	Gruen = '\033[32m'
	HEVORHEBEN = '\033[4m'
	ROT ='\033[31m'
	RESET = '\033[0m'


def colorize(color, message):
    """
    Adds ANSI colors to the message
    :type color: str
    :type message: str
    :param color: Colors to add to the message
    :param message: Message which should be displayed colored
    :return: the colored message
    """
    return "%s%s%s" % (color, message, Farben.RESET)


def float_input(promt, default, decimals=0):
    input_text =""
    while True:
                try:
                    input_text =str(safe_input("{promt} [{default}]".
                       format(promt=promt,default=default)))
                    if(len(input_text)) == 0:
                        return default
                        #TODO: elif Float aber zu viel Nachkomma
                    elif more_decimals_than(float(input_text), decimals):
                        print(more_decimals_than(float(input_text), decimals))
                        print(colorize(Farben.ROT,
                        "You must enter a number with at most %d decimals" % decimals))
                        continue
                    else:
                        return float(input_text)
                except ValueError:
                    print(colorize(Farben.ROT, "EUROBETRAG EINGEBEN. Versuche es nochmal"))

def bestaetigung_input(text):
    input_text=""
    while True:
        print(text)
        input_text = str(safe_input())
        if input_text.strip().capitalize() =='Y':
            return True
        elif input_text.strip().capitalize() == 'N':
            return False
        else:
            print('Eingabe nicht erkannt')


def zeilen_abfrage(name):
    while True:
        # row['Name']
        if len(name) ==0:
            print('Wie heist der neue Benutzer?')
            v_name =str(safe_input())
        else:
            v_name = str(name)
        print(v_name)
        # row[ 'Eingezahlt']
        v_eingezahlt = float(row['Eingezahlt']) + float_input("Einzahlung:",0.0,2)
        print( str(v_eingezahlt -float(row['Eingezahlt'])))

        # row['#50ct']
        kosten_50ct = float_input("#50ct",0.0,0)
        print('#50ct: '+str(kosten_50ct))
        v_50ct = float(row['#50ct']) + kosten_50ct
        #row[ '#70ct']
        kosten_70ct = float_input("#70ct",0.0,0)
        print('#70ct: '+str(kosten_70ct))
        v_70ct = float(row['#70ct'])+kosten_70ct

        #row[ '#100ct']
        kosten_100ct = float_input("#100ct",0.0,0)
        print('#100ct: '+str(kosten_100ct))
        v_100ct = float(row['#100ct'])+kosten_100ct


        if bestaetigung_input('Ist die Eingabe richtig? [y/n]'):
            return {'Name' : v_name, 'Eingezahlt' : str(v_eingezahlt),'#50ct' : str(v_50ct), '#70ct' : str(v_70ct), '#100ct' : str(v_100ct)}






#####Programm start

#CSV-Update
#Input DB
readDB = open('mitglieder_db.csv')
csvreader = csv.DictReader(readDB)

#fieldnames = ['Name','Eingezahlt','#50ct','#70ct','#100ct']
fieldnames = csvreader.fieldnames
#print(fieldnames)


#Output DB
writeDB =  open("auto_mitglieder_db.csv",'a')
csvwriter = csv.DictWriter(writeDB,fieldnames=fieldnames)

#LaTex-Datei erstellen
#Input
filename_Input = str("getraenkeliste_vorlage.tex")
lines = codecs.open(filename_Input, 'r', encoding='utf-8').readlines()

#Output
filename_Output = str("getraenkeliste.tex")
lines = codecs.open(filename_Output, 'w+', encoding='utf-8')
csvwriter.writeheader()
for row in csvreader:
    #Schreiben der CSV-Zeile
    csvwriter.writerow(zeilen_abfrage(row['Name']))

#TODO: Nutzer anlegen
if bestaetigung_input('Soll ein neuer Benutzer angelegt werden? [y/n]'):

    csvwriter.writerow(zeilen_abfrage(''))

writeDB.close()
readDB.close()


#TODO: Ausgabe schreiben






print("Geschafft")











#!/usr/bin/env python3
#import

import os
import codecs
import sys
import signal #Fenstergroessenaenderung
import csv
import shutil

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


def DBEinfuegen(dbname):
    insertstring =''
   #csv.open
    readDB = open(str(dbname))
    csvreader = csv.DictReader(readDB)
    gesges =0
    ges50 =0
    ges70 =0
    ges100 =0

    for row in csvreader:
        insertstring = str(row['Name'])+' &'
        ges = (float(row['Eingezahlt'])-0.5*float(row['#50ct'])-0.7*float(row['#70ct'])-1.0*float(row['#100ct']))
        gesges += ges
        if(ges >= 0.0):
            insertstring += str(ges)+' &'
        else:
            insertstring += str(ges)+' &' #TODO:colour <RED
        ges50 += float(row['#50ct'])
        ges70 += float(row['#70ct'])
        ges50 += float(row['#100ct'])

        insertstring += str(row['#50ct'])+' &'
        insertstring += str(row['#70ct'])+' &'
        insertstring += str(row['#100ct'])+' \\\hline'

    insertstring += str(ges50)+' &'
    insertstring += str(ges70)+' &'
    insertstring += str(ges100)+' \\\hline'
    return insertstring

#####Programm start

#CSV-Update
#Input DB
DBFile ='mitglieder_db.csv'
readDB = open(DBFile)
csvreader = csv.DictReader(readDB)

#fieldnames = ['Name','Eingezahlt','#50ct','#70ct','#100ct']
fieldnames = csvreader.fieldnames
#print(fieldnames)


#Output DB
DBFileTmp ="auto_mitglieder_db.csv"
writeDB =  open(DBFileTmp,'w')
csvwriter = csv.DictWriter(writeDB,fieldnames=fieldnames)

#Eintargungen in die DB
csvwriter.writeheader()
## Alte Benutzer
for row in csvreader:
    #Schreiben der CSV-Zeile
    csvwriter.writerow(zeilen_abfrage(row['Name']))


## Nutzer anlegen
if bestaetigung_input('Soll ein neuer Benutzer angelegt werden? [y/n]'):

    csvwriter.writerow(zeilen_abfrage(''))
#Dateien schließen
writeDB.close()
readDB.close()
#Dateien rueckschreiben
os.remove(DBFile)
shutil.copy(DBFileTmp, DBFile)
os.remove(DBFileTmp)


# Ausgabe schreiben

#LaTex-Datei erstellen
#Input
filename_Input = str("getraenkeliste_vorlage.tex")
lines = codecs.open(filename_Input, 'r', encoding='utf-8').readlines()

#Output
filename_Output = str("getraenkeliste.tex")
writer = codecs.open(filename_Output, 'w+', encoding='utf-8')

for line in lines:
    if(line=='%Hier kommen die Daten rein\n'):
        DBeinfuegen(DBFile)
    else:
        writer.write(line)



print("Geschafft")











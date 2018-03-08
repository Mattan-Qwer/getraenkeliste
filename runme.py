#!/usr/bin/env python3
#import

import os
import codecs
import sys
import signal #Fenstergroessenaenderung
import csv

if sys.version_info <(3, 4):
	safe_input = raw_input
elif sys.version_info >=(3, 4):
	safe_input = input

#CSV-Update
#Input DB
readDB =open("mitglieder_db.csv")
csvreader = csv.reader(readDB)

#Output DB
writeDB = open(file("auto_mitglieder_db.csv")
csvwriter = csv.writer(writeDB)

#LaTex-Datei erstellen
#Input
filename_Input = str("getraenkeliste_vorlage.tex")
lines = codecs.open(filename_Input, 'r', encoding='utf-8').readlines()

#Output
filename_Output = str("getraenkeliste.tex")
lines = codecs.open(filename_Output, 'w+', encoding='utf-8')

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


#####Programm start
for rowcounter, row in enumerate(csvreader):

	if rowcounter ==0:
		rowHead = row
		print(rowHead)
		csvwriter.writerow(rowHead)
	else:
		while True:
			rowNew = []
			lineNew=''
			for columnCounter in range(0, len(row)):
				if rowHead[columnCounter].strip() == 'Name':
					rowNew.append(row[columnCounter])
					print(colorize(Farben.Gruen, (rowNew[columnCounter])))
					lineNew += colorize(Farben.GruenBg ,rowHead[columnCounter].strip()+ ': '+ rowNew[columnCounter] )+ ' \n'

				elif rowHead[columnCounter].strip() == 'Eingezahlt':
					einzahlung = float_input("Einzahlung:",0.0,2)
					rowNew.append(str(float(row[columnCounter])+einzahlung))
					lineNew += rowHead[columnCounter].strip()+ ': '+ str(float(rowNew[columnCounter])-float(row[columnCounter])) + ' \n'

				elif rowHead[columnCounter].strip() == '#50ct':
					kosten_50ct = float_input("#50ct",0.0,0)
					rowNew.append(str(float(row[columnCounter])+kosten_50ct))
					lineNew += rowHead[columnCounter].strip()+ ': '+ str(float(rowNew[columnCounter])-float(row[columnCounter])) + ' \n'

				elif rowHead[columnCounter].strip() == '#70ct' :
					kosten_70ct = float_input("#70ct",0.0,0)
					rowNew.append(str(float(row[columnCounter])+kosten_70ct))
					lineNew += rowHead[columnCounter].strip()+ ': '+ str(float(rowNew[columnCounter])-float(row[columnCounter])) + ' \n'

				elif rowHead[columnCounter].strip() == '#100ct' :
					kosten_100ct = float_input("#100ct",0.0,0)
					rowNew.append(str(float(row[columnCounter])+kosten_100ct))
					lineNew += rowHead[columnCounter].strip()+ ': '+ str(float(rowNew[columnCounter])-float(row[columnCounter])) + ' \n'

			#print(lineNew)
			if bestaetigung_input('Ist die Eingabe richtig? [y/n]'):
				break


		csvwriter.writerow(rowNew)

#TODO: Nutzer anlegen
	writeDB.close()
	readDB.close()
	#

#TODO: Ausgabe schreiben






print("Geschafft")











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
csvreader = csv.reader(file("mitglieder_db.csv"))

#Output DB
csvwriter = csv.writer(file("some.csv", "w"))

#LaTex-Datei erstellen
#Input
filename_Input = str("getraenkeliste_vorlage.tex")
lines = codecs.open(filename_Input, 'r', encoding='utf-8').readlines()

#Output
filename_Output = str("getraenkeliste.tex")
lines = codecs.open(filename_Output, 'w+', encoding='utf-8')

#Farbdefinition
class Farben(object):

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



#####Programm start
linecounter =0
for dbline in dblines:
	linecounter += 1
	if linecounter>1:
		print(dbline[0:dbline.index(",")].strip())
		print(dbline[0:dbline.index(",")].strip())
		einzahlung = float_input("Einzahlung:",0.0,2)
		print("%d" %einzahlung)


	else:
		outFile.write(dbline)

#TODO: Ausgabe schreiben




#TODO: Nutzer anlegen


print("EoF")











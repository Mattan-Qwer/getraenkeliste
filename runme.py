#!/usr/bin/env python3
#import

import os
import codecs
import sys
import signal #Fenstergroessenaenderung

if sys.version_info <(3, 4):
	safe_input = raw_input
elif sys.version_info >=(3, 4):
	safe_input = input

#CSV-Update
#Input DB
dbname = str("mitglieder_db.csv")
dblines = codecs.open(dbname, 'r', encoding='utf-8').readlines()

#Output DB
outputDb = str("auto_mitglieder_db.csv")
outFile = codecs.open(outputDb, 'w+' , encoding='utf-8')

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

def float_input(promt, default, decimals=0):
	input_text =""
	while True:
		try:
			input_text =str_input(safe_input("{promt} [{default}]".
				format(promt=promt,default=default)))
		 	if(len(input_text)) == 0:
				return default
				#TODO: elif Float aber zu viel Nachkomma
			else:
				return float(input_text)
		except ValueError:
			print(colorize(Farbe.ROT, "EUROBETRAG EINGEBEN. Versuche es nochmal"))



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











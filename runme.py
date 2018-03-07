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
dblines = codecs.open(filename, 'r', encoding='utf-8').readlines()

#Output DB
outputDb = str("auto_mitglieder_db.csv")
outFile = codecs.open(outputDb, 'w+' , encoding='utf-8')

#LaTex-Datei erstellen
#Input
filename = str("getraenkeliste_vorlage.tex")
lines = codecs.open(filename, 'r', encoding='utf-8').readlines()

#Output
filename = str("getraenkeliste.tex")
lines = codecs.open(filename. 'w+', encoding='utf-8')

#Farbdefinition
class Farben(object):

	HEVORHEBEN = '\033[4m'

def float_imput(promt, default, decimals=0):
	input_text =""
	while True:
		try:
			input_text =str_input("{promt} [{default}]".format(promt=promt,default =default))
#TODO: -Input ordentlich machen



#####Programm start
for dbline in dblines:
	print(dbline[0:dbline.index(",")].strip())
	einzahlung = float_input("Einzahlung:"),0.0,2)

#TODO: Ausgabe schreiben

#TODO: Nutzer anlegen


print(colorized(Farbe.











#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import subprocess
import os, sys
reload(sys)
sys.setdefaultencoding('utf8')

class analizador():

	def __init__(self):
		self.words = []
		self.words_morfo = []
		self.words_stemm = []
		self.words_lema = []

	def split(self, strings):
		self.words = strings.split()
		print(self.words)
		return self.words

	def lema(self, strings):
		process = subprocess.Popen('echo '+strings+' | analyze -f es.cfg', shell=True, stdout=subprocess.PIPE)

		for line in iter(process.stdout.readline,''):
			if(len(line) > 2):
				words_lema_temp = line.split()[1]
				self.words_lema.append(words_lema_temp)

		print(self.words_lema)
		return self.words_lema

	def morfo(self, strings):
		process = subprocess.Popen('echo '+strings+' | analyze -f esm.cfg', shell=True, stdout=subprocess.PIPE)

		self.words_morfo = []

		for line in iter(process.stdout.readline,''):
			word_morfo_temp = line.split()[1:]
			word_morfo = []

			while len(word_morfo_temp) != 0:
				word_morfo.append(word_morfo_temp[:3])
				del word_morfo_temp[0:3]
			
			if(len(word_morfo) != 0):
				self.words_morfo.append(word_morfo)

		print(self.words_morfo)
		return self.words_morfo

	def stemm(self, strings_split):
		for string in strings_split:
			string_temp = subprocess.check_output('php stemm_es.php '+ string, shell=True)
			if len(string_temp) != 0:
				self.words_stemm.append(string_temp[:-2])
		print(self.words_stemm)
		return self.words_stemm

	def run(self, strings):
		self.split(strings)
		self.morfo(strings)
		self.lema(strings)
		self.stemm(self.words)
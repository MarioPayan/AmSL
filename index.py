#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from flask import Flask, request, render_template
from flask import render_template
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from analizador import analizador
app = Flask("AmSL")
@app.route('/')
def set():
	return render_template('index.html',text="")

@app.route('/', methods=['POST'])
def get():
	text=str(request.form['inte'])
	if(text!=""):
		arbol =	analizar(text)
		words = arbol[0]
		lemas = arbol[2]
		stemms = arbol[3]
		morfos = arbol[1]
		return render_template('index.html', text=text, words=words, lemas=lemas, stemms=stemms, morfos=morfos)
	else:
		return render_template('index.html')

def analizar(strings):
	analyze = analizador()
	analyze.run(strings)

	analyze_text1 = analyze.words
	analyze_text2 = analyze.words_morfo
	analyze_text3 = analyze.words_lema
	analyze_text4 = analyze.words_stemm

	return [analyze_text1,analyze_text2,analyze_text3,analyze_text4]

if __name__ == '__main__':
	app.run()
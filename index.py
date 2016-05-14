from flask import Flask, request, render_template
from flask import render_template
import os
from analizador import analizador
app = Flask("AmSL")
@app.route('/')
def cargar():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def obtener():
	texto=str(request.form['id_entrada'])
	arbol =	analizar(texto)
	words = arbol[0]
	lemas = arbol[2]
	stemms = arbol[3]
	morfos = arbol[1]
	return render_template('index.html', texto=texto, words=words, lemas=lemas, stemms=stemms, morfos=morfos)
	#return render_template('index.html')

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
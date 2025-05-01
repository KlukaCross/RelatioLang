# see https://tomassetti.me/antlr-mega-tutorial/#chapter11 and https://www.antlr.org/

build-python:
	antlr4 -Dlanguage=Python3 RelatioLangLexer.g4 RelatioLangParser.g4

ast:
	antlr4-parse RelatioLangLexer.g4 RelatioLangParser.g4 parse -gui

clean-python:
	rm *.py

clean-antlr4:
	rm *.tokens *.interp

run-python:
	python main.py

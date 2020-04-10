#!/usr/bin/python3
# -*- coding:utf-8 -*-
from tempfile import mkstemp
from os import close
from shutil import move

def remove_dubl(file):
	count = 0
	ft, temp = mkstemp() # создать temp-файл
	lines = [] # уникальные строки из file
	with open(temp, 'w', encoding='utf-8') as t, open(file, encoding='utf-8') as f:
		for line in f: # читать file построчно
			print(line)
			if line not in lines: # для line, отсутствующих в lines
				lines.append(line) # сохранить line в lines
				t.write(line) # записать line в temp-файл
	close(ft) # закрыть temp-файл
	move(temp, file) # переместить/переименовать temp-файл в file

remove_dubl('Шпуленко.txt')
#!/usr/bin/python3
# -*- coding:utf-8 -*-
from tempfile import mkstemp
from os import close
from shutil import move
import requests


def remove_dubl(file):
	i = 0
	ft, temp = mkstemp() # создать temp-файл
	lines = [] # уникальные строки из file
	original = []
	with open(temp, 'w', encoding='utf-8') as t, open(file, encoding='utf-8') as f:
		for line in f: # читать file построчно
			try:
				response = requests.get(line)
			except:
				continue
			print(response)
			if response.content not in original:
				original.append(response.content)
				lines.append(line)
				t.write(line)
				i += 1
				print(i)
			else:
				print('duplicate')
	close(ft) # закрыть temp-файл
	move(temp, file) # переместить/переименовать temp-файл в file

remove_dubl('../photo_link.txt')
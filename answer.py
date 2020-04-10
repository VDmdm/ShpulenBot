import random
import requests


def answer_text(lst_text):
	nbr = random.randint(0, len(lst_text))
	return lst_text[nbr]


def answer_photo(lst_photo):
	nbr = random.randint(0, len(lst_photo))
	photo = requests.get(lst_photo[nbr])
	if photo.content:
		return photo.content
	else:
		return answer_photo(lst_photo)

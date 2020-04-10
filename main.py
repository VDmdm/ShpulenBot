import telebot
import lst_filler
import answer
from telebot import types

bot = telebot.TeleBot('1281526127:AAFHktwX9c3jQo6I8F5Fmo9kLySB2V1Bpuc')
GROUP_ID = -100029590

@bot.message_handler(commands=['start'])
def start_massage(message):
	keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	keyboard.row('О, великая богиня, дай мне мудрость!')
	bot.send_message(message.chat.id, 'Привет , пишите мне только по делу . Я занятая бизнес-леди .', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text == 'О, великая богиня, дай мне мудрость!':
		bot.send_message(message.chat.id, answer.answer_text(lst_text))
		bot.send_photo(message.chat.id, answer.answer_photo(lst_photo))
	else:
		bot.send_message(message.chat.id, 'Пиши мне по делу , бесплатные консультации не даю!')


@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text == 'О, великая богиня, дай мне мудрость!':
		bot.send_message(message.chat.id, answer.answer_text(lst_text))
		bot.send_photo(message.chat.id, answer.answer_photo(lst_photo))


lst_text = []
lst_photo = []
lst_filler.lst_fill_text(lst_text)
lst_filler.lst_fill_photo(lst_photo)
bot.polling()
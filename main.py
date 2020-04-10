import telebot
import lst_filler
import answer
import apiai, json
from telebot import types

bot = telebot.TeleBot('1274591655:AAEGkkUEUPemTn4Pyl12r2OggtJEJRWtrkw')
GROUP_ID = -100029590

@bot.message_handler(commands=['start'])
def start_massage(message):
	keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	keyboard.row('О, великая богиня, дай мне мудрость!')
	keyboard.row('Богиня, можно бесплатную консультацию?')
	bot.send_message(message.chat.id, 'Привет , пишите мне только по делу . Я занятая бизнес-леди .', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_answer(message):

	if message.text == 'О, великая богиня, дай мне мудрость!':
		bot.send_message(message.chat.id, answer.answer_text(lst_text))
		bot.send_photo(message.chat.id, answer.answer_photo(lst_photo))

	elif message.text == 'Богиня, можно бесплатную консультацию?':
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		keyboard.row('Ну пожалуйста, богиня, я мужчина!')
		bot.send_message(message.chat.id, 'Бесплатных консультаций не даю', reply_markup=keyboard)

	elif message.text == 'Ну пожалуйста, богиня, я мужчина!':
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		keyboard.row('Богиня, спасибо за консультацию!')
		msg = bot.reply_to(message, 'Ах , мужчина... Ну хорошо , я сделаю исключение ! Рассказывайте как дела...', reply_markup=keyboard)
		bot.register_next_step_handler(msg, answer_small_talk)

	elif message.chat.type == 'private':
		bot.send_message(message.chat.id, 'Пиши мне по делу , бесплатные консультации не даю!')

def answer_small_talk(message):

	if message.text == 'Богиня, спасибо за консультацию!':
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		keyboard.row('О, великая богиня, дай мне мудрость!')
		keyboard.row('Богиня, можно бесплатную консультацию?')
		bot.send_message(message.chat.id, 'Всего доброго ! Отзыв можно оставить в группе вк .', reply_markup=keyboard)
		exit()
		print('1')

	print('2')
	request = apiai.ApiAI('f7e6460c45cb4ab0bce37f676e320792').text_request()  # Токен API к Dialogflow
	request.lang = 'ru'  # На каком языке будет послан запрос
	request.session_id = 'Spulenbot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
	request.query = message.text  # Посылаем запрос к ИИ с сообщением от юзера
	response_json = json.loads(request.getresponse().read().decode('utf-8'))
	response = response_json['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
	# Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
	if response:
		msg = bot.reply_to(message, response)
		bot.register_next_step_handler(msg, answer_small_talk)
	else:
		msg = bot.reply_to(message, 'Я Вас не совсем поняла ! Что за мужчины пошли ! Пишите по делу или в чс !')
		bot.register_next_step_handler(msg, answer_small_talk)


lst_text = []
lst_photo = []
lst_filler.lst_fill_text(lst_text)
lst_filler.lst_fill_photo(lst_photo)
bot.polling()
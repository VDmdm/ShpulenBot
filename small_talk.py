import apiai, json
import telebot

elif message.text == 'Ну пожалуйста, богиня, я мужчина!':
	keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	keyboard.row('Богиня, спасибо за консультацию!')
	request = apiai.ApiAI('f7e6460c45cb4ab0bce37f676e320792').text_request()  # Токен API к Dialogflow
	request.lang = 'ru'  # На каком языке будет послан запрос
	request.session_id = 'Spulenbot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
	request.query = message.text  # Посылаем запрос к ИИ с сообщением от юзера
	response_json = json.loads(request.getresponse().read().decode('utf-8'))
	response = response_json['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
	# Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
	if response:
		bot.send_message(message.chat.id, response, reply_markup=keyboard)
	else:
		bot.send_message(message.chat.id, 'Я Вас не совсем поняла ! Что за мужчины пошли ! Пишите по делу или в чс !',
	                 reply_markup=keyboard)
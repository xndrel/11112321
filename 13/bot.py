import telebot
from telebot import types
import os
from botek import send_video_description, find_video_path

bot = telebot.TeleBot('7095549792:AAFqExmSpSVjBUmjZOLswciPuE7YZbwpG-U')

user_actions = {}
used_features = set()

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    photo = open('photo/WELCOMEE.jpg', 'rb')
    
    
    keyboard = types.InlineKeyboardMarkup()
    menu = types.InlineKeyboardButton("меню", callback_data='menu')
    keyboard.row(menu)

    bot.send_photo(message.chat.id, photo, caption="Привет, {0.first_name}!\n\nЯ бот созданный помочь тебя научить турнирным фишкам Dead by Daylight.".format(message.from_user),reply_markup=keyboard)

    user_actions[chat_id] = 'welcome'

    photo.close()
    bot.delete_message(message.chat.id, message.message_id)

used_features = set()

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    if call.data in used_features:
        bot.answer_callback_query(call.id, text="Эта фишка уже была выбрана.")
    elif call.data in ['jump_to_pallet', 'invisible_stun', 'texture_abuse', 'crouch_tech', 'snowball_protection', 'for_the_people', 'bloodlust_reset', 'agility_bite', 'cabinet_stand', 'back_flip', 'ability_block', 'solo_escape', 'timing_adrenaline', 'corrupt_evade', 'terror_running', 'proper_reset', 'corner_fall', 'obsession_transfer', 'high_ground_abuse', 'ability_reset', 'koli_timing', 'clown_abuse', 'high_ground', 'texture_slizing']:
        bot.answer_callback_query(call.id, text="Загружаем обучение, пожалуйста, подождите...")
        video_filename = call.data + ".mp4"  
        video_path = find_video_path(video_filename)
        if video_path:
            video = open(video_path, 'rb')
            bot.send_video(call.message.chat.id, video)
            video.close()
            send_video_description(bot, chat_id, call.data)
            used_features.add(call.data)  
            update_features_keyboard(call.message)  
        else:
            bot.send_message(call.message.chat.id, "Извините, не удалось загрузить обучение.\n\nВозможная ошибка an_cb_q.\n\nОбратитесь в поддержку для решение данной проблемы")
    elif call.data == 'menu':
        photo = open('photo/MENU.jpg', 'rb')
        keyboard = create_main_menu_keyboard()  
        bot.send_photo(call.message.chat.id, photo, caption="Выберите раздел:", reply_markup=keyboard) 

        user_actions[chat_id] = 'menu'

        photo.close() 
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'features':
        keyboard = create_features_keyboard()
        photo = open('photo/FISHKAA.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo, caption="Выберите интересующую фишку:", reply_markup=keyboard)
        
        user_actions[chat_id] = 'features'
        
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'support':
        keyboard = create_support_keyboard()
        support_photo = open('photo/SUPPORT.jpg', 'rb')
        bot.send_photo(call.message.chat.id, support_photo, caption="По поводу бота писать - @xndre1",reply_markup=keyboard)
        
        user_actions[chat_id] = 'support'

        support_photo.close()
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'back':
        previous_action = user_actions.get(chat_id)
        if previous_action == 'menu':
            welcome(call.message)

            bot.delete_message(call.message.chat.id, call.message.message_id)

        elif previous_action == 'features':
            keyboard = create_main_menu_keyboard()
            bot.send_photo(call.message.chat.id, open('photo/MENU.jpg', 'rb'), caption="Выберите раздел:", reply_markup=keyboard)

            bot.delete_message(call.message.chat.id, call.message.message_id)

        elif previous_action == 'support':
            photo = open('photo/MENU.jpg', 'rb')
            keyboard = create_main_menu_keyboard()  
            bot.send_photo(call.message.chat.id, photo, caption="Выберите раздел:", reply_markup=keyboard) 

            bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data in ['texture_slizing', 'jump_to_pallet', 'invisible_stun', 'texture_abuse', 'crouch_tech', 'snowball_protection', 'for_the_people', 'bloodlust_reset', 'agility_bite', 'cabinet_stand', 'back_flip', 'ability_block', 'solo_escape', 'timing_adrenaline', 'corrupt_evade', 'terror_running', 'proper_reset', 'corner_fall', 'obsession_transfer', 'high_ground_abuse', 'ability_reset', 'koli_timing', 'clown_abuse', 'high_ground']:
        video = open('video/' + call.data + '.mp4', 'rb')
        bot.send_video(call.message.chat.id, video)

    else:
        bot.send_message(call.message.chat.id, "Извините, Видео по данной фишке не найдено.\n\nВозможноая ошибка cb_hl.\n\nНапишите в поддержку о данной проблеме и мы в скором времени её решим.")





def create_main_menu_keyboard():
    markup = types.InlineKeyboardMarkup()
    
    features_button = types.InlineKeyboardButton("Фишки", callback_data='features')
    support_button = types.InlineKeyboardButton("Поддержка", callback_data='support')
    back_button = types.InlineKeyboardButton("Назад", callback_data='back')
    
    markup.row(features_button)
    markup.row(support_button)
    markup.row(back_button)
    
    return markup

def create_features_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(types.InlineKeyboardButton("Облизывание текстур", callback_data='texture_slizing'))
    markup.add(types.InlineKeyboardButton("Байт прыжок в паллету", callback_data='jump_to_pallet'))
    markup.add(types.InlineKeyboardButton("Невидимый стан", callback_data='invisible_stun')) 
    markup.add(types.InlineKeyboardButton("Абуз 3 текстурки", callback_data='texture_abuse')) 
    markup.add(types.InlineKeyboardButton("Крауч тек", callback_data='crouch_tech')) 
    markup.add(types.InlineKeyboardButton("Защита от сноубола", callback_data='snowball_protection'))
    markup.add(types.InlineKeyboardButton("Ради Людей/FTP", callback_data='for_the_people')) 
    markup.add(types.InlineKeyboardButton("Сброс bloodlust", callback_data='bloodlust_reset')) 
    markup.add(types.InlineKeyboardButton("Байт гибскость", callback_data='agility_bite')) 
    markup.add(types.InlineKeyboardButton("шкафстан", callback_data='cabinet_stand')) 
    markup.add(types.InlineKeyboardButton("Обратный прыжок", callback_data='back_flip')) 
    markup.add(types.InlineKeyboardButton("Блокирование абилки", callback_data='ability_block')) 
    markup.add(types.InlineKeyboardButton("100% побег в соло", callback_data='solo_escape')) 
    markup.add(types.InlineKeyboardButton("Адреналин по таймингу", callback_data='timing_adrenaline')) 
    markup.add(types.InlineKeyboardButton("Отвод на коррапт", callback_data='corrupt_evade')) 
    markup.add(types.InlineKeyboardButton("Бегать по террору", callback_data='terror_running')) 
    markup.add(types.InlineKeyboardButton("Правильный Ресет", callback_data='proper_reset')) 
    markup.add(types.InlineKeyboardButton("Падение в угол", callback_data='corner_fall')) 
    markup.add(types.InlineKeyboardButton("Переброс обсешна", callback_data='obsession_transfer')) 
    markup.add(types.InlineKeyboardButton("Абуз хайграунда от Вескера", callback_data='high_ground_abuse')) 
    markup.add(types.InlineKeyboardButton("Сброс абилки они", callback_data='ability_reset')) 
    markup.add(types.InlineKeyboardButton("Правильный тайминг от Коли", callback_data='koli_timing'))
    markup.add(types.InlineKeyboardButton("Бессоница против Клоуна", callback_data='clown_abuse'))
    markup.add(types.InlineKeyboardButton("Спрыжка с хг без стана", callback_data='high_ground'))

    back_button = types.InlineKeyboardButton("Назад", callback_data='back')
    markup.row(back_button)

    return markup

def update_features_keyboard(message):
    markup = create_features_keyboard()  
    features_to_remove = list(used_features)  
    for feature in features_to_remove:
        markup.keyboard = [[button for button in row if button.text != feature.replace('_', ' ').title()] for row in markup.keyboard]  
    bot.edit_message_reply_markup(message.chat.id, message.message_id, reply_markup=markup) 

def create_support_keyboard():
    markup = types.InlineKeyboardMarkup()
    
    back_button = types.InlineKeyboardButton("Назад", callback_data='back')
    markup.add(back_button)
    
    return markup
    
bot.polling(none_stop=True)

            

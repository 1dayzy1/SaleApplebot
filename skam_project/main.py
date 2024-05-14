import telebot
from telebot import types
from random import randint
from datetime import datetime


bot = telebot.TeleBot(ТОКЕН)


apples = {}
application = {}
previous = None
admin_id = [5919133090]
my_id = 5919133090
ran = randint(3499,9999)
app = {}
order_status = {}
all_users = []
start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
activ = {}
My_prof = {}
fedd = None



#Обработчик команды Start
@bot.message_handler(commands=['start'])
def start(message):
    start_date
    global all_users
    logo_iTime = open('logo_skam.jpg','rb')
    usernam =  message.from_user.username
    userid = message.from_user.id
    with open('users.txt', 'a') as file:
        file.write(f"{message.chat.id}\n")
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    btn1 = types.KeyboardButton('🛒Оформить заказ')
    btn2 = types.KeyboardButton('⭐Отзывы')
    btn3 = types.KeyboardButton('👨🏻‍💻Админ-панель')
    btn4 = types.KeyboardButton('🍏🕰iTime')
    btn5 = types.KeyboardButton('🎁Пригласить друга')
    btn6 = types.KeyboardButton('💻Личный кабинет')
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
    bot.send_photo(message.chat.id,logo_iTime)
    bot.send_message(message.chat.id,f'Приветствую тебя {message.from_user.username}!\n🌟 Добро пожаловать в магазин умных часов 🍏🕰iTime! 🕒✨\nЗдесь вы найдете лучшие модели часов, сочетающие в себе стиль и инновационные технологии. 💫',reply_markup=markup)
    if usernam not in all_users:
        all_users.append('@'+ usernam)
    


#Создание рассылки всем пользователям
@bot.message_handler(func=lambda message: message.text and message.text.startswith('/send_to_all'))
def send_to_all(message):
    with open('users.txt', 'r') as file:
        users = file.readlines()
        for i in users:
            try:
                bot.send_message(i.strip(), message.text[13:])  # Отправка сообщения всем пользователям из списка
            except Exception as e:
                print(f"Failed to send message to user {i.strip()}: {str(e)}")




#Проверка команд пользователя
@bot.message_handler(content_types=['text'])
def proverka(message):
    image_watch = open('iTime.jpg','rb')
    #user = message.from_user.last_name
    global My_prof
    global all_users
    global order_status
    global app
    global ran
    global previous
    global apples
    global my_id
    global fedd
    users_list = '\n'.join(all_users)
    text_invite = ('🌟 Присоединяйтесь к нашей команде iTime🍏🕰\n\n📱 У нас вы найдете:\n\n✨ Последние новости из мира гаджетов.\n\n✨ Советы и рекомендации по использованию наших часов.\n\n✨ Эксклюзивные акции и скидки на технику.\n\n🔥 Не пропустите возможность быть в курсе всех трендов!\n\n📡 Присоединяйтесь к нам прямо сейчас, просто нажмите на кнопку ниже! 🎉📲\n\n👇 Перейти в наш Telegram канал 👇\n\niTime Apple watch shop - https://t.me/iTimeAppleWatch')
    text_watch = ('Для того что бы оформить заявку на покупку часов нам от вас потребуется\n\n1.Ваше ФИО(Фамилия Имя Отчество).\n2.Адресс по которому будет отправлена поссылка.\n\nВо избежание обмана с обеих сторон мы работаем по предоплате.\nЧуть ниже будут данные куда необоходимо перевести предоплату.\nПредоплата всегда составляет 800р.\nПример как должна выглядеть заявка\n\n1.Иванов Иван Иванович\n2.Г.Псокв ул.Вернадского\n3.Ваши контактные данные для того чтоб наш администратор связался с вами и подтвердил заказ\n4.Скинуть скриншот администратору в личные сообщения.\n\nКогда заявка заполнена отправляете ее боту после чего  нажимаете кнопку Да и бот ее отправляет администратору  и ваш заказ начинает обрабатываться.\n\nРекзвизиты для перевода предоплаты - 2200 7008 7034 7928 \n\nЕсли у вас останутся вопросы вы всегда можете обратиться к нашему администратору - @iTimeShop')
    #Оформление заказа
    if message.text == '🛒Оформить заказ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('😁Я выбрал')
        btn2 = types.KeyboardButton('🔙Назад')
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,'Здесь вы можете посмотреть какие товары в наличии🍏🕰',reply_markup=markup)
        bot.send_message(message.chat.id,'⌚Apple watch series 5\nГод выпуска:2019 Год\nЦена:2499\nВ наличии:✅\n\n⌚Apple watch SE(1-ое поколение)\nГод выпуска:2020\nЦена:3299\nВ наличии:✅\n\n⌚Apple watch series 6\nГод выпуска:2021\nЦена:3499\nВ наличии:✅\n\n⌚Apple watch series 7\nГод выпуска:2022\nЦена:3999\nВ наличии:✅\n\n⌚Apple watch series SE(2-ое поколение)\nГод выпуска:2022\nЦена:4999\nВ наличии:✅')
        bot.send_photo(message.chat.id, image_watch)
    #Возвращение в главное меню пользователя
    elif message.text == '🔙Назад' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        btn1 = types.KeyboardButton('🛒Оформить заказ')
        btn2 = types.KeyboardButton('⭐Отзывы')
        btn3 = types.KeyboardButton('👨🏻‍💻Админ-панель')
        btn4 = types.KeyboardButton('🍏🕰iTime')
        btn5 = types.KeyboardButton('🎁Пригласить друга')
        btn6 = types.KeyboardButton('💻Личный кабинет')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
        bot.send_message(message.chat.id,'Что-то не так?',reply_markup=markup)
    #Выбор модель
    elif message.text == '😁Я выбрал':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⌚Apple watch series 5')
        btn2 = types.KeyboardButton('⌚Apple watch series SE(1-ое поколение)')
        btn3 = types.KeyboardButton('⌚Apple watch series 6')
        btn4 = types.KeyboardButton('⌚Apple watch series 7')
        btn5 = types.KeyboardButton('⌚Apple watch series SE(2-ое поколение)')
        btn6 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2, btn3, btn4, btn5,btn6 )
        bot.send_message(message.chat.id,'Мы рады что вы решили приобрести у нас часы!)🤝\nВыберите модель.',reply_markup=markup)
    elif message.text == '⌚Apple watch series 5': #Модель 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        btn1 = types.KeyboardButton('📦Перейти к оформлению')
        btn2 = types.KeyboardButton('🔁Сменить модель')
        btn3 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,'Хорошо!)\nЕсли вы определились с моделью часов вы можете продолжить оформление часов\nЕсли так получилось что вы решили выбрать другую модель просто нажмите на кнопку 🔁Сменить модель ', reply_markup=markup)
        apples = '⌚Apple watch series 5 \n🏷️Цена:2499р'
    elif message.text == '⌚Apple watch series SE(1-ое поколение)': #Модель 2
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        btn1 = types.KeyboardButton('📦Перейти к оформлению')
        btn3 = types.KeyboardButton('🔁Сменить модель')
        btn2 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,'Хорошо!)\nЕсли вы определились с моделью часов вы можете продолжить оформление часов\nЕсли так получилось что вы решили выбрать другую модель просто нажмите на кнопку 🔁Сменить модель', reply_markup=markup)
        apples = '⌚Apple watch series SE(1-ое поколение)\n🏷️Цена:3299р'
    elif message.text == '⌚Apple watch series 6': #Модель 3
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        btn1 = types.KeyboardButton('📦Перейти к оформлению')
        btn3 = types.KeyboardButton('🔁Сменить модель')
        btn2 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Хорошо!)\nЕсли вы определились с моделью часов вы можете продолжить оформление часов\nЕсли так получилось что вы решили выбрать другую модель просто нажмите на кнопку 🔁Сменить модель',reply_markup=markup)
        apples = '⌚Apple watch series 6\n🏷️Цена:3499р'
    elif message.text == '⌚Apple watch series 7': #Модель 4
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        btn1 = types.KeyboardButton('📦Перейти к оформлению')
        btn3 = types.KeyboardButton('🔁Сменить модель')
        btn2 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2,btn3)
        bot.send_message(message.chat.id,'Хорошо!)\nЕсли вы определились с моделью часов вы можете продолжить оформление часов\nЕсли так получилось что вы решили выбрать другую модель просто нажмите на кнопку 🔁Сменить модель', reply_markup=markup)
        apples = '⌚Apple watch series 7\n🏷️Цена:3999р'
    elif message.text == '⌚Apple watch series SE(2-ое поколение)': #Модель 5
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        btn1 = types.KeyboardButton('📦Перейти к оформлению')
        btn3 = types.KeyboardButton('🔁Сменить модель')
        btn2 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2,btn3)
        bot.send_message(message.chat.id,'Хорошо!)\nЕсли вы определились с моделью часов вы можете продолжить оформление часов\nЕсли так получилось что вы решили выбрать другую модель просто нажмите на кнопку 🔁Сменить модель', reply_markup=markup)
        apples = '⌚Apple watch series SE(2-ое поколение)\n🏷️Цена:4999р'
    #Меню оформления заказа
    elif message.text == '📦Перейти к оформлению':
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        btn2 = types.KeyboardButton('📝Заполнить данные для заказа')
        btn3 = types.KeyboardButton('🔁Сменить модель')
        btn1 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, f'Хорошо, проверьте выбранную вами модель и продолжайте оформление(После оформление заказа поменять модель в боте нельзя будет, но вы можете напиать нашему администратору и договриться уже с ним)\n{apples}',reply_markup=markup)
    #Отзывы магазина
    elif message.text == '⭐Отзывы':
        bot.send_message(message.chat.id,'В этом разделе вы найдете самые свежие и объективные отзывы о наших часах от наших клиентов. 🕒💬 Погрузитесь в мир их опыта и делитесь своими впечатлениями!\n\n 🌟👏📢 Подпишитесь на наш Telegram-канал iTimeReviews для более подробной информации и обновлений: https://t.me/iTimeReviews ')
    #Смена модели 
    elif message.text == '🔁Сменить модель':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⌚Apple watch series 5')
        btn2 = types.KeyboardButton('⌚Apple watch series SE(1-ое поколение)')
        btn3 = types.KeyboardButton('⌚Apple watch series 6')
        btn4 = types.KeyboardButton('⌚Apple watch series 7')
        btn5 = types.KeyboardButton('⌚Apple watch series SE(2-ое поколение)')
        btn6 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2, btn3, btn4, btn5,btn6 )
        bot.send_message(message.chat.id,'Что-то не так?',reply_markup=markup)
        bot.send_message(message.chat.id,'⌚Apple watch series 5\nГод выпуска:2019 Год\nЦена:2499\nВ наличии:✅\n\n⌚Apple watch SE(1-ое поколение)\nГод выпуска:2020\nЦена:3299\nВ наличии:✅\n\n⌚Apple watch series 6\nГод выпуска:2021\nЦена:3499\nВ наличии:✅\n\n⌚Apple watch series 7\nГод выпуска:2022\nЦена:3999\nВ наличии:✅\n\n⌚Apple watch series SE(2-ое поколение)\nГод выпуска:2022\nВ наличии:✅\nЦена:4999')
        bot.send_photo(message.chat.id, image_watch)
    #Заполнения данных для заказа
    elif message.text == '📝Заполнить данные для заказа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,text_watch,reply_markup=markup)
    #Отправление заявки администратору если человек оформил заявку
    elif message.text  == 'Да':
        # Удаляем предыдущее сообщение
        bot.delete_message(message.chat.id, previous.message_id)
        # Отправляем предыдущее сообщение другому пользователю
        bot.send_message(my_id, f"Заявка от пользователя @{message.from_user.username}:\n{previous.text}\nМодель:{apples}")
        bot.send_message(message.chat.id, f'Ваша заявка принята в обработку✅)\nОжидайте с вами свяжется наш администратор\nВы так же можете посмотреть наш телеграм канал в котором сможете узнать нас поближе и читать интересные статьи про наши часы)\nt.me/ItimeAppleWatch\nНомер вашей заявки: {ran}')
        order_status[message.chat.id] = apples
        My_prof[message.chat.id] = 'У вас есть заказ'
    previous = message
    #Создание Админ-панель
    if message.from_user.id in admin_id and message.text == '👨🏻‍💻Админ-панель':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1  = types.KeyboardButton('📥Рассылка')
        btn2 = types.KeyboardButton('Все пользователи')
        btn3 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2, btn3 )
        bot.send_message(message.chat.id, '👔Привет админ!)',reply_markup=markup)
    elif message.from_user.id != admin_id and message.text == '👨🏻‍💻Админ-панель':
        bot.send_message(message.chat.id, '🚫Вы не админ!')
        bot.send_message(my_id, f'пользователь:@{message.from_user.username} пытался войти в Админ-панель')
    elif message.from_user.id in admin_id and message.text == '📥Рассылка':
        bot.send_message(message.chat.id, 'Пропишите комманду /send_to_all,а затем текст который хотите отправить всем)',send_to_all(message))
    elif message.text == 'Все пользователи' and message.from_user.id in admin_id:
        bot.send_message(message.chat.id,f'{users_list}')
    elif message.from_user.id != admin_id and message.text == '📥Рассылка':
        bot.send_message(message.chat.id, '🚫Вы не админ!')
        bot.send_message(my_id, f'Пользователь:@{message.from_user.username} пытался сделать рассылку')
    #Приглашение в телеграмм канал
    elif message.text == '🍏🕰iTime':
        bot.send_message(message.chat.id, text_invite)
    elif message.text == '🎁Пригласить друга':
        bot.send_message(message.chat.id,'Вот ваша личная ссылка для приглашения друга.\nОтправьте её другу  если он подпишется вам и ему будет скидка на заказ в 15%\nt.me/iTimeAppleWatch')
    elif message.text == '🔙Назад' and order_status.get(message.chat.id) :
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        btn1 = types.KeyboardButton('🛒Оформить заказ')
        btn2 = types.KeyboardButton('⭐Отзывы')
        btn3 = types.KeyboardButton('👨🏻‍💻Админ-панель')
        btn4 = types.KeyboardButton('🍏🕰iTime')
        btn5 = types.KeyboardButton('🎁Пригласить друга')
        btn6 = types.KeyboardButton('🚚Мой заказ')
        btn7 = types.KeyboardButton('💻Личный кабинет')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7)
        bot.send_message(message.chat.id,'Мы рады что вы выбрали именно нас!)',reply_markup=markup)
    elif message.text == '🚚Мой заказ' and order_status.get(message.chat.id) :
        bot.send_message(message.chat.id, f'Ваш заказ:\n{order_status[message.chat.id]}\nСтатус заказа:В обработке✅\nДля связи:@iTimeshop')
    elif message.text == '💻Личный кабинет' and My_prof.get(message.chat.id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🚚Мой заказ')
        btn2 = types.KeyboardButton('Отправить предложение')
        btn3 = types.KeyboardButton('🔙Назад')
        markup.add(btn1, btn2,btn3)
        bot.send_message(message.chat.id,f'🔐Личный кабинет:\n 👤Имя:{message.from_user.username}\n 📦Ваш заказ:{My_prof[message.chat.id]}, вы можете   посмотреть его нажав на кнопку мой заказ\n 🕒Дата регистрации:{start_date}\n 🆔Ваш ID:{message.from_user.id}\n Для того чтоб отправить предложение просто напишите что хотели бы добавить затем нажмите кнопку,"Отправить предложение", и всё!)',reply_markup=markup)
    elif message.text == '💻Личный кабинет' and not My_prof.get(message.chat.id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙Назад')
        btn2 = types.KeyboardButton('Отправить предложение')
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id, f'🔐Личный кабинет:\n 👤Имя:{message.from_user.username}\n 📦Ваш заказ:К сожалению у вас нет заказа(\n 🕒Дата регистрации:{start_date}\n 🆔Ваш ID:{message.from_user.id}\n Для того чтоб отправить предложение просто напишите что хотели бы добавить затем нажмите кнопку,"Отправить предложение", и всё!)',reply_markup=markup)
    elif message.text == 'Отправить предложение':
        bot.delete_message(message.chat.id, fedd.message_id)
        bot.send_message(my_id, f'Предложение от: @{message.from_user.username}\n{fedd.text}')
        bot.send_message(message.chat.id, 'Благодарим вас за преложние!)😁')
    fedd = message


bot.polling(non_stop=True)
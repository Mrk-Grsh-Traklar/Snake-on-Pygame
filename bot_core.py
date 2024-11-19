from imp import *
from database import DataBase

class TelebotClass:
# token    
    def __init__(self, token, db_name, carttable_name) -> None:
        self.bot = telebot.TeleBot(token)
        self.cash_data = 0

        self.db = DataBase(db_name)
        self.db.create_carttable(carttable_name)
        self.db.insert_data(carttable_name, "BrawlStars", "gems", 999, 1 )

        self.bot.message_handler(commands=['start'])(self.lobby)
        self.bot.callback_query_handler(func=lambda call: True)(self.inline_message_handler)


    def lobby(self, message):
        keyboard = types.InlineKeyboardMarkup()
        products = types.InlineKeyboardButton("Продукты🎮", callback_data="products_button")
        profile = types.InlineKeyboardButton("Профиль👤", callback_data="profile_button")
        Revocation = types.InlineKeyboardButton("Отзывы🦻", callback_data="Revocation_button") 
        shopping_cart = types.InlineKeyboardButton("Корзина🛒", callback_data="shopping_cart_button")
        support = types.InlineKeyboardButton("Поддержка⚙", callback_data="support_button")
        keyboard.add(products,profile,Revocation, shopping_cart,support)

        self.bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=keyboard)

    def products(self, message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        product1 = types.InlineKeyboardButton("BrawlStars", callback_data= "brawlstars_button")
        product2 = types.InlineKeyboardButton("Valorant", callback_data="Valorant_button")
        product4 = types.InlineKeyboardButton("Fortnite", callback_data="Fortnite_button")
        product3 = types.InlineKeyboardButton("Steam", callback_data="Steam_button")
        product5 = types.InlineKeyboardButton("Clash Royale", callback_data="Clash_royale_button")
        product6 = types.InlineKeyboardButton("Twitch", callback_data="Twitch_button")
        product7 = types.InlineKeyboardButton("Discord", callback_data="Discord_button")
        product8 = types.InlineKeyboardButton("Spotify", callback_data="Spotyfy_button")
        product9 = types.InlineKeyboardButton("Minecraft", callback_data="Minecraft_button")
        product10 = types.InlineKeyboardButton("Genshin Impact", callback_data="Genshin_Impact_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        keyboard.add(product1,product2,product3,product4,product5,product6,product7,product8,product9,product10)
        keyboard.add(product11)
        self.bot.send_message(message.chat.id, "Раздел с продуктами", reply_markup=keyboard)

    def profile(self, message):
        # Создаем клавиатуру с двумя кнопками
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        # profile_button = types.InlineKeyboardButton(text="Мой профиль", callback_data="profile_info")
        balance_button = types.InlineKeyboardButton("Пополнить баланс", callback_data="top_up_balance")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        keyboard.add(product11, balance_button)


        # Допустим, у нас есть функции для получения баланса и статуса пользователя
        user_balance = self.get_user_balance(message.chat.id)  # Эта функция должна вернуть реальный баланс
        user_History = self.get_user_History(message.chat.id)

        response_text = f"""
        👤 Ваш профиль:
        ID: {message.chat.id}
        💰 Баланс: {user_balance} $
        ⏳ Сделано покупок: {user_History}

        """

        # Отправляем сообщение с клавиатурой
        self.bot.send_message(message.chat.id, response_text, reply_markup=keyboard)

    # Пример функций для получения баланса и статуса пользователя:
    def get_user_balance(self, user_id):
        # Здесь должен быть реальный код для получения баланса пользователя
        # Для примера вернем фиксированную сумму
        return 1000
    
    def shopping_cart(self, message):

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_up = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        delite_product= types.InlineKeyboardButton("Очистить корзину", callback_data="delite_product_button")
        checkout = types.InlineKeyboardButton("Оформить заказ", callback_data="checkout_button")

        keyboard.add(checkout,delite_product,back_up)
        shopping_cart_text = f'''
        🛒 Корзина:   
        Список всех добавленных товаров:
        заказ №1
        заказ №2
        заказ №3
        Сумма заказа: 1000 $
        '''

        self.bot.send_message(message.chat.id, shopping_cart_text, reply_markup=keyboard)

    def Brawlstars(self,message,table_name):
        self.db.select_data(table_name)
        name,cost = self.con.fetchone()
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'items', reply_markup=keyboard)

    def Valorant(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'lorem ipsum', reply_markup=keyboard)
    
    def Fortnite(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'lorem ipsum', reply_markup=keyboard)

    def Steam(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'lorem ipsum', reply_markup=keyboard)

    def Clash_Roale(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'lorem ipsum', reply_markup=keyboard)

    def Twitch(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'lorem ipsum', reply_markup=keyboard)

    def Discord(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'lorem ipsum', reply_markup=keyboard)

    def Genshin(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'lorem ipsum', reply_markup=keyboard)

    def Minecraft(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'lorem ipsum', reply_markup=keyboard)

    def Spotyfy(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        back_product = types.InlineKeyboardButton("Назад", callback_data="back_button")
        keyboard.add(back_product)
        self.bot.send_message(message.chat.id, f'lorem ipsum', reply_markup=keyboard)



    def get_user_History(self,message):
        return 0
    
    def support(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        keyboard.add(product11)
        self.bot.send_message(message.chat.id, f'Вы всегда можете связаться с нашей тех.поддержкой @AssMaser', reply_markup=keyboard)

    def Revocation(self,message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        add_Revocation = types.InlineKeyboardButton("Оставить отзывы", callback_data="add_Revocation_button")
        see_Revocation = types.InlineKeyboardButton("посмотреть отзывы", callback_data="see_Revocation_button")
        product11 = types.InlineKeyboardButton("В главное меню", callback_data="nazad_button")
        keyboard.add(add_Revocation,see_Revocation,product11)
        self.bot.send_message(message.chat.id, f'Ваши отзывы очень важны для нас😉', reply_markup=keyboard)

    def delete_msg(self, message):
        self.bot.delete_message(message.chat.id, message.message_id)


    def inline_message_handler(self, call):
        data = call.data
        match data:
            case "products_button":
                self.delete_msg(call.message)
                self.products(call.message)
            case "profile_button":
                self.delete_msg(call.message)
                self.profile(call.message)
            case "topup_button":
                self.delete_msg(call.message)
                self.delete_msg(call.message)
            case "nazad_button":
                self.delete_msg(call.message)
                self.lobby(call.message)
            case "money_button":
                self.delete_msg(call.message)
                self.money_game(call.message)
            case "shopping_cart_button":
                self.delete_msg(call.message)
                self.shopping_cart(call.message)
            case 'support_button':
                self.delete_msg(call.message)
                self.support(call.message)
            case 'brawlstars_button':
                self.delete_msg(call.message)
                self.Brawlstars(call.message)
            case 'Valorant_button':
                self.delete_msg(call.message)
                self.Valorant(call.message)
            case 'Fortnite_button':
                self.delete_msg(call.message)
                self.Fortnite(call.message)
            case 'Steam_button':
                self.delete_msg(call.message)
                self.Steam(call.message)
            case 'Clash_royale_button':
                self.delete_msg(call.message)
                self.Clash_Roale(call.message)
            case 'Twitch_button':
                self.delete_msg(call.message)
                self.Twitch(call.message)
            case 'Discord_button':
                self.delete_msg(call.message)
                self.Discord(call.message)
            case 'Spotyfy_button':
                self.delete_msg(call.message)
                self.Spotyfy(call.message)
            case 'Genshin_Impact_button':
                self.delete_msg(call.message)
                self.Genshin(call.message)
            case 'Minecraft_button':
                self.delete_msg(call.message)
                self.Minecraft(call.message)
            case 'back_button':
                self.delete_msg(call.message)
                self.products(call.message)
            case 'Revocation_button':
                self.delete_msg(call.message)
                self.Revocation(call.message)


    def run(self):
        self.bot.infinity_polling()
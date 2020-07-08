# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time
import sqlite3
import telebot
from telebot.types import Message

TOKEN = '1315762320:AAGrFbOXp4w427CeGY_ofPxCyCR5-Uu5gf0'

bot = telebot.TeleBot(TOKEN)

# создаем таблицу если отсустсвует
try:
    cursor.execute("""CREATE TABLE list_of_refs
                    (href text)
                """)
except:
    pass


web_site = 'https://rst.ua'

regions = {'komsomolsk':'http://rst.ua/oldcars/poltava/499',
        'kremenchug':'http://rst.ua/oldcars/poltava/501',
        'svetlovodsk':'http://rst.ua/oldcars/kirovograd/305'}

conn = sqlite3.connect("list_of_cars.db")
cursor = conn.cursor()
cursor.execute('''SELECT * FROM list_of_refs''')
row = cursor.fetchall()
data_base = [x[0] for x in row]

@bot.message_handler(commands=['start', 'help'])
def command_handler(message):
    i  = True
    print('тест')
    bot.send_message(message.chat.id, f'Привет я заработал!')
    while i:      
        with sqlite3.connect("list_of_cars.db") as conn:
            for city, link in regions.items():
                for i in range(1,11):
                    time.sleep(10)
                    # print(f'{city}:{i}')
                    r = requests.get(f'{regions[city]}/{i}.html', headers={'User-Agent':UserAgent().chrome})
                    html = r.content
                    soup = BeautifulSoup(html,'html.parser')
                    obj = soup.find_all('a', attrs = {'class':'rst-ocb-i-a'})
                    obj_price = soup.find_all('span', attrs = {'class':'rst-uix-grey'})
                    # print(obj)
                    for x in range(len(obj)):
                        
                        try:
                            car_name = obj[x].find('span').text
                            car_price = obj_price[x].text
                        except (AttributeError,IndexError):
                            car_name = obj[x]
                            # car_price = obj_price[x].text
                            
                        link_to_car = obj[x].attrs['href']       
                        if link_to_car not in data_base:
                            cursor = conn.cursor()
                            cursor.execute("""INSERT INTO list_of_refs VALUES (?)""",(link_to_car,))
                            # Сохраняем изменения
                            conn.commit()

                            data_base.append(link_to_car)
                            bot.send_message(624450338, f'{web_site}{link_to_car}')
                            bot.send_message(624450338, f'ЦЕНА: {car_price}')
                            
                            bot.send_message(431200271, f'{web_site}{link_to_car}')
                            bot.send_message(431200271, f'ЦЕНА: {car_price}')
                            
if __name__ == "__main__":
    bot.polling(none_stop=True)
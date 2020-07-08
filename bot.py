# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time
import sqlite3
import telebot
from telebot.types import Message
import random



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

# @bot.message_handler(commands=['start', 'help'])
def command_handler():
    i  = True
    # print('тест')
    bot.send_message(431200271, f'Привет я заработал но уже на сервере!')
    bot.send_message(624450338, f'Привет я заработал но уже на сервере!')
    
    while i:      
        with sqlite3.connect("list_of_cars.db") as conn:
            for city, link in regions.items():
                for i in range(1,11):
                    
                    print(f'{city}:{i}')
                    if i == 1:
                        r = requests.get(f'{regions[city]}', headers={'User-Agent':UserAgent().chrome})
                    else:
                        r = requests.get(f'{regions[city]}/{i}.html', headers={'User-Agent':UserAgent().chrome})
                    if int(r.status_code) == 403:
                        bot.send_message(431200271, f'Забанили')
                        bot.send_message(624450338, f'Забанили')
                        
                    html = r.content
                    soup = BeautifulSoup(html,'html.parser')
                    obj = soup.find_all('a', attrs = {'class':'rst-ocb-i-a'})
                    obj_price = soup.find_all('span', attrs = {'class':'rst-uix-grey'})
                    
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
                    time.sleep(random.randint(10, 80))
            time.sleep(random.randint(250, 350))            

if __name__ == "__main__":
    # bot.polling(none_stop=True)
    command_handler()
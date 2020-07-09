import requests            #осуществляет работу с HTTP-запросами
# import urllib.request      #библиотека HTTP
from lxml import html      #библиотека для обработки разметки xml и html, импортируем только для работы с html
# import re                  #осуществляет работу с регулярными выражениями
# from bs4 import BeautifulSoup    #осуществляет синтаксический разбор документов HTML
# import csv                 #осуществляет запись файла в формате CSV
# import tkinter             #создание интерфейса 
# from tkinter.filedialog import *


class Proxy:      
#создаем класс
    proxy_url = 'http://www.ip-adress.com/proxy_list/'     
#переменной присваиваем ссылку сайта, выставляющего прокси-сервера
    proxy_list = []      
#пустой массив для заполнения 

    def __init__(self):       
#функция конструктора класса с передачей параметра self	
        r = requests.get(self.proxy_url)      
#http-запрос методом get, запрос нужно осуществлять только с полным url
        str = html.fromstring(r.content)      
#преобразование документа к типу lxml.html.HtmlElement
        result = str.xpath("//tr[@class='odd']/td[1]/text()")      
#берем содержимое тега вместе с внутренними тегами для получение списка прокси
        for i in result:       
#перебираем все найденные прокси
            if i in massiv:      
#если есть совпадение с прокси уже использованными
                yy = result.index(i)       
#переменная равна индексу от совпавшего прокси в result
                del result[yy]      
#удаляем в result этот прокси
        self.list = result      
#конструктору класса приравниваем прокси
        
    def get_proxy(self):
#функция с передачей параметра self
        for proxy in self.list:
#в цикле перебираем все найденные прокси
            if 'https://'+proxy == proxy1:
#проверяем, совпдает ли до этого взятый прокси с новым, если да:
                    global massiv
#massiv объявляем глобальным 
                    massiv = massiv + [proxy]
#добавляем прокси к массиву
            url = 'https://'+proxy
#прибавляем протокол к прокси
            return url
#возвращаем данные
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
import re
import time

def count(mass_split, unique_mass):
    d = {}
    for item in unique_mass:
        s = 0
        for item2 in mass_split:
            if item == item2:
                s = s + 1
        d[item] = s
    return d

def unique(mass_split):
    unique = []
    for item in mass_split:
        if item in unique:
            continue
        else:
            unique.append(item)
    return unique

mass = 'Наклейка | MTS GameGod Wolf | Кёльн 2014, Наклейка | Copenhagen Wolves | Кёльн 2014, Наклейка | London Conspiracy | Кёльн 2014, ' \
       'Наклейка | dAT team | Кёльн 2014, Наклейка | HellRaisers | Кёльн 2014, Наклейка | Vox Eminor | Кёльн 2014, Наклейка | Vox Eminor | Кёльн 2014, ' \
       'Наклейка | MTS GameGod Wolf | Кёльн 2014, Наклейка | MTS GameGod Wolf | Кёльн 2014, Наклейка | HellRaisers | Кёльн 2014, ' \
       'Наклейка | Copenhagen Wolves | Кёльн 2014, Наклейка | Team LDLC.com | Кёльн 2014, Наклейка | Vox Eminor | Кёльн 2014, ' \
       'Наклейка | HellRaisers | Кёльн 2014, Наклейка | Team Dignitas | Кёльн 2014, Летний кейс eSports 2014, Летний кейс eSports 2014, ' \
       'Летний кейс eSports 2014, Летний кейс eSports 2014, Летний кейс eSports 2014, Летний кейс eSports 2014, Летний кейс eSports 2014, ' \
       'Летний кейс eSports 2014, Летний кейс eSports 2014, Летний кейс eSports 2014, Летний кейс eSports 2014, Летний кейс eSports 2014, ' \
       'Наклейка | Epsilon eSports | Кёльн 2014, Наклейка | Team LDLC.com | Кёльн 2014, Наклейка | Ninjas in Pyjamas | Кёльн 2014, ' \
       'Летний кейс eSports 2014, Наклейка | Team LDLC.com | DreamHack 2014, Наклейка | Fnatic | DreamHack 2014, Наклейка | Team Dignitas | DreamHack 2014, ' \
       'Наклейка | Team LDLC.com | DreamHack 2014, Летний кейс eSports 2014, Летний кейс eSports 2014, Наклейка | Fnatic | Катовице 2015, ' \
       'Наклейка | Natus Vincere | Катовице 2015, Наклейка | Fnatic | Кёльн 2015, Наклейка | Team EnVyUs | Кёльн 2015, Капсула с автографом | Team EnVyUs | Кёльн 2015, ' \
       'Капсула с автографом | Fnatic | Кёльн 2015, Наклейка | Ninjas in Pyjamas | Кёльн 2015, Наклейка | Titan | Кёльн 2015, Наклейка | Team SoloMid | Кёльн 2015, ' \
       'Наклейка | Natus Vincere | Кёльн 2015, Наклейка | Virtus.Pro | Кёльн 2015, Наклейка | mousesports | Кёльн 2015, Наклейка | Team Kinguin | Кёльн 2015, ' \
       'Наклейка | Cloud9 G2A | Кёльн 2015, Капсула с автографом | Titan | Кёльн 2015, Капсула с автографом | Team SoloMid | Кёльн 2015, ' \
       'Капсула с автографом | Virtus.Pro | Кёльн 2015, Наклейка | kioShiMa | Кёльн 2015, Капсула с автографом | Ninjas in Pyjamas | Кёльн 2015, ' \
       'Капсула с автографом | Titan | Кёльн 2015, Наклейка | Fnatic | Клуж-Напока 2015, Капсула с автографом | Team EnVyUs | Клуж-Напока 2015, ' \
       'Капсула с автографом | Team SoloMid | Клуж-Напока 2015, Капсула с автографом | Virtus.Pro | Клуж-Напока 2015, Капсула с автографом | Natus Vincere | Клуж-Напока 2015, ' \
       'Капсула с автографом | G2 Esports | Клуж-Напока 2015, Капсула с автографом | Ninjas in Pyjamas | Клуж-Напока 2015, Капсула с автографом | Luminosity Gaming | Клуж-Напока 2015, ' \
       'Капсула с автографом | Titan | Клуж-Напока 2015, Капсула с автографом | Cloud9 | Клуж-Напока 2015, Капсула с автографом | mousesports | Клуж-Напока 2015, ' \
       'Капсула с автографом | Team Liquid | Клуж-Напока 2015, Капсула с автографом | Flipsid3 Tactics | Клуж-Напока 2015, Капсула с автографом | Vexed Gaming | Клуж-Напока 2015, ' \
       'Капсула с автографом | Counter Logic Gaming | Клуж-Напока 2015, Капсула с автографом | Team Dignitas | Клуж-Напока 2015, Капсула с автографом | Team EnVyUs | Клуж-Напока 2015, ' \
       'Наклейка | Team SoloMid | Клуж-Напока 2015, Наклейка | Natus Vincere | Клуж-Напока 2015, Наклейка | G2 Esports | Клуж-Напока 2015, Капсула с автографом | Ninjas in Pyjamas | Клуж-Напока 2015, ' \
       'Наклейка | Luminosity Gaming | Клуж-Напока 2015, Наклейка | Titan | Клуж-Напока 2015, Наклейка | mousesports | Клуж-Напока 2015, Наклейка | Team Liquid | Клуж-Напока 2015, ' \
       'Наклейка | Flipsid3 Tactics | Клуж-Напока 2015, Наклейка | Vexed Gaming | Клуж-Напока 2015, Наклейка | Counter Logic Gaming | Клуж-Напока 2015, Наклейка | Team Dignitas | Клуж-Напока 2015, ' \
       'Капсула с автографом | Fnatic | Клуж-Напока 2015, Капсула с автографом | Team EnVyUs | Клуж-Напока 2015, Капсула с автографом | Virtus.Pro | Клуж-Напока 2015, ' \
       'Капсула с автографом | Virtus.Pro | Клуж-Напока 2015, Капсула с автографом | G2 Esports | Клуж-Напока 2015, Капсула с автографом | G2 Esports | Клуж-Напока 2015, ' \
       'Капсула с автографом | Natus Vincere | Клуж-Напока 2015, Капсула с автографом | Titan | Клуж-Напока 2015, Капсула с автографом | Team SoloMid | Клуж-Напока 2015, ' \
       'Наклейка | Team SoloMid | Клуж-Напока 2015, Наклейка | Fnatic | Клуж-Напока 2015, Наклейка | Team EnVyUs | Клуж-Напока 2015, Наклейка | Natus Vincere | Клуж-Напока 2015, ' \
       'Наклейка | Flipsid3 Tactics | Клуж-Напока 2015, Наклейка | Ninjas in Pyjamas | Клуж-Напока 2015, Наклейка | Team EnVyUs | Клуж-Напока 2015, Наклейка | Virtus.Pro | Клуж-Напока 2015, ' \
       'Наклейка | Astralis | MLG Columbus 2016, Наклейка | Counter Logic Gaming | Колумбус 2016, Наклейка | mousesports | Колумбус 2016, Наклейка | Luminosity Gaming | MLG Columbus 2016, ' \
       'Наклейка | Gambit Gaming | Колумбус 2016, Наклейка | G2 Esports | Колумбус 2016, Наклейка | FaZe Clan | MLG Columbus 2016, Наклейка | Flipsid3 Tactics | Колумбус 2016, ' \
       'Наклейка | Fnatic | MLG Columbus 2016, Наклейка | Team Liquid | Колумбус 2016, Наклейка | Team EnVyUs | MLG Columbus 2016, Наклейка | Splyce | Колумбус 2016, ' \
       'Наклейка | Virtus.Pro | Колумбус 2016, Наклейка | Natus Vincere | Колумбус 2016, Наклейка | Natus Vincere | Колумбус 2016, Наклейка | Ninjas in Pyjamas | Колумбус 2016, ' \
       'Наклейка | Flipsid3 Tactics | Колумбус 2016, Наклейка | Flipsid3 Tactics | Колумбус 2016, Наклейка | FaZe Clan | MLG Columbus 2016, Наклейка | FaZe Clan | MLG Columbus 2016, ' \
       'Наклейка | Splyce | Колумбус 2016, Наклейка | Astralis | MLG Columbus 2016, Наклейка | Gambit Gaming | Колумбус 2016, Капсула с автографом | Gambit Gaming | MLG Columbus 2016, ' \
       'Капсула с автографом | Team EnVyUs | MLG Columbus 2016, Капсула с автографом | Team Liquid | MLG Columbus 2016, Капсула с автографом | Natus Vincere | MLG Columbus 2016, ' \
       'Капсула с автографом | G2 Esports | MLG Columbus 2016, Наклейка | Astralis | Кёльн 2016, Наклейка | SK Gaming | Кёльн 2016, Наклейка | mousesports | Кёльн 2016, Наклейка | G2 Esports | Кёльн 2016, ' \
       'Наклейка | FaZe Clan | Кёльн 2016, Наклейка | Fnatic | Кёльн 2016, Наклейка | Flipsid3 Tactics | Кёльн 2016, Наклейка | Virtus.Pro | Кёльн 2016, Наклейка | Virtus.Pro | Кёльн 2016, ' \
       'Наклейка | Natus Vincere | Кёльн 2016, Наклейка | Natus Vincere | Кёльн 2016, Наклейка | OpTic Gaming | Кёльн 2016, Наклейка | Counter Logic Gaming | Кёльн 2016, ' \
       'Капсула с автографом | G2 Esports | Кёльн 2016, Капсула с автографом | G2 Esports | Кёльн 2016, Капсула с автографом | Team EnVyUs | Кёльн 2016, ' \
       'Сувенирный набор «ELEAGUE Atlanta 2017 Cobblestone», Сувенирный набор «ELEAGUE Atlanta 2017 Nuke», Сувенирный набор «ELEAGUE Atlanta 2017 Mirage», ' \
       'Наклейка | Team Liquid | Атланта 2017, Наклейка | Natus Vincere | Атланта 2017, Наклейка | GODSENT | Атланта 2017, Наклейка | HellRaisers | Атланта 2017, ' \
       'Наклейка | Astralis | Атланта 2017, Капсула с автографом | Astralis | Атланта 2017, Наклейка | Team EnVyUs | Атланта 2017, Капсула с автографом | Team EnVyUs | Атланта 2017, ' \
       'Наклейка | FaZe Clan | Атланта 2017, Капсула с автографом | FaZe Clan | Атланта 2017, Наклейка | Flipsid3 Tactics | Атланта 2017, Капсула с автографом | Flipsid3 Tactics | Атланта 2017, ' \
       'Наклейка | Fnatic | Атланта 2017, Капсула с автографом | Fnatic | Атланта 2017, Наклейка | G2 Esports | Атланта 2017, Капсула с автографом | G2 Esports | Атланта 2017, ' \
       'Наклейка | Gambit Gaming | Атланта 2017, Капсула с автографом | Gambit Gaming | Атланта 2017, Капсула с автографом | GODSENT | Атланта 2017, Наклейка | HellRaisers | Атланта 2017, ' \
       'Капсула с автографом | HellRaisers | Атланта 2017, Наклейка | mousesports | Атланта 2017, Капсула с автографом | mousesports | Атланта 2017, Наклейка | Natus Vincere | Атланта 2017, ' \
       'Капсула с автографом | Natus Vincere | Атланта 2017, Наклейка | North | Атланта 2017, Капсула с автографом | North | Атланта 2017, Наклейка | OpTic Gaming | Атланта 2017, ' \
       'Капсула с автографом | OpTic Gaming | Атланта 2017, Наклейка | SK Gaming | Атланта 2017, Капсула с автографом | SK Gaming | Атланта 2017, Наклейка | Team Liquid | Атланта 2017, ' \
       'Капсула с автографом | Team Liquid | Атланта 2017, Наклейка | Virtus.Pro | Атланта 2017, Капсула с автографом | Virtus.Pro | Атланта 2017, Наклейка | Team LDLC.com | DreamHack 2014, ' \
       'Наклейка | Titan | Катовице 2015, AK-47 | Синий глянец'

mass_split = mass.split(', ')  # разбиваем строку (188 итемов)

unique_mass = unique(mass_split)   # выбираем уникальные значения из массива (134 итема)

d = count(mass_split, unique_mass)  # тут словарь будет например, ключ - 'Наклейка | Titan | Катовице 2015, AK-47 | Синий глянец': 1 - значение (количество предметов)
s = 0

price_sum = {}

def sum_inventory(price_item):
    q = 0
    for price_item, z in price_sum.items():
        price_item = re.sub("[^0-9|.]", '', price_item)
        q += float(price_item) * z
    return round(q, 2)

try:
    for item, count_item in d.items():
        s = s + 1
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # для открытия headless-браузера
        browser = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', options=options)
        # Переход на страницу входа
        browser.get('https://steamcommunity.com/market/')
        browser.implicitly_wait(5)
        browser.find_element_by_css_selector('#findItemsSearchBox').send_keys(item)
        browser.implicitly_wait(5)
        browser.find_element_by_css_selector('#findItemsSearchSubmit').click()
        browser.implicitly_wait(5)
        try:
            price = WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="result_0"]/div[1]/div[2]/span[1]/span[1]'))).text
        except (TimeoutException, NoSuchElementException):
            text ="Page load Timeout Occured ... moving to next item !!!"
            print(text, item)
            continue
        price_sum[price] = count_item
        print(str(s)+')', item, price, "Количество:", count_item, "Сумма всех элементов =", sum_inventory(price_sum))
        time.sleep(1)
        browser.quit()


finally:
    time.sleep(1)
    browser.quit()





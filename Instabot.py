from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(15)
        button = bot.find_element_by_css_selector('button.HoLwm')
        button.click()
       


    def follower(self):
        bot = self.bot
        bot.get('https://www.instagram.com/selenagomez/')
        time.sleep(2)
        try:
            bot.find_element_by_css_selector('a.-nal3').click()
            time.sleep(4)
            scr1 = bot.find_element_by_css_selector('div.isgrP')
        except: 
            nik.follower()
        i = 2
        while (i < 15): #100
            bot.execute_script("arguments[0].scrollTop = arguments[1]",scr1, 200 * i)
            time.sleep(0.3)
            i += 1

        try:
            allNames = bot.find_elements_by_css_selector('a._0imsa')
            print(allNames)
            name = [elem.get_attribute('title') for elem in allNames]
        except:
            print()
        print(name)
        #b = 0

        for i in name:
            try:
                #if(b > 50):
                  #  time.sleep(120)
                   # b = 0

                print('YYYYYYYYYYYYYYY')
                #nik.like_tweet(i)
                print('XXXXXXXXXXXXXXX')
                #b += 1
            except: 
                pass

        #nik.follower()
        


    def like_tweet(self,name):
        bot = self.bot
        bot.get('https://www.instagram.com/' + name + '/')
        time.sleep(1,5)
        # print('SSSSSSSSSSSSSSSSSSSSs')
        # # try:
        # #     folgenButton = bot.find_element_by_css_selector('button._5f5mN')
        # # except:
        # #     try:
        # #         folgenButton = bot.find_element_by_css_selector('button.BY3EC')
        # #     except:
        # #         return
        # # folgenButton.click()
        # #time.sleep(2)
        # try:
        #     bot.find_element_by_css_selector('button.HoLwm').click()
        #     elem = bot.find_element_by_css_selector('span.g47SY')
        # except NoSuchElementException:
        #     pass
        # anzahl = int(elem.text)
        # time.sleep(1.5)
        # try:
        #     bot.find_element_by_css_selector('div._9AhH0').click()
        # except NoSuchElementException:
        #     return 
        # time.sleep(1)
        # i = 0
        # try:
        #     if(anzahl > 4):
        #         while(i < 4):
        #             actions = ActionChains(bot)
        #             actions.double_click(bot.find_element_by_css_selector('div._9AhH0')).perform()
        #             time.sleep(1.5)
        #             acctions = ActionChains(bot)
        #             acctions.send_keys(Keys.RIGHT).perform()
        #             time.sleep(1.5)
        #             i += 1
        #     else:
        #         while(i < anzahl):
        #             actions = ActionChains(bot)
        #             actions.double_click(bot.find_element_by_css_selector('div._9AhH0')).perform()
        #             time.sleep(1.5)
        #             acctions = ActionChains(bot)
        #             acctions.send_keys(Keys.RIGHT).perform()
        #             time.sleep(1.5)
        #             i += 1
        # except:
        #     return

    def like_frontpage(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')

        for i in range(1,500):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            #tweets = bot.find_element_by_css_selector('div._9AhH0')
            print(tweets)
            # [elem.get_attribute('title') for elem in allNames]
            # for link in links:
            #     try:
            #         link.click()
            #         time.sleep(1)
            #     except Exception as ex:
            #         time.sleep(1)

       


nik = InstaBot(username, password)
nik.login()
nik.follower()


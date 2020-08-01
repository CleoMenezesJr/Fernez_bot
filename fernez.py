from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

import speech_recognition as sr
import pyaudio

from gtts import gTTS
from playsound import playsound


text = ' '
text_2 = ' '

contact_list = []


class talk():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

    def AskMe():
        tts = gTTS('Hola, ¿como te puedo ayudar?', lang='es') 
        tts.save('askme.mp3')
        playsound('askme.mp3')
        talk.Speech()

    
    def WhatLookingFor():
        tts = gTTS('Vale! ¿Para quien vas a enviar ese mensaje?', lang='es')
        tts.save('whatlookingfor.mp3')
        playsound('whatlookingfor.mp3')
        talk.Speech()


    def Contact():
        tts = gTTS('Perfecto! ¿A alguien más?', lang='es')
        tts.save('somore.mp3')
        playsound('somore.mp3')
        talk.Speech()
    
    def Msn():
        tts = gTTS('¿Qué mensaje te gustaria enviar?', lang='es')
        tts.save('msn.mp3')
        playsound('msn.mp3')
        
        with sr.Microphone() as source:
            answer = r.listen(source)

            try:
                text2 = r.recognize_google(speak, language='es-mx')
            except:
                print('Sorry. Could not recognize your voice')




    def Speech(): #Escutar
        global r
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Speak Anything')
            speak = r.listen(source)
            
            try:
                text = r.recognize_google(speak, language='es-mx')
                #Decisçoes
                convert = text.upper()
                print(convert)
                if convert == 'ENVIAR MENSAJE':
                    talk.WhatLookingFor()
                
                elif convert == 'NO':
                    talk.Msn()
                else:
                    contact_list.append(text)
                    talk.Contact()
                
                
            except:
                print('Sorry. Could not recognize your voice')

class WhatsAppBot:
    def __init__(self):
        talk.AskMe()

        self.message_all = ''
        self.people = contact_list
        options = webdriver.ChromeOptions()
        options.add_argument('lang=es-mx')
        self.driver = webdriver.Chrome(chrome_options=options)


    def SendMessages(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)
        for people in self.people:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{str(people).upper()}']")
            time.sleep(3)
            campo_grupo.click()
            time.sleep(10)
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys("Este es un mensaje de prueba.")
            time.sleep(3)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

run = WhatsAppBot()
run.SendMessages()



#("//span[@data-icon='send']")
#importação da biblioteca
import pyautogui as auto
import time

#define o tempo p/ cada comando
auto.PAUSE = 1

#abre o menu iniciar
auto.press('win')
#abre o firefox
auto.write('firefox')
auto.press('enter')

#abre o github
auto.write('github.com')
auto.press('enter')


#abre o classrom em uma nova guia
time.sleep('3')
auto.hotkey('ctrl', 't')
auto.write('classroom.google.com')
auto.press('enter')
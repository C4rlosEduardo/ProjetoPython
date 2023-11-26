import pyautogui
import os.path

pyautogui.PAUSE = 1

#Abre Explore
pyautogui.hotkey('Win', 'e')
#Encontra localizacao botao
button7location = pyautogui.locateOnScreen('C:\BotProject\img\Dlocal.png')
#print(button7location)

button7location[0]
button7location.left #seleciona X,Y

#encontra o centro
button7point = pyautogui.center(button7location)
#print(button7point)

button7point[0]
button7point.x
button7x, button7y = button7point
#Clica no botao
pyautogui.click(button7x, button7y)


pyautogui.PAUSE = 1

#Abre Pasta Bot
#Encontra localizacao botao
buttonlocationPBot = pyautogui.locateOnScreen('C:\BotProject\img\PBot.png')
#print(button7location)

buttonlocationPBot[0]
buttonlocationPBot.left #seleciona X,Y

#btn centro
buttonBotpoint = pyautogui.center(buttonlocationPBot)
#print(button7point)

buttonBotpoint[0]
buttonBotpoint.x
buttonBotx, buttonBoty = buttonBotpoint
#Clica no Pasta Bot
pyautogui.doubleClick(buttonBotx, buttonBoty)


pyautogui.PAUSE = 1
#Abre Pasta Img
#Encontra localizacao botao
buttonPdflocation = pyautogui.locateOnScreen('C:\BotProject\img\pdf.png')
#print(button7location)

buttonPdflocation[0]
buttonPdflocation.left #seleciona X,Y

#btn centro
buttonPdfpoint = pyautogui.center(buttonPdflocation)
#print(button7point)

buttonPdfpoint[0]
buttonPdfpoint.x
buttonPdfx, buttonPdfy = buttonPdfpoint
#Clica no Pasta img
pyautogui.doubleClick(buttonPdfx, buttonPdfy)


#pyautogui.PAUSE = 1

pyautogui.hotkey('alt', 'F4')

# #btnFechar
# #Encontra localizacao botao
# buttonFecharlocation = pyautogui.locateOnScreen('C:\BotProject\img\Fechar.png')
# #print(button7location)

# buttonFecharlocation[0]
# buttonFecharlocation.left #seleciona X,Y

# #btn centro
# buttonFecharpoint = pyautogui.center(buttonFecharlocation)
# #print(button7point)

# buttonFecharpoint[0]
# buttonFecharpoint.x
# buttonPdfx, buttonPdfy = buttonFecharpoint
# #Clica no Pasta Fechar
# pyautogui.click(buttonPdfx, buttonPdfy)




#pyautogui.PAUSE = 2
#Abre Explore

#pyautogui.hotkey('Win', 'e')

#pyautogui.click('C:\BotProject\img\explore.png')

# stc = pyautogui.screenshot()
# stc.save('tt2.png')
# t = pyautogui.locateOnScreen('tt2.png', 'Disco local (C)')



# sc = pyautogui.screenshot(region=(11,690,158,30))
# sc.save('teste.png')

# if(os.path.isfile('teste.png')):
#      pyautogui.click('teste.png')

# while True:
#     pyautogui.displayMousePosition()

'''if pyautogui.locateAllOnScreen('C:\BotProject\img\Dklocal.PNG'):
        print("Esta na tela")
    else:
        print("Não esta na tela")'''

#pyautogui.click('C:\BotProject\img\maximizar.png', interval=0.25)
# pyautogui.doubleClick('C:\BotProject\img\Dklocal.PNG')
# pyautogui.doubleClick('C:\BotProject\img\PBot.png')
# pyautogui.doubleClick('C:\BotProject\img\Ppdf.png')

#pyautogui.click(button='Save')






#Localiza BtnDownload

# try:
#     BtnDlocallocation = pyautogui.locateOnScreen('C:\BotProject\img\BtnDownload.PNG')
# #encontra o centro BtnDownload
#     Pause()
#     BtnDlocalpoint = pyautogui.center(BtnDlocallocation)

# #Param BtnDownloadpoint
#     Pause()
#     BtnSavex, BtnSavey = BtnDlocalpoint
# #Clica no BtnDownloady
#     pyautogui.click(BtnSavex, BtnSavey)

# except:
#     print('Passou')


#Pausa Processo
# Pause()


#Localiza BtnDlocal

# try:
#     BtnDlocallocation = pyautogui.locateOnScreen('C:\BotProject\img\Dlocal.PNG')
# #encontra o centro BtnDownload
#     Pause()
#     BtnDlocalpoint = pyautogui.center(BtnDlocallocation)

# #Param BtnDlocalPoint
#     Pause()
#     BtnSavex, BtnSavey = BtnDlocalpoint
# #Clica no BtnDlocal
#     pyautogui.doubleClick(BtnSavex, BtnSavey)

# except:
#     print('Except BtnDlocal')



# #Pausa Processo
# Pause()


# #localiza Pasta Bot

# try:
#     locationPBot = pyautogui.locateOnScreen('C:\BotProject\img\PBot.png')
#     Pause()
# #encontra o centro BtnDownload
#     PBotpoint = pyautogui.center(locationPBot)
# #Param BtnDlocalPoint
#     Pause()
#     PBotx, PBoty = PBotpoint
# #Clica no Pasta Bot
#     pyautogui.doubleClick(PBotx, PBoty)

# except:
#     print('Except Pasta Bot')


# #Pausa Processo
# Pause()

# #localiza Pasta Pdf

# try:
#     Pdflocation = pyautogui.locateOnScreen('C:\BotProject\img\pdf.png')
#     Pause()
# #encontra o centro BtnDownload
#     Pdfpoint = pyautogui.center(Pdflocation)
# #Param BtnDlocalPoint
#     Pdfx, Pdfy = Pdfpoint
# #Clica no Pasta pdf
#     Pause()
#     pyautogui.doubleClick(Pdfx, Pdfy)

# except:
#     print('Except Pasta Pdf')



#Pausa Processo
#Pause()

#Localiza BtnSave






#Funcao download 

# options = Options()
# options.headless = False

# caminho = os.getcwd()

# profile = webdriver.FirefoxProfile()
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX  # DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# firefox_capabilities.setdefault("marionette.defaultPrefs.enabled", True)
# firefox_capabilities.setdefault("marionette.defaultPrefs.port", 2828)
# firefox_capabilities.setdefault("marionette.logging", True)
# profile.set_preference("startup.homepage_welcome_url", "about: blank")
# profile.set_preference("browser.shell.checkDefaultBrowser", False)
# profile.set_preference("browser.startup.page", 0)
# profile.set_preference("browser.sessionstore.resume_from_crash", False)
# profile.set_preference("browser.warnOnQuit", False)
# profile.set_preference("browser.cache.disk.enable", False)
# # profile.set_preference('network.proxy.socks_port', port)
# # profile.set_preference("browser.cache.memory.enable", False)
# # profile.set_preference("network.proxy.type", 1)
# # profile.set_preference("network.proxy.http", proxy)
# # profile.set_preference("network.proxy.https", proxy)
# # profile.set_preference("network.proxy.http_port", port)
# # profile.set_preference("network.proxy.ssl", proxy)
# # profile.set_preference("network.proxy.ssl_port", port)
# profile.set_preference("browser.cache.disk.enable", True)
# profile.set_preference("browser.cache.memory.enable", True)
# profile.set_preference("browser.cache.offline.enable", True)
# profile.set_preference("network.http.use-cache", True)
# profile.set_preference("browser.download.folderList", 2)
# profile.set_preference("browser.download.manager.showWhenStarting", False)


# profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
#                                    "application/pdf;application/x-www-form-urlencoded")
# profile.set_preference("pdfjs.disabled", True)
# profile.set_preference("browser.download.dir", r"C:\BotProject\Pdf")
# profile.update_preferences()
#profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/force-download;application/octet-stream")
#profile.set_preference("browser.download.manager.showWhenStarting", False)

#options = webdriver.FirefoxOptions()
#options.add_argument('--headless')

#CaminhoDownloads = "C:\BotProject"
#options.add_argument("download.default_directory='{CaminhoDownloads}'")

#driver = webdriver.Firefox()#(options=options)
#driver = webdriver.Firefox(options=options, firefox_profile=profile)#,
                                       #capabilities=firefox_capabilities)
                                       #,
                                       #executable_path=caminho + '\geckodriver.exe',
                                       #service_log_path=caminho + '\geckodriver.log')


# options = Options()

# options.set_preference("browser.download.folderList",2)
# options.set_preference("browser.download.manager.showWhenStarting", False)
# options.set_preference("browser.download.dir","C:\BotProject\Pdf")
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/force-download;application/octet-stream")
#(firefox_options=options)
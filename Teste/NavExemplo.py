import pyautogui

def Pause():
    pyautogui.PAUSE = 1

class Save:
    #def ConPath(): 
    #Pausa Processo

    #Localiza BtnDownload
    def BtnDownload():
        try:
            BtnDlocallocation = pyautogui.locateOnScreen('C:\BotProject\img\BtnDownload.PNG')
        #encontra o centro BtnDownload
            Pause()
            BtnDlocalpoint = pyautogui.center(BtnDlocallocation)

        #Param BtnDownloadpoint
            Pause()
            BtnSavex, BtnSavey = BtnDlocalpoint
        #Clica no BtnDownloady
            pyautogui.click(BtnSavex, BtnSavey)

        except:
            print('Passou')


    #Pausa Processo
    Pause()


    #Localiza BtnDlocal
    def BtnDlocal():
        try:
            BtnDlocallocation = pyautogui.locateOnScreen('C:\BotProject\img\Dlocal.PNG')
        #encontra o centro BtnDownload
            Pause()
            BtnDlocalpoint = pyautogui.center(BtnDlocallocation)

        #Param BtnDlocalPoint
            Pause()
            BtnSavex, BtnSavey = BtnDlocalpoint
        #Clica no BtnDlocal
            pyautogui.doubleClick(BtnSavex, BtnSavey)

        except:
            print('Passou')



    #Pausa Processo
    Pause()


    #localiza Pasta Bot
    def Pastabot():
        try:
            locationPBot = pyautogui.locateOnScreen('C:\BotProject\img\PBot.png')
            Pause()
        #encontra o centro BtnDownload
            PBotpoint = pyautogui.center(locationPBot)
        #Param BtnDlocalPoint
            Pause()
            PBotx, PBoty = PBotpoint
        #Clica no Pasta Bot
            pyautogui.doubleClick(PBotx, PBoty)

        except:
            print('Passou')


    #Pausa Processo
    Pause()

    #localiza Pasta Pdf

    def Pastapdf():
        try:
            Pdflocation = pyautogui.locateOnScreen('C:\BotProject\img\pdf.png')
            Pause()
        #encontra o centro BtnDownload
            Pdfpoint = pyautogui.center(Pdflocation)
        #Param BtnDlocalPoint
            Pause()
            Pdfx, Pdfy = Pdfpoint
        #Clica no Pasta pdf
            pyautogui.doubleClick(Pdfx, Pdfy)

        except:
            print('Passou')



    #Pausa Processo
    Pause()

    #Localiza BtnSave

    def BtnSave():
        try:
            BtnDlocallocation = pyautogui.locateOnScreen('C:\BotProject\img\BtnSave.PNG')
        #encontra o centro BtnSave
            Pause()
            BtnDlocalpoint = pyautogui.center(BtnDlocallocation)
        #Param BtnSave
            Pause()
            BtnSavex, BtnSavey = BtnDlocalpoint
        #Clica no BtnDownloady
            pyautogui.click(BtnSavex, BtnSavey)

        except:
            print('btnSave Bugou!')

    #Pausa Processo
    Pause()

    pyautogui.hotkey('alt', 'F4')
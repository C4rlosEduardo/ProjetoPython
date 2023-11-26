
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.firefox.options import Options
import pyautogui



from Func.conn import Consulta
from Entities.Usuario import Usuario

usuarios = Consulta()


for usuario in usuarios:

    try:
        login = usuario[2] 
        senha = usuario[3] 

        print('Iniciar')

        driver = webdriver.Firefox()

        driver.get("https://cloud.staffexpress.jp/ikaigr/neo/index.php")


        #Id
        print('Inserido Id')
        idi_text = driver.find_element(By.XPATH,"//*[@id='idi_text']")
        idi_text.send_keys(login)

        #Login
        print('Inserido Login')
        login_pw = driver.find_element(By.XPATH,"//*[@id='pwi']")
        login_pw.send_keys(senha)

        time.sleep(2)

        #clickButton
        print('ClickButton')
        element = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div/form/button')#driver.find_element(By.XPATH, "//*[@id='login']/div/form/input")
        element.click()

        print('Logar')

        time.sleep(2)

        home_calendar = driver.find_element(By.XPATH, '//*[@id="home_calendar"]/tbody')

        #Verificar tag
        #Exist_Link = len(home_calendar.find_elements(By.TAG_NAME, 'tr')[2].find_elements(By.TAG_NAME, 'a')) > 0

        Exist_Link =  home_calendar.find_elements(By.TAG_NAME, 'tr')

        _link = False
        for tr in Exist_Link:
            if tr.find_elements(By.TAG_NAME, 'a'):
                _Link = True
                break


        select_element = driver.find_element(By.NAME, 'y')
        select = Select(select_element)
        AnoSelect = select.first_selected_option.text


        select_element = driver.find_element(By.NAME, 'm')
        select = Select(select_element)
        MesSelect = select.first_selected_option.text

        from Func.Mes import Mes    

        mes = Mes(MesSelect)
        Ano = AnoSelect
        NomeAqurivo = 'Horel_' + MesSelect + '_' + Ano + "_" + mes


        if _Link == True:

            qtd = 0

            listTr = home_calendar.find_elements(By.TAG_NAME, 'tr')

            for tr in listTr:
                if tr.find_elements(By.TAG_NAME, 'a'):
                    tr.find_element(By.TAG_NAME, 'a').click()
                    break

            # Carregar Tr
            #list_dias = home_calendar.find_elements(By.TAG_NAME, 'tr')[2].text.split()
            #for dia in list_dias:
                #print(dia)
                #if dia == '13':
                    #print('dia = ' + dia)
                    #home_calendar.find_elements(By.TAG_NAME, 'tr')[2].find_elements(By.TAG_NAME, 'a')[0].click()
                    #break
                #elif dia == '14':
                    #print('dia = ' + dia)
                    #home_calendar.find_elements(By.TAG_NAME, 'tr')[2].find_elements(By.TAG_NAME, 'a')[0].click()
                    #break
                #elif dia == '15':
                    #print('dia = ' + dia)
                    #home_calendar.find_elements(By.TAG_NAME, 'tr')[2].find_elements(By.TAG_NAME, 'a')[0].click()
                    #break

            #content = driver.page_source

            btnDown = driver.find_element(By.ID, 'download')
            btnDown.click()

            def Pause():
                pyautogui.PAUSE = 2

        
            #Localiza BtnSeta

            try:
                pyautogui.write(NomeAqurivo) 

                Pause()
                BtnSetalocation = pyautogui.locateCenterOnScreen('C:\BotProject\img\seta.PNG')
                #encontra o centro BtnSeta
                Pause()
                BtnSetapoint = pyautogui.center(BtnSetalocation)

                #Param BtnDownloadpoint
                Pause()
                BtnSetaSavex, BtnSetaSavey = BtnSetapoint
                #Clica no BtnDownloady
                pyautogui.click(BtnSetaSavex, BtnSetaSavey)

            except:
                print('Except BtnSeta, forca tarefa')
                Pause()
                BtnSetalocation = pyautogui.locateOnScreen('C:\BotProject\img\seta.PNG')
                #encontra o centro BtnSeta
                Pause()
                BtnSetapoint = pyautogui.center(BtnSetalocation)
                #Param BtnDownloadpoint
                BtnSetaSavex, BtnSetaSavey = BtnSetapoint
                #Clica no BtnDownloady
                pyautogui.click(BtnSetaSavex, BtnSetaSavey)

                #Exemplo 1

                pyautogui.write('C:\BotProject\Pdf')  
                pyautogui.press('enter')
                pyautogui.hotkey('alt', 'l')

                #Exemplo 2
                #clipboard.copy("C:\BotProject\Pdf")

                #Finaliza o processo FireFox
                driver.quit()

                import Func.LerPdf 
                        


        else:
            print("Mês não contém Horelite!")
            #Finaliza o processo FireFox
            driver.quit()

    except Exception as e:
        print(e.args)
        from Func.RemovePdf import RemoveArq
        RemoveArq('C:\BotProject\Pdf')
        #Finaliza o processo FireFox
        driver.quit()





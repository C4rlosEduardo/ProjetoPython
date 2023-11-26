import base64, os
import  pyodbc


# Conexão com o banco de dados
Conn =  pyodbc.connect('Driver={SQL Server};'
    'Server=DESKTOP-9HU6DH7;'
    'Database=DB_BOT;'
    'UID=sa;'
    'PWD=Japao2023')


Caminho = "C:\BotProject\Pdf"
for _, _, arquivo in os.walk('C:\BotProject\Pdf'):
    Caminho += "\\" + arquivo[0]

with open(Caminho, "rb") as img_file:
    my_string = base64.b64encode(img_file.read())


print(my_string)

cursor = Conn.cursor()

img = my_string.decode('utf-8')

cursor.execute("INSERT INTO [dbo].[TBL_SERVICO]" +
        "([COD_USUARIO] " + 
        ",[IMG_PDF]) " +
    "VALUES('1'"
        ",'"+ str(img) + "')")
    
    #print(t)
cursor.commit()







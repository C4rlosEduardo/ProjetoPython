import os

caminho = 'C:\BotProject\Pdf'

dir = caminho
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
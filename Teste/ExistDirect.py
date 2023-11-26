import os, shutil
import PyPDF2
import tabula

import csv
import openpyxl


import warnings
warnings.filterwarnings("ignore") 

arquivo = '.\Pdf'

arquivoPdf = open('C:\BotProject\Pdf\Horel2023_Agosto.pdf','rb')
pdf = PyPDF2.PdfReader(arquivoPdf)

pagina = pdf._get_page(0)

conteudo_pdf = pagina.extract_text()
print(conteudo_pdf)



ListaTabela = tabula.read_pdf('C:\BotProject\Pdf\Horel2023_Agosto.pdf', pages = 'all')
#print(ListaTabela)

print(ListaTabela)

list3 = ListaTabela[3]
#array = list3.split(' ', '|')

strreplace = str(list3).replace('NaN', '').replace('Unnamed: 0', '').replace('Unnamed: 1', '').replace('Unnamed: 2', '').replace('Unnamed: 3', '').replace('Unnamed: 4', '')
arquivo = open('arq01.txt','w')


arquivo.write(strreplace)
arquivo.close()

#Salva Aquivo na estrutura

input_file = arquivo.name
output_file = 'test.xlsx'

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

with open(input_file, 'r') as data:
    reader = csv.reader(data, delimiter='\t')
    for row in reader:
        ws.append(row)

wb.save(output_file)



#for l in ListaTabela:
    #for tabela in ListaTabela.items[l]:
    #print(l)
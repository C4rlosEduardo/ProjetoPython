import os, shutil
import PyPDF2
import tabula
import base64
from Entities.Servico import Servico

def LimpaString(NomeAtual):
    
    Dic_Nome = {
         "Unnamed:" : ""
        , "Unnamed: 0":""
        , "Unnamed: 1": ""
        , "Unnamed: 2": ""
        , "Unnamed: 3": ""
        , "Unnamed: 4": ""

        , "NaN":  ""
        ,"1\n0" : ""
        ,"1\n0": ""
        ,"[" : ""

        ,"0" : ""
        ,"1" : ""
        ,"2" : ""
        ,"3" : ""

        ,"de\n0" : ""

        ,"folgas\n1" : ""
        ,"remuneradas\n2" : ""
        ,"Restante" : ""

        ,"NaN\n0" : ""
        ,"NaN\n1" : ""
        ,"NaN\n2" : ""
        ,"NaN\n3" : ""
        ,"NaN\n4" : ""
        ,"NaN\n5" : ""
        ,"NaN\n6" : ""
        ,"NaN\n7" : ""
        ,"NaN\n8" : ""
        ,"NaN\n9" : ""
        ,"NaN\n10" : ""
        ,"NaN\n12" : ""

        ,"NaN," : ""
        
        , "F": ""
        , "r": ""
        , "e": ""
        , "q": ""
        , "u": "" 
        , "ê": "" 
        , "n": "" 
        , "c": "" 
        , "i": "" 
        , "a": "" 
        
        , "R": "" 
        , "e": "" 
        , "n": "" 
        , "d": "" 
        , "i": "" 
        , "m": "" 
        , "e": "" 
        , "n": "" 
        , "t": "" 
        , "o": "" 

        , "D": "" 
        , "e": "" 
        , "s": "" 
        , "p": "" 
        , "e": "" 
        , "s": "" 
        , "a": "" 
        , "s": "" 

        , "e": ""  }
    
    AtualS = str(NomeAtual).split(" ")

    count = 0
    t = []
    for qtdstr in AtualS:
        
        if qtdstr != "":
            if qtdstr in Dic_Nome:
                AtualS[count].replace(qtdstr, '')
            else:
            #if qtdstr != Dic_Nome:
              t.append(AtualS[count])
        count = count + 1
                
    return t

Caminho = "C:\BotProject\Pdf"
for _, _, arquivo in os.walk('C:\BotProject\Pdf'):
    Caminho += "\\" + arquivo[0]

#Convert Img pdf para Base64
with open(Caminho, "rb") as img_file:
    ImgPdfBase64 = base64.b64encode(img_file.read())

ListaTabela = tabula.read_pdf(Caminho, pages = 'all')

MesAno = Caminho.split("_")
Mes = MesAno[1]
Ano = MesAno[2]

list2 = ListaTabela[3:6]
print(list2)

#ArrayList1 = LimpaString(str(list1))
#print(ArrayList1)

ArrayList2 = LimpaString(str(list2))
print(ArrayList2)


servico = Servico()

#list1
servico.DiasTrabalhados = "" #ArrayList1[int('08')]
#Foi necessario para efetuar replace
Restante_Remuneradas = "" #ArrayList1[int('09')]
servico.RestanteRemuneradas = "" #Restante_Remuneradas.replace('\n4', '')

servico.HorasTrabalhadas = "" #ArrayList1[16]
servico.HorasExtras = "" #ArrayList1[17] 
servico.HorasNoturnas = "" #ArrayList1[18]


#list2
servico.Aposentadoria = ""
servico.SeguroDesemprego = ""
servico.ImpostoRenda = ""

servico.SeguroCiclista = ""
servico.Aluguel = ""
servico.AluguelAguaGas = ""
servico.AssocicaoHakuikai = ""

servico.mes = str(Mes)
servico.ano = str(Ano)
servico.RedimentoBruto = ArrayList2[11]
servico.DeducaoTotal = ArrayList2[12]
servico.RedimentoLiquido = ArrayList2[13]
servico.DepositoBancario = ArrayList2[14]

servico.ValorTributario = ArrayList2[62]
servico.SeguroSocial = ArrayList2[63]
servico.ImpostoRetidoFonte = ArrayList2[64]

servico.ImgPdf = ImgPdfBase64.decode('utf-8')

try:
    from Func.conn import Consulta
    from Entities.Usuario import Usuario
    usuarios = Consulta()

    codUsuario = str(usuarios).split(",")
    CodUsu = str(codUsuario[0]).replace("[[", "")

    servico.codUsuario = CodUsu
except Exception as e:
    print(e.args)

#Servico(servico)

from Func.RemovePdf import RemoveArq
Caminho = "C:\BotProject\Pdf"
RemoveArq(Caminho)

from Func.conn import save
save(servico)
import pyodbc
import pandas as pd

def Consulta():

    # Criar o objeto cursor
    cursor = Conn.cursor()

    # Executar a consulta SQL
    cursor.execute('SELECT COD_USUARIO,NOME,USUARIO,SENHA, ATIVO FROM [DBO].[TBL_USUARIO] WHERE Ativo = 1' )

    # Busca todos os resultados
    from Entities.Usuario import Usuario
    usuario = Usuario()

    from_db = []

    for row in cursor:
        row = list(row)
        from_db.append(row)

    #columns = ["Cod_Usuario","Nome","Usuario","Senha"]
    #df = pd.DataFrame(from_db, columns= columns)

    # for row in from_db:
    #     usuario.codUsuario = str(row[0])
    #     usuario.nome = row[1]
    #     usuario.usuario = row[2]
    #     usuario.senha = row[3]
    #     usuario.ativo = str(row[4])

    #t = row[1]
    #i = int(row['Cod_Usuario'])
    #usuario.codUsuario = str(t)
    #usuario.nome = row['Nome']
    #usuario.usuario = row['Usuario']
    #usuario.senha = row['Senha']

    return from_db
    

def save(servico):

    from Entities.Servico import Servico
    S = Servico()
    S = servico
    # ListaServico = ListaServico

    # Criar o objeto cursor
    cursor = Conn.cursor()

     # Executar a consulta Insert
    
    try:

        cursor.execute("INSERT INTO [dbo].[TBL_SERVICO]" +
        "([COD_USUARIO] " +

        ",[MES] " +
        ",[ANO] " +

        ",[ALUGUEL] " +
        ",[DIAS_TRABALHADO] " +
        ",[HORAS_NORTUNAS] " +
        ",[HORAS_EXTRAS] " +
        ",[NORTUNO_TRABALHADO] " +
        ",[REDIMENTO_BRUTO] " +

        ",[DEDUCAO_TOTAL] " +
        ",[REDIMENTO_LIQUIDO] " +
        ",[DEPOSITO_BANCARIO] " +
        ",[VALOR_TRIBUTARIO] " +
        ",[SEGURO_SOCIAL] " +
        ",[IMPOSTO_RETIDO_FONTE] " +

        ",[FOLGA_TOTAL] " +
        ",[SALARIO_BASE] " +
        ",[APOSENTATORIA] " +
        ",[SEGURO_DESEMPREGO] " +
        ",[IMPOSTO_RENDA] " +
        ",[ASSOCIACAO_HAKUKAI] " +
        ",[SEGURO_CICLISTA] " +
        ",[IMG_PDF]) " +
    "VALUES("+ S.codUsuario + ""

        ",'"+ S.mes + "'" +
        ",'"+ S.ano + "'" +

        ",'"+ S.Aluguel + "'" +
        ",'"+ S.DiasTrabalhados + "'" +
        ",'"+ S.HorasNoturnas +"'" +
        ",'"+ S.HorasExtras + "'" +
        ",'"+ S.HorasNoturnas + "'" +
        ",'"+ S.RedimentoBruto + "'" +
        #Nova Linha adiconada 
        ",'"+ S.DeducaoTotal + "'" +
        ",'"+ S.RedimentoLiquido + "'" +
        ",'"+ S.DepositoBancario + "'" +
        ",'"+ S.ValorTributario + "'" +
        ",'"+ S.SeguroSocial + "'" +
        ",'"+ S.ImpostoRetidoFonte + "'" +

        ",'"+ S.RestanteRemuneradas + "'" +
        ",'"+ S.RedimentoBruto + "'" +
        ",'"+ S.Aposentadoria + "'" +
        ",'"+ S.SeguroDesemprego + "'" +
        ",'"+ S.ImpostoRenda + "'" +
        ",'"+ S.AssocicaoHakuikai + "'" +
        ",'"+ S.SeguroCiclista + "'" +
        ",'"+ S.ImgPdf + "')")

    except Exception as e:
        print(type(e))
        print(e.args)
        print(e)
        
    
    #print(t)
    cursor.commit()


# Conexão com o banco de dados
Conn =  pyodbc.connect('Driver={SQL Server};'
    'Server=DESKTOP-9HU6DH7;'
    'Database=DB_BOT;'
    'UID=sa;'
    'PWD=Japao2023')
  



def Mes(NomeMes):
    
    Dic_Mes = {
        "Janeiro": "1"
        , "Fevereiro": "2"
        , "Marco":"3"
        , "Abril": "4"
        , "maio": "5"
        , "Junho": "6"
        , "Julho": "7"
        , "Agosto": "8"
        , "Setembro": "9"
        , "outubro": "10"
        , "Novembro": "11"
        , "Dezembro": "12"  }
    
    for M, valor in Dic_Mes.items():
        if NomeMes == valor:
            NomeMes = M
            break

    return NomeMes
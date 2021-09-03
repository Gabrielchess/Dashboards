# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 11:49:50 2021

@author: geologia
"""

def month_name (number):
    if number == "janeiro":
        return "01"
    elif number == 'fevereiro':
        return "02"
    elif number == "março":
        return "03"
    elif number == "abril":
        return "04"
    elif number == "maio":
        return "05"
    elif number == "junho":
        return "06"
    elif number == "julho":
        return "07"
    elif number == "agosto":
        return "08"
    elif number == "setembro":
        return "09"
    elif number == "outubro":
        return "10"
    elif number == "novembro":
        return "11"
    elif number == "dezembro":
        return "12"
    
def dataInvalida(df):
    df = df[df.Data.str.contains("^29/02") == False]
    df = df[df.Data.str.contains("^30/02") == False]
    df = df[df.Data.str.contains("^31/02") == False]
    df = df[df.Data.str.contains("^31/04") == False]
    df = df[df.Data.str.contains("^31/06") == False]
    df = df[df.Data.str.contains("^31/09") == False]
    df = df[df.Data.str.contains("^31/11") == False]
    df = df[df.Data.str.contains("^nan") == False]
    
    return df
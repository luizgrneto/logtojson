#Script para conversão de arquivo de log para json
#Arquivo de log continha 3 colunas Diretorio, Total_Cotas e Usado_Cotas, espaçados apenas por tabulação 


import json
import os
import glob
import sys
import time

folder = '/content/*'


def log_to_json(arquivo):

  if os.path.isfile(arquivo):
  
    with open(arquivo,'r') as f:
      data  = f.read()

    data_split = data.split('\n')

    dir_index = data_split[1].index("Diretorio")
    total_index = data_split[1].index("Total_Cotas")
    usado_index = data_split[1].index("Usado_Cotas")

    dicionario = [{'Diretorio': data_split[2][dir_index:total_index].strip(), 'Total_Cotas': data_split[2][total_index:usado_index].strip(), 'Usado_Cotas': data_split[2][usado_index:len(data_split[2])]}]

    for i in data_split[3:len(data_split)-1]:
      dicionario.append({'Diretorio': i[dir_index:total_index].strip(), 'Total_Cotas': i[total_index:usado_index].strip(), 'Usado_Cotas': i[usado_index:len(i)]})

    dicionario2 = {data_split[0]: dicionario}

    return print(json.dumps(dicionario2))

  else: return('Não é arquivo!')


for file in glob.glob(folder):
    if os.path.getmtime(file) < time.time() - 24 * 60 * 60:  #Só interessava arquivos de 24h atrás
      continue
    else: log_to_json(file)


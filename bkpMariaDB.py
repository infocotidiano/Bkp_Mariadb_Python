# program       bkpMariDB.py
# author        Daniel de Morais
# installation  Backup base de dados Banco MariaDB
# date-written  14/07/2024

import time
import os
import sys
import subprocess 

LDATA    = time.strftime('%Y%m%d_%H%M%S')
LUSUARIO = 'root'
LSENHA   = 'Info@1234'
LPORTA   = 3306
LBANCO   = 'hermes'
LDESTINO = 'c:/temp'
LHOST    = 'localhost'
LPATHDUMP= '"C:/Program Files/MariaDB 10.9/bin/mysqldump"'

LNomeArquivoDestino = "%s/%s-%s.sql" % (LDESTINO, LBANCO, LDATA)
print('Arquivo de destino: ',LNomeArquivoDestino)
ComandoBkp =  ("%s -u %s -p%s -h %s -e --opt -B -R -c %s > %s" % (LPATHDUMP,LUSUARIO, LSENHA, LHOST, LBANCO, LNomeArquivoDestino))
print(ComandoBkp)
cmd_result = subprocess.getoutput(ComandoBkp)
LProcesso = subprocess.Popen(ComandoBkp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = LProcesso.communicate()
if LProcesso.returncode != 0:
    print(f"Erro ao realizar o backup: {stderr.decode('utf-8')}")
else:
    print("Backup realizado com sucesso!")



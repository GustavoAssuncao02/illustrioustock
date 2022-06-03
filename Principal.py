class usuário:
    def __init__(self,nome= None,CPF = None,dataNascimento = None, senha = None, email = None):
        self.nome = nome
        self.CPF = CPF
        self.dataNascimento =dataNascimento
        self.senha = senha
        self.email = email
    
    def nomeGet(self):
        return self.nome
    
    def nomeSet(self,nome):
        self.nome = nome
    
    def cpfGet(self):
        return self.CPF
    
    def cpfSet(self,cpf):
        self.cpf = cpf
    
    def dataNascimentoGet(self):
        return self.dataNascimento

    def dataNascimentoSet(self,data):
        self.dataNascimento = data

    def senhaGet(self):
        return self.senha

    def senhaSet(self,senha):
        self.senha = senha

    def emailGet(self):
        return self.email
    
    def emailSet(self,email):
        self.email = email

    def idGet(self):
        pass   #codificar conexão com o banco caso necessário

class item:
    def __init__(self,foto = None, nome =None):
        self.foto = foto
        self.nome = nome

    def fotoGet(self):
        return self.foto

    def fotoSet(self,foto):
        self.foto = foto
    
    def nomeGet(self):
        return self.nome

    def nomeSet(self,nome):
        self.nome = nome

    def idGet(self):
        pass   #codificar conexão com o banco caso necessário
class categoria:
    def __init__(self,nome = None):
        self.nome = nome

    def nomeGet(self):
        return self.nome
    
    def nomeSet(self, nome):
        self.nome = nome

    def idGet(self):
        pass #codificar conexão com o banco caso necessário 
        
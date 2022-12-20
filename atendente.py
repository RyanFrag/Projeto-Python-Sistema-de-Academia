from aluno import Aluno
from personal import Personal
import random


class Atendente:
    def __init__(self, senha, nome):
        self.senha = senha
        self.nome = nome

    def create_entity(self, data, typeAluno=None):
        if not data:
            return 'ERRO, data não encontrada'
        senha = generate_senha()
        if typeAluno is True:
            data['cpf'] = str(data.get('cpf'))
            if not data.get('cpf').isnumeric():
                return 'ERRO, cpf invalido'
            if not data.get('nome') or not data.get('tipo_mensalidade'):
                return 'ERRO, campos obrigatórios não são enviados'
            aluno = Aluno(nome=data.get('nome'), cpf=data.get('cpf'), email=data.get('email'),
                          telefone=data.get('telefone'), tipo_mensalidade=data.get('tipo_mensalidade'), senha=senha)
            return aluno
        if typeAluno is False:
            data['cpf'] = str(data.get('cpf'))
            if not data.get('cpf').isnumeric():
                return 'ERRO, cpf invalido'
            if not data.get('nome'):
                return 'ERRO, campos obrigatórios não são enviados'
            personal = Personal(nome=data.get('nome'),cpf=data.get('cpf'), senha=senha)
            return personal
        if not typeAluno:
            self.setNome(data.get('nome'))
            self.setSenha(senha)

    def edit_entity(self, cpf, data: dict, bank_data: dict, aluno: Aluno):
        if self.search_um_aluno(cpf, bank_data):
            if data.get('nome'):
                aluno.setNome(data.get('nome'))
            if data.get('telefone'):
                aluno.setTelefone(data.get('telefone'))
            if data.get('email'):
                aluno.setEmail(data.get('email'))
            if data.get('tipo_mensalidade'):
                aluno.set_tipo_mensalidade(data.get('tipo_mensalidade'))
            return aluno
        else:
            return False

    def entrada(self, senha, bank_data):
        if not senha.isnumeric():
            return 'ERRO, insira uma senha válida'
        for aluno in bank_data:
            if senha == aluno.senha:
                print('Bem vindo')
                return True
        print('Erro, Senha não encontrada')
        return False

    def search_um_aluno(self, cpf, bank_data):
        for aluno in bank_data:
            if aluno.cpf == cpf:
                return vars(aluno)
        print('Aluno não encontrado')
        return False

    def search_alunos(self, tipo_mensalidade, bank_data):
        res = []
        for aluno in bank_data:
            if aluno.tipo_mensalidade == tipo_mensalidade:
                res.append(aluno)
        if len(res) == 0:
            return 'Tipo de mensalidade não encontrado'
        return res

    def setNome(self, nome):
        self.nome = nome

    def setSenha(self, senha):
        self.senha = senha


def generate_senha():
    senha = []
    i = None
    for i in range(0, 4):
        senha.append(str(random.randint(0, 9)))
    senha = ''.join(senha)
    return senha


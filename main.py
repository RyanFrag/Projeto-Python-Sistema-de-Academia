from academia import Academia
from atendente import Atendente

academia = Academia(nomeAcademia='GYM', endereco='Ryan Street Gym')
atendente = Atendente(nome='Ryan', senha='1708')

data = {
    'nome': 'João',
    'cpf': '11111111111',
    'email': 'joãozinho@gmail.com',
    'telefone': '40028922',
    'tipo_mensalidade': '1',
    'date': {
        'dia': '17',
        'mes': '08',
        'ano': '2022',
        'valor': '150'
    }
}


data1 = {
    'nome': 'José',
    'cpf': '987654321',
    'email': 'josezinho@gmail.com',
    'telefone': '40028922',
    'tipo_mensalidade': '1',
    'date': {
        'dia': '17',
        'mes': '08',
        'ano': '2022',
        'valor': '150'
    }
}

data2 = {
    'nome': 'Ryan',
    'cpf': '123456789',
    'email': 'ryanzito@gmail.com',
    'telefone': '40028922',
    'tipo_mensalidade': '1',
    'date': {
        'dia': '17',
        'mes': '08',
        'ano': '2022',
        'valor': '150'
    }
}


def generate_bak_data():
    alunos = []

    aluno1 = atendente.create_entity(typeAluno=True, data=data)
    alunos.append(aluno1)
    aluno1.create_mensalidade(data.get('date'))

    aluno2 = atendente.create_entity(typeAluno=True, data=data1)
    aluno2.setSenha('3214')
    alunos.append(aluno2)
    aluno2.create_mensalidade(data1.get('date'))

    aluno3 = atendente.create_entity(typeAluno=True, data=data2)
    alunos.append(aluno3)
    aluno3.create_mensalidade(data2.get('date'))

    return alunos





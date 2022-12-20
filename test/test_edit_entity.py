from atendente import Atendente
from academia import Academia
from main import generate_bak_data

atendente = Atendente(nome='Ryan', senha='1708')
academia = Academia(nomeAcademia='GYM', endereco='Ryan Street Gym')

edit_data = {
    'nome': 'José',
    'cpf': '00000000000',
    'email': 'josezinho@gmail.com',
    'telefone': '4213452134',
    'tipo_mensalidade': '2',
    'date': {
        'dia': '02',
        'mes': '03',
        'ano': '2022',
        'valor': '150'
        },
    }

data = {
    'nome': 'Fabio',
    'cpf': '00000000000',
    'email': 'fabioofthenight@gmail.com',
    'telefone': '40028922',
    'tipo_mensalidade': '1',
    'date': {
        'dia': '17',
        'mes': '08',
        'ano': '2022',
        'valor': '150'
    }
}


def test_edit_entity():
    bank_data = generate_bak_data()
    aluno = atendente.create_entity(typeAluno=True, data=data)
    bank_data.append(aluno)
    res = atendente.edit_entity(cpf='00000000000', data=edit_data, bank_data=bank_data, aluno=aluno)
    for i in vars(res):
        assert i is not None


def test_edit_not_found():
    aluno = atendente.create_entity(typeAluno=True, data=data)
    res = atendente.edit_entity('9999999999', edit_data, generate_bak_data(), aluno=aluno )
    assert res is False
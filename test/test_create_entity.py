from atendente import Atendente

atendente = Atendente(nome='Ryan', senha='1708')

data = {
    'nome': 'João',
    'cpf': 123456789,
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
dt_nome_erro = {
    'cpf': '123456789',
    'email': 'joãozinho@gmail.com',
    'telefone': '40028922',
    'date': {
        'dia': '17',
        'mes': '08',
        'ano': '2022',
        'valor': '150'
    }
}

dt_cpf_erro = {
    'nome': 'João',
    'cpf': 'string',
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
error_data = {}


def test_create_aluno():
    res = atendente.create_entity(typeAluno=True, data=data)
    res.create_mensalidade(data=data.get('date'))
    for i in vars(res):
        assert i is not None


def test_create_personal():
    res = atendente.create_entity(typeAluno=False, data=data)
    temp = vars(res)
    for i in temp:
        assert temp[i] is not None


def test_create_atendente():
    atendente.create_entity(typeAluno='Atendente', data=data)
    assert atendente.nome is not None
    assert atendente.senha is not None


def test_error_create_entity():
    res = atendente.create_entity(typeAluno=True, data=error_data)
    assert res == 'ERRO, data não encontrada'


def test_error_cpf_create_entity():
    res = atendente.create_entity(typeAluno=True, data=dt_cpf_erro)
    assert res == 'ERRO, cpf invalido'


def test_error_nome_create_entity():
    res = atendente.create_entity(typeAluno=True, data=dt_nome_erro)
    assert res == 'ERRO, campos obrigatórios não são enviados'


def test_create_error_personal():
    res = atendente.create_entity(typeAluno=False, data=error_data)
    assert res == 'ERRO, data não encontrada'


def test_error_cpf_personal():
    res = atendente.create_entity(typeAluno=False, data=dt_cpf_erro)
    assert res == 'ERRO, cpf invalido'


def test_error_nome_personal():
    res = atendente.create_entity(typeAluno=False, data=dt_nome_erro)
    assert res == 'ERRO, campos obrigatórios não são enviados'

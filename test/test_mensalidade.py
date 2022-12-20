from atendente import Atendente

atendente = Atendente(nome='Ryan', senha='1708')

data_pago = {
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
data_pendente = {
    'nome': 'João',
    'cpf': '11111111111',
    'email': 'joãozinho@gmail.com',
    'telefone': '40028922',
    'tipo_mensalidade': '1',
    'date': {
        'dia': '17',
        'mes': '08',
        'ano': '2022',
        'valor': '10'
    }
}

data_error = {
    'nome': 'João',
    'cpf': '11111111111',
    'email': 'joãozinho@gmail.com',
    'telefone': '40028922',
    'tipo_mensalidade': '1',
    'date': {
        'dia': 'string',
        'mes': '08',
        'ano': '2022',
        'valor': '10'
    }
}


def test_create_mensalidade_pago():
    aluno1 = atendente.create_entity(typeAluno=True, data=data_pago)
    mensalidade_aluno = aluno1.create_mensalidade(data_pago.get('date'))
    status = vars(mensalidade_aluno).get('_status')
    assert status == 'PAGO'
    for i in vars(mensalidade_aluno):
        assert i is not None


def test_create_mensalidade_pendente():
    aluno1 = atendente.create_entity(typeAluno=True, data=data_pendente)
    mensalidade_aluno = aluno1.create_mensalidade(data_pendente.get('date'))
    status = vars(mensalidade_aluno).get('_status')
    assert status == 'PENDENTE'
    for i in vars(mensalidade_aluno):
        assert i is not None


def test_create_mensalidade_not_found():
    aluno1 = atendente.create_entity(typeAluno=True, data=data_pendente)
    res = aluno1.create_mensalidade(None)
    assert 'erro, data de pagamento não encontrada'


def test_create_mensalidade_erro_data():
    aluno1 = atendente.create_entity(typeAluno=True, data=data_error)
    res = aluno1.create_mensalidade(data_error.get('date'))
    assert res == 'erro, valor invalido'

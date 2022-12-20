from atendente import Atendente
from academia import Academia
from main import generate_bak_data

academia = Academia(nomeAcademia='GYM', endereco='Ryan Street Gym')
atendente = Atendente(nome='Ryan', senha='1708')

data = {
    'nome': 'João',
    'cpf': '123456789',
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
aluno = atendente.create_entity(typeAluno=True, data=data)


def test_search_um_aluno():
    bank = generate_bak_data()
    bank.append(aluno)
    res = atendente.search_um_aluno(aluno.cpf, bank)
    for i in res:
        assert i is not None


def test_search_alunos():
    bank = generate_bak_data()
    res = atendente.search_alunos('1', bank)
    for aluno in res:
        for i in vars(aluno):
            assert i is not None


def test_search_um_aluno_error():
    bank = generate_bak_data()
    res = atendente.search_um_aluno('00000000', bank)
    assert res is False


def test_search_alunos_error():
    bank = generate_bak_data()
    res = atendente.search_alunos('99', bank)
    assert res == 'Tipo de mensalidade não encontrado'

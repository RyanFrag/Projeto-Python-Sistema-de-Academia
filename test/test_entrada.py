from atendente import Atendente
from main import generate_bak_data
atendente = Atendente(nome='Ryan', senha='1708')


def test_entrada_sucesso():
    res = atendente.entrada('3214', generate_bak_data())
    assert res is True


def test_entrada_senha_not_found_erro():
    res = atendente.entrada('1234', generate_bak_data())
    assert res is False


def test_entrada_senha_invalida_erro():
    res = atendente.entrada('', generate_bak_data())
    assert res == 'ERRO, insira uma senha válida'


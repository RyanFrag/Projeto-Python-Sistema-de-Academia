

class Academia:
    def __init__(self, nomeAcademia, endereco):
        self.nomeAcademia = nomeAcademia
        self._endereco = endereco

    def getNomeAcademia(self):
        return self.nomeAcademia

    def setNomeAcademia(self, nomeAcademia):
        self.nomeAcademia = nomeAcademia

    def setEndereco(self, endereco):
        self._endereco = endereco

    def getEndereco(self):
        return self._endereco

    def setAlunos(self, aluno):
        self.atendente.alunos.append(aluno)


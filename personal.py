class Personal:
    def __init__(self, nome, cpf, senha):
        self.nomePersonal = nome
        self._cpfPersonal = cpf
        self._senha = senha

    def setPersonalNome(self, nome):
        self.nomePersonal = nome

    def setPersonalCpf(self, cpf):
        self._cpfPersonal = cpf

    def setPersonalSenha(self, senha):
        self._senha = senha

    @property
    def getNome(self):
        return self.nomePersonal

    @property
    def getCPF(self):
        return self._cpfPersonal

    @property
    def getSenha(self):
        return self._senha
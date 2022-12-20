from mensalidade import Mensalidade


class Aluno:
    def __init__(self,nome,telefone,email, cpf, tipo_mensalidade, senha):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self._cpf = cpf
        self.tipo_mensalidade = tipo_mensalidade
        self._senha = senha
        self.mensalidade = Mensalidade

    @property
    def Getnome(self):
        return self.nome

    @property
    def senha(self):
        return self._senha

    @property
    def cpf(self):
        return self._cpf

    def getSetTipoMensalidade(self):
        return self.tipo_mensalidade()

    def setNome(self, value):
        self.nome = value

    def setSenha(self, senha):
        self._senha = senha

    def setcpf(self, cpf):
        self._cpf = cpf

    def setEmail(self, email):
        self.email = email

    def setTelefone(self, telefone):
        self.telefone = telefone

    def set_tipo_mensalidade(self, tipo_mensalidade):
        self.tipo_mensalidade = tipo_mensalidade

    def create_mensalidade(self, data):
        if not data:
            return 'erro, data de pagamento não encontrada'
        for i in data:
            data[i] = str(data[i])
            if not data[i].isnumeric():
                return 'erro, valor invalido'
        mensalidade = self.mensalidade(mes=data.get('mes'), ano=data.get('ano'), dia=data.get('dia'),
                                  valor_pago=data.get('valor'))
        if mensalidade.check_mensalidade():
            mensalidade.setStatus('PAGO')
        else:
            mensalidade.setStatus('PENDENTE')
        return mensalidade

    def get_mensalidade(self):
        return self.mensalidade.getdata


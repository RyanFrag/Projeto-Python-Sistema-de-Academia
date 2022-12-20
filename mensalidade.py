class Mensalidade:
    def __init__(self, mes, ano, dia, valor_pago):
        self.mes = mes
        self.ano = ano
        self.dia = dia
        self._valor = '150'
        self.valor_pago = valor_pago
        self._status = None

    @property
    def getdata(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    @property
    def getStatus(self):
        return self._status

    @property
    def getValorPago(self):
        return self.valor_pago

    def setStatus(self, status):
        self._status = status

    def setValorPago(self, valor_pago):
        self.valor_pago = valor_pago

    def setAno(self, ano):
        self.ano = ano

    def setMes(self, mes):
        self.mes = mes

    def setDia(self, dia):
        self.dia = dia

    def setAluno(self, aluno):
        self.aluno = aluno

    def check_mensalidade(self):
        if self.valor_pago == self._valor:
            return True
        return False

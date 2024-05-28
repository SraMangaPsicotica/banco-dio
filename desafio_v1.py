from abc import ABC

class Transacao(ABC):

  def registrar(self, conta):
    self.conta = Conta


class Historico:
  def __init__(self, conta):
    self.conta = Conta
    self.operacoes = []
  
  def adicionar_transacao(self, transacao):
    self.transacao = Transacao
  pass
  

class Conta:
  def __init__(self):
    self.saldo = float
    self.numero = int
    self.agencia = str
    self.cliente = Cliente
    self.historico = Historico


  def nova_conta(self, cliente, numero):
    self.cliente = Cliente
    self.numero = int


class Cliente:
  def __init__(self,endereco):
    self.endereco = endereco
    self.contas = []

  def realizar_transacao(self, conta, transacao):
    transacao.registrar(conta)
  
  def adicionar_conta(self, conta):
    self.contas.append(conta)


class Saque(Transacao):
  def __init__(self, valor):
    self.valor = valor

  def registrar(self, conta):
    self.conta = Conta
    self.valor = f'Saque de {self.valor}'

class Deposito(Transacao):
  def __init__(self, valor):
    self.valor = valor

  def registrar(self, conta):
    self.conta = Conta
    self.valor = f'Depósito de {self.valor}'
    

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


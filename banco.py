menu = """
[1 Saque]

[2 Deposito]

[3 Extrato]

[4 Sair]
"""

saldo = 100
limite = 500
saques = 0
LIMITE_DE_SAQUES = 3
operacoes = []
while True:
  print('- '*10)
  opcao = input(menu)
  
  if opcao == '1':
    if saques < LIMITE_DE_SAQUES:
      print(f'Seu saldo: {saldo}')
      valor = float(input('Digite o valor do saque desejado: \n'))
  
      if valor > saldo:
        print('Saldo insuficiente')
  
      elif valor > limite:
        print('Valor acima do limite de saque')
  
      elif valor <= saldo:
        saldo -= valor
        print(f'Saque realizado com sucesso! Seu saldo atual é de {saldo}')
        saques += 1

        operacoes.append(f'Saque de {valor}')
    else:
      print('Você atingiu o limite de saques diários')


  
  elif opcao == '2':
    print(f'Seu saldo: {saldo}')
    valor = float(input('Digite o valor do deposito desejado: \n'))
    if valor > 0:
      saldo += valor
      print(f'Deposito realizado com sucesso! Seu saldo atual é de {saldo}')

      operacoes.append(f'Deposito de {valor}')
    else:
      print('Valor inválido')

  elif opcao == '3':
    print("Operações: \n")
    for i in operacoes:
      print(i)

  elif opcao == '4':
    print('- '*10)
    print('Atendimento encerrado.')
    break

  else:
    print('Opção inválida')
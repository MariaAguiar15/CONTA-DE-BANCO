"""
CONTA DE BANCO
"""

# titular = 'maria'
# numero = '0605'
# saldo = 1000
# limite = 3000

# conta = {'numero': 2012,
# 'titular': 'maria',
# 'saldo': 1000,
# 'limite': 3000
# }

# print(conta)


# def buscar_conta():
# pass
# conta = {'numero': 2012,
# 'titular': 'maria',
# 'saldo': 1000,
# 'limite': 3000
# }
# return conta
from typing import Dict, Any


def criar_conta(numero, titular, saldo, limite):
    conta = {
        'numero_conta': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite,
    }
    return conta


def depositar(numeroconta, valor):
    # conta['saldo'] = conta['saldo'] + valor
    numeroconta['saldo'] += valor


def sacar(numeroconta, valor):
    numeroconta['saldo'] = numeroconta['saldo'] - valor


def extrato(conta):
    print(f"numero{conta['numero_conta']}\nvalor atualizado: {conta['saldo']}")


conta = criar_conta(2012, 'maria', 1000, 3000)

print('saldo atual:', conta['saldo'])

depositar(conta, 150)
extrato(conta)

sacar(conta, 100)
extrato(conta)

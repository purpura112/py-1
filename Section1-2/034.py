# exercicio 18
saldoExistente = float(359.56)
saldoAdicional = float(input("Quanto você quer adicionar na conta? "))
faturaCartao = float(125.98)

saldoFinal = saldoExistente + saldoAdicional - faturaCartao
print("Você teve reduzido do seu saldo R$%.2f da fatura, seu novo saldo é de %.2f" %(faturaCartao, saldoFinal))
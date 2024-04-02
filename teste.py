qmaçãs = int(input("Quantas maçãs você comprou?: "))
if qmaçãs < 12:
    custo_total = qmaçãs * 0.30
else:
    custo_total = qmaçãs * 0.25

print(f"Total R${custo_total:.2f}")
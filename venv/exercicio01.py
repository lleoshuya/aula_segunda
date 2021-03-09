##Par ou impar

inicio = int(input("Digite o primeiro Número.:"))
fim = int(input("Digite o último Número......:"))
salto = int(input("Salto de..................:"))
for i in range (inicio, fim, salto):
    if(i%2==0):
        print(i, "Par")
    else:
        print(i, "Impar/Primo")

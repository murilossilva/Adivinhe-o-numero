import random
import math

menor = int(input("Digite o menor número possível: "))
maior = int(input("Digite o maior número possível: "))
 
x = random.randint(menor, maior)
chance = round(math.log(maior - menor +1, 2))

print("\nVocê tem", 
       chance,
      "chances para tentar acertar o número!\n")

i = 0
 
while i < chance:
    i = i + 1
 
    num = int(input("Adivinhe o número: "))
 
    if x == num:
        print("Parabéns você acertou o número em ",
              i, " tentativas!")
        break
    elif x > num:
        print("O número é maior!")
    elif x < num:
        print("O número é menor!")
 
if i >= chance:
    print("\nQue pena, você perdeu... O número era %d!!! =(" % x)
    print("\tMais sorte da próxima vez!")

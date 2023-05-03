# Jogo da bolinha nos 3 copos
b = float(input("Em qual copo está a bolinha? \n > "))
import random
s = random.randint(1,3)
print("A bolinha estava no copo", s, "!")
if s == b:
    print("Parabéns, você achou a bolinha!")

else:
    print("Infelizmente não foi dessa vez!")



import random

def tirardados():
    return random.randint(1,6) + random.randint(1,6)


puntuacion = {2 : 0, 3 : 0, 4: 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
expected = {2:2.78, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67, 8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}
for punto in range(0,1000):
    puntos = tirardados()
    puntuacion[puntos] += 1

print("Total\tSimulated\tExpected")
print("\t  Percent\t Percent")

for a in puntuacion:
    print("{:2d}\t{:8.2f}\t{:7.2f}".format(a, puntuacion[a]/1000 * 100, expected[a]))
    

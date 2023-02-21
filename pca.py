import numpy as np, random
from matplotlib import pyplot as plt

#dataset 1 
x1 = []
y1 = []

#dataset 2
x2 = []
y2 = []

#vytvoření datasetů s random hodnotami
for i in range(20):
    x1.append(random.randint(0,100))
    y1.append(random.randint(0,100))
    x2.append(random.randint(0,100))
    y2.append(random.randint(0,100))

#kovariační matice
matice_1 = np.cov(np.asarray([x1, y1]))
matice_2 = np.cov(np.asarray([x2, y2]))

#vlastní čísla a vektory
vl_cisla1, vl_vektor1 = np.linalg.eig(matice_1)
vl_cisla2, vl_vektor2 = np.linalg.eig(matice_2)

#výpočet variability 
variabilita_1 = (vl_cisla1[1] / (vl_cisla1[1] + vl_cisla1[0]) * 100)
variabilita_2 = (vl_cisla2[1] / (vl_cisla2[1] + vl_cisla2[0]) * 100)

print("DATASET 1:")
print(f"x: {x1}")
print(f"y: {y1} \n")
print(f"Matice: \n {matice_1}")
print(f"Vlastní čísla: {vl_cisla1} \n")
print(f"Vlastní vektory: \n {vl_vektor1}")
print(f"Variabilita: {round(variabilita_1, 2)} % \n")

print("DATASET 2:")
print(f"x: {x2}")
print(f"y: {y2} \n")
print(f"Matice: \n {matice_2}")
print(f"Vlastní čísla: {vl_cisla2} \n")
print(f"Vlastní vektory: \n {vl_vektor2}")
print(f"Variabilita: {round(variabilita_2, 2)} % \n")

plt.scatter(x1, y1, c = "cornflowerblue")
plt.title("dataset 1")
plt.show()

plt.scatter(x2, y2, c = "palevioletred")
plt.title("dataset 2")
plt.show()
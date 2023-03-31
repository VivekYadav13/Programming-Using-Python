'''
Write a program that computes the molecular weight of a carbohydrate (in grams per mole) based on the number of hydrogen, carbon, and oxygen atoms in the molecule. The program should prompt the user to enter the number of hydrogen atoms, the number of carbon atoms, and the number of oxygen atoms. The program then prints the total combined molecular weight of all the atoms based on these individual atom weights:
Atom | Weight (grams/mole)
H | 1.00794
C | 12.0107
O | 15.9994
For example, the molecular weight of water (H2O) is: 2(1.00794) + 15.9994 = 18.01528.
'''

C, H, O = 12.0107, 1.00794, 15.9994 # Weight of single atoms in grams/mole
c, h2o = int(input("Enter number of Carbon atoms: ")), int(input("Enter number of Water molecules: "))
print("General structure of Carbohydrate atom: (C)x(H20)y\nAs per entered data,\nCarbohydrate formula: C", c, "H", h2o*2, "O", h2o, "\nWeight of Carbohydrate molecule = ", C*c+H*h2o*2+O*h2o,  " grams/mole", sep='')

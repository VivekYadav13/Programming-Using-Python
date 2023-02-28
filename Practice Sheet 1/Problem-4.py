'''
Problem 4:
'''

C, H, O = 12.0107, 1.00794, 15.9994 # Weight of single atoms in grams/mole
c, h20 = int(input("Enter number of Carbon atoms: ")), int(input("Enter number of Water molecules: "))
print("General structure of Carbohydrate atom: (C)x(H20)y\nAs per entered data,\nCarbohydrate formula: C", c, "H", h20*2, "O", h20, "\nWeight of Carbohydrate molecule = ", C*c+H*h20*2+O*h20,  " grams/mole", sep='')

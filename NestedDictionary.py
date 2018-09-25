# Will Wagner
# IST303
# 9/23/2018

# Write a Python program to store the following information in a nested dictionary called nest_dict:
# Name 	Gender 	Favorite Animals
# Tonderai 	M 	Cat, Donkey
# Tariro 	F 	Cat, Dog, Antelope, Lion
# Tongai 	M 	Goat, Sparrow, Cat
# Tanaka 	F 	Orca, Owl, Tiger, Squirrel
# Tadiwa 	F 	Dog

# The program must also accomplish the following using for loop traversals of nest_dict:

#     Create a set called animal of all the favorite animals in the nested dictionary
#     Display a set called m_animal of favorite animals of all the males
#     Display a set called ex_f_animal of all the animals that appear more than once 
#       but only in female lists.



nest_dict = {   
    'Tonderai'  : {'Favorite Animals': ('Cat', 'Donkey'), 'Gender': 'M'},
    'Tariro'    : {'Favorite Animals': ('Cat', 'Dog', 'Antelope', 'Lion'), 'Gender': 'F'},
    'Tongai'    : {'Favorite Animals': ('Goat', 'Sparrow', 'Cat'), 'Gender': 'M'},
    'Tanaka'    : {'Favorite Animals': ('Orca', 'Owl', 'Tiger', 'Squirrel'), 'Gender': 'F'},
    'Tadiwa'    : {'Favorite Animals': ['Dog'], 'Gender': 'F'}
}

animals = set()   # <--- I used animals (plural) because of naming convention
m_animals = set()
f_animals = set()
ex_f_animals = set()


#  Create the Sets: animals, m_animals, and ex_f_animals
for name in nest_dict:
    for animal in nest_dict[name]['Favorite Animals']:

        if animal not in animals:
            animals.add(animal)

        if nest_dict[name]['Gender'] == "M":
            m_animals.add (animal)

        if nest_dict[name]['Gender'] == "F":
            if animal in f_animals:
                ex_f_animals.add (animal)
            if animal not in f_animals:
                f_animals.add(animal)
            

print ('Set of all favorite animals: ' + str(animals))
print ('Set of all favorite animals of the males: ' + str(m_animals))
print ('Set of all multiple favorite animals of females: ' + str(ex_f_animals))
    

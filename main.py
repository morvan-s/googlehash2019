import sys
from Resolver import Resolver

inputs = {
    "a" : "a_example",
    "b" : "b_lovely_landscapes",
    "c" : "c_memorable_moments",
    "d" : "d_pet_pictures",
    "e" : "e_shiny_selfies"
}

if len(sys.argv) < 2:
    print("Error : input name required !")
    sys.exit()

letter = sys.argv[1]

if letter not in inputs.keys():
    print("Error : wrong input name !")
    sys.exit()

Resolver(inputs[letter])

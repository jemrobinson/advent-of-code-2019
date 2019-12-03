#! /usr/bin/env python

# Fuel calculation
def get_fuel(mass):
    return (mass // 3) - 2

# Fuel calculation including the mass of the fuel itself
def get_compounded_fuel(mass):
    fuel_mass = get_fuel(mass)
    total_fuel_mass = 0
    while fuel_mass > 0:
        total_fuel_mass += fuel_mass
        fuel_mass = get_fuel(fuel_mass)
    return total_fuel_mass

# Use examples from problem page as tests
assert(get_fuel(12) == 2)
assert(get_fuel(14) == 2)
assert(get_fuel(1969) == 654)
assert(get_fuel(100756) == 33583)

# Calculate total fuel
with open("inputs/problem01-masses.txt", "r") as f_masses:
    masses = f_masses.readlines()
print("Simple: %i" % sum([get_fuel(int(m.strip())) for m in masses]))


# Use examples from problem page as tests
assert(get_compounded_fuel(14) == 2)
assert(get_compounded_fuel(1969) == 966)
assert(get_compounded_fuel(100756) == 50346)

# Calculate total fuel
print("Compounded: %i" % sum([get_compounded_fuel(int(m.strip())) for m in masses]))


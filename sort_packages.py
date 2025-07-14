# Objective

# Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

# Rules

# Sort the packages using the following criteria:

# - A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
# - A package is **heavy** when its mass is greater or equal to 20 kg.

# You must dispatch the packages in the following stacks:

# - **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
# - **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
# - **REJECTED**: packages that are **both** heavy and bulky are rejected.

# Implementation

# Implement the function **`sort(width, height, length, mass)`** (units are centimeters for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go.


def sort(width, height, length, mass) -> str: 
    if min(width, height, length, mass) <= 0:
        return "INVALID INPUT"
    
    isBulky = (width >= 150 or height >= 150 or length >= 150) or (width * height * length >= 1_000_000)
    isHeavy = (mass >= 20)
    
    
    if isBulky and isHeavy:
        return "REJECTED"
    elif isBulky or isHeavy:
        return "SPECIAL"
    else:
        return "STANDARD"
    
    
if __name__ == '__main__':
    print(sort(10, 10, 10, 10))
    print(sort(150, 10, 1, 10))
    print(sort(150, 10, 1, 20))
    print(sort(100, 100, 100, 15))
    print(sort(150, 10, 0, 20))
    print(sort(-10, 10, 10, 20))
    
import math

def vs_maintainability(V, G, L):
    """Count vs maintainability
    Inputs:
        V: is the Halstead Volume
        G: is the total Cyclomatic Complexity
        L: is the number of Source Lines of Code (SLOC)
    """
    sub = 171 - 5.2 * math.log(V) - 0.23 * G - 16.21 * math.log(L)
    mi = 0.100 * (sub / 171)
    return mi * 1000

def radon_maintainability(V, G, L, C):
    """Count radon maintainability
    Inputs:
        V: is the Halstead Volume
        G: is the total Cyclomatic Complexity
        L: is the number of Source Lines of Code (SLOC)
        C: s the percent of comment lines
    """
    sub = 171 - 5.2 * math.log(V) - 0.23 * G - 16.21 * math.log(L) + 50 * math.sin(math.sqrt(2.4 * math.radians(C)))
    mi = 0.100 * (sub / 171)
    return mi * 1000

def main():
    # Change V, G and L to get the desired value

    # V: is the Halstead Volume
    # G: is the total Cyclomatic Complexity
    # L: is the number of Source Lines of Code (SLOC)
    # C: is the percent of comment lines

    V = 0
    G = 0
    L = 0
    C = 0
    vs_mi = vs_maintainability(V, G, L)
    radon_mi = radon_maintainability(V, G, L, C)
    print("The vs maintability index of your code is: ", vs_mi) # 37.35
    print("The radon maintability index of your code is: ", radon_mi) # 64.53


if __name__ == "__main__":
    main()
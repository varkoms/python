import math

def espiral(lado):
    superior = (math.ceil(lado / 2))
    
    for i in range(superior):
        if (i == 0):
            print(("═"*(lado-1)) + "╗")
        else:
            print(("║"*(i-1)+ "╔" + "═"*(lado - (2*i)-1)) + "╗" + "║"*i)
    
    for i in range(superior, lado):
        print("║"*(lado-i-1)+ "╚" + "═"*((2*i)-lado) + "╝" + "║"*(lado-i-1))

# Pruebas 
espiral(3)
espiral(5)
espiral(10)
espiral(30)
espiral(50)
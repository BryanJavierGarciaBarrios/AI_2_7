import sympy as sp

# Definir símbolos
x, u = sp.symbols('x u')

# Definir las funciones
f = sp.sin(u)
g = u**2 + 1

# Combinar las funciones
composite_function = f.subs(u, g)

# Calcular la derivada
derivative = sp.diff(composite_function, x)

print("Función compuesta:", composite_function)
print("Derivada:", derivative)

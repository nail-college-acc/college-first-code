a : int = 8
b : int = 3

c : int = 8
d : int = 5

#region aritmetic
add = a + b #(+) add
min = a - b #(-) minus
tim = a * b #(*) times
dev = a / b #(/) devide
mod = a % b #(%) modulus
exp = a ** b #(**) exponent
dvf = a // b #(//) devision floor

#region print function
print("\nadd")
print(type(add))
print(add)
print("\nmin")
print(type(min))
print(min)
print("\ntim")
print(type(tim))
print(tim)
print("\ndev")
print(type(dev))
print(dev)
print("\nmod")
print(type(mod))
print(mod)
print("\nexp")
print(type(exp))
print(exp)
print("\ndvf")
print(type(dvf))
print(dvf)
#endregion

#endregion

#region assignment
print("\nassign")
temp = c #(=) assign
print(temp)

print("\nadd")
temp = c 
temp += d #(+=) add (temp = temp + d)
print(temp)

print("\nmin")
temp = c 
temp -= d #(-=) minus (temp = temp - d)
print(temp)

print("\ntim")
temp = c
temp *= d #(*=) times (temp = temp * d)
print(temp)

print("\ndev")
temp = c
temp /= d #(/=) devide (temp = temp / d)
print(temp)

print("\nmod")
temp = c
temp %= d #(%=) modulus (temp = temp % d)
print(temp)

print("\nexp")
temp = c
temp **= d #(**=) exponent (temp = temp ** d)
print(temp)

print("\ndvf")
temp = c
temp //= d #(//=) devision floor (temp = temp // d)
print(temp)
#endregion

#region comparison
print(f"\n{a} > {b}? ", a > b)

print(f"\n{a} < {b}? ", a < b)

print(f"\n{a} == {b}? ", a == b)

print(f"\n{a} <= {b}? ", a <= b)

print(f"\n{a} >= {b}? ", a >= b)

isItTrue : bool = c < d
print("hmmm, it is ", isItTrue)
#endregion
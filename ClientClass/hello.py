"""""
c=seed; a=multiplier; b=increment; m=modulus; n=desired array length; 

Modulus 'm' is the biggest Number 
- always positive
- The maximum number

The Seed, Incremet and Multiplier are less than the modulus and always positive

"""

def linearRandomGenerator(m, c, a, b, n):
    results = []
    if m > 0 and 0 < a < m and 0 <= b < m and 0 <= c < m:
        for i in range(n):
            c = ((a * c + b) % m) 
            results.append(c)

    return results

instance = linearRandomGenerator(20, 10, 1, 2, 100)

print(instance)
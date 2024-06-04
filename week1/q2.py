import math
def is_number(n):
    try:
        float(n)
        return True
    except:
        return False
    
assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))
print(is_number('n'))
#cau2 - B
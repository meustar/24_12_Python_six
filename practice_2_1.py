## 연산자

print(1 + 1) # 2
print(3 - 2) # 1
print(5 * 2) # 10
print(6 / 3) # 2

print("==="*20)

print(2 ** 3) # 2 ^ 3 = 8
print(5 % 3) # 나머지 구하기 2
print(10 % 3) # 1
print(5 // 3) # 몫 구하기 1
print(10 // 3) # 3

print("==="*20)

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print("==="*20)

print(3 == 3) # 같다 True
print(4 == 2) # False
print(3 + 4 == 7) # True

print("==="*20)

print(1 != 3) # True
print(not(1 != 3)) # False

print("==="*20)

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5))

print("==="*20)

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print("==="*20)

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

print("==="*20)

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

print("==="*20)

number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /=2 # 18
print(number)
number -= 2 # 16
print(number)

number %= 2 # 0
print(number)
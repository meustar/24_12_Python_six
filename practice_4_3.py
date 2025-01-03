## Tuple 
# List와 다르게 내용 변경&추가가 불가능 하나. 속도가 List 보다 빠르다.
# 변경되지 않는 상수에 대해서 사용한다.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# 추가하려고 할떄
# menu.add("생선까스")    # AttributeError: 'tuple' object has no attribute 'add'

# name = "김종국"
# age  = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
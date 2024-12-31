# 숫자형 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

#  boolean 자료형 (참/거짓)
print(5 > 10) # False
print(5 < 10) # True
print(True)
print(False)
print(not True) # False
print(not False) # True
print(not (5 > 10)) # True

# 변수
# 애완동물으 소개해 주세요.
name = "므갱이"
animal = "강아지"
age = 10
hobby = "낮잠"
is_adult = age >= 1

print("우리집 " + animal + " 이름은 " + name + "에요")
hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 " , age, "살이며, ", hobby,"을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
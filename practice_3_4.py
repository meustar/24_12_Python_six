## 문자열 포멧
# print("a" + "b")
# print("a", "b")

# 방법 1
print("=== 방법 1 ===")
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요" %"파이썬")
print("Apple 은 %c로 시작해요" %"A")
print("나는 %s살 일까요?" % 20)
print("나는 %s색과 %s색을 좋아해요. "%("파란", "빨간"))

# 방법 2
print("=== 방법 2 ===")
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))    # 연속적으로.
print("나는 {0}색과 {1}색을 좋아해요.".format("노란", "초록"))  # 순서대로 1
print("나는 {1}색과 {0}색을 좋아해요.".format("노란", "초록"))  # 순서대로 2

print("=== 방법 3 ===")
print("나는 {age}살 이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))  # format 안에서 변수 선언하여 활용.
print("나는 {age}살 이며, {color}색을 좋아해요.".format(color="빨간", age = 20))  # 순서 상관없이 정의한 변수에 대해서.

print("=== 방법 4 _ Python_v_3.6 이상 ===")
age = 33
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
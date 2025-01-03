# Dicionary (사전)
'''
  단어 : 뜻(정의)
  key : value
  * key에 대한 중복이 허용되지 않는다. 유일값.
'''

cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])   # 오류 발생후 프로그램 종류.
print(cabinet.get(5)) # 없는 값을 넣었을 경우 [5]와 다르게 get()은 None 값을 반환하고 다음으로 넘어간다.
print(cabinet.get(6, "사용가능"))
print("hi")

# 딕셔너리 값을 확인하는 방법
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로운 손님
print(cabinet)
cabinet["C-20"] = "조세호" # key를 만들고. value를 업데이트.
cabinet["A-3"] = "김종국"
print(cabinet)

# 간 손님.
del cabinet["A-3"]
print(cabinet)

# Key 들만 출력
print(cabinet.keys())   # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# Key, value 쌍으로 출력
print(cabinet.items())  # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet)  # {}
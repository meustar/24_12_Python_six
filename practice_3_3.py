## 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())                     # 대문자를 소문자로.
print(python.upper())                     # 소문자를 대문자로.
print(python[0].isupper())                # 0번째 글자가 대문자 인지 boolean으로 확인
print(len(python))                        # 문자열 전채 길이
print(python.replace("Python", "Java"))   # 문자열 바꾸기

index = python.index("n")                 # 첫번째 "n"을 찾기
print(index)
index = python.index("n", index + 1)      # 첫번째 "n" 다음 두번째 "n" 찾기
print(index)

print(python.find("Java"))                # 원하는 값이 없을때 -1 반환.
# print(python.index("Java"))               # index()에서 원하는 값이 없을때는 오류 발생. 프로그램 종료.

print(python.count("n"))                  # count()에서 "n"이 몇번 들어있는지 확인.
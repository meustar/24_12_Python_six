## 기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


# 같은 학교 같은 학년 같은 반 같은 수업 => 나이 같은 고유한 값을 제외하곤 동일해서 기본값 사용

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")
## 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)


# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")   # 이름 : 유재석    나이 : 20       Python Java C C++ C#
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")        # 이름 : 김태호    나이 : 25       Kotlin Swift  

# 가변인자 적용
def profile(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")   # 이름 : 유재석    나이 : 20       Python Java C C++ C# Javascript 
profile("김태호", 25, "Kotlin", "Swift")                                  # 이름 : 김태호    나이 : 25       Kotlin Swift 
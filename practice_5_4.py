# continue 와 break

# 반복문 내에서 사용 가능.

absent = [2, 5] # 결석
no_book = [7] # 책을 안가져왔음.
for student in range(1,11): # 1부터 10q번 까지의 학생
    if student in absent:
        continue    # 다음 반복으로 진행.
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break       # 반복문 종료.
    print("{0}, 책을 읽어봐".format(student))
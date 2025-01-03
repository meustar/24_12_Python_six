## Set (집합)
# 중복 X, 순서 X

my_set = {1,2,3,3,3}
print(my_set)   # {1, 2, 3} 중복 허용하지 않음.

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자.)
print(java & python)    # {'유재석'}
print(java.intersection(python))  # {'유재석'}

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)  # {'김태호', '양세형', '박명수', '유재석'}
print(java.union(python)) # {'김태호', '양세형', '박명수', '유재석'}

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)  # {'양세형', '김태호'}
print(java.difference(python))  # {'양세형', '김태호'}

# python 할 줄 아는 사람이 늘어남.
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java) # {'유재석', '양세형'}
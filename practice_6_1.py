## 함수


# 함수 정의
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 함수 호출
open_account()


# 파라미터를 이용한 함수 정의
def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)


# 출금
def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance
    
balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)


# 저녁에 수수료 지불하고 출금
def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))
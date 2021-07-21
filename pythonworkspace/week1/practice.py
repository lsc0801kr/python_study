from random import *
print("주사위 던지기")
rand = range(1, 7)
rand = list(rand)
shuffle(rand)

one = rand[0]
print("주사위 1: ", one)

shuffle(rand)

two = rand[0]
print("주사위 2: ", two)

print("실행할 연산의 종류를 입력하세요.")
print("1. 덧셈  2. 뺄셈  3. 곱셈  4. 나눗셈  5. 나머지 구하기")
num = int(input("연산종류: "))
while num == 0 or num > 5:
    print("1부터 5까지의 수를 입력하세요")
    num = int(input())


if num == 1:
    print("덧셈 결과 : ", one+two)
    new = one+two
elif num == 2:
    print("뺄셈 결과 : ", one-two)
    new = one-two
elif num == 3:
    print("곱셈 결과 : ", one*two)
    new = one*two
elif num == 4:
    print("나눗셈 결과 : ", one/two)
    new = one/two
else:
    print("나머지 구하기 결과 : ", one % two)
    new = one % two

print("별찍기")
hi = 0
while hi != new:
    hi += 1
    print("*"*hi)

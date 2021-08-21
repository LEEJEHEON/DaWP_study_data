
while True:
    num = input("실수를 입력하시오. (q,Q을 입력하시면 종료됩니다.)")
    if num =='q' or num=='Q':
        break
    try:
        value = 1/float(num)
    except ZeroDivisionError:
        print("0을 입력하시면 안됩니다.")
        continue
    print(value)
print("종료")
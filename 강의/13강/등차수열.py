inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력:')) 

valueN = 0
n = 1
while n <= inputN: # n이 N개가 되기 전까지 반복

    if n == 1:
        valueN = inputN1 # 첫번째 항의 값
        print('{}번째 항의 값: {}'.format(n, valueN))
        n += 1
        continue

    valueN += inputD #공차만큼 더해줌
    print('{}번째 항의 값: {}' .format(n, valueN))
    n +=1

print('{}번째 항의 값: {}' .format(inputN, valueN))
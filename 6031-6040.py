#6031 10진 정수 1개를 입력받아 유니코드 문자로 출력
c=int(input())
print(chr(c))

#6032 입력된 정수의 부호를 바꿔 출력
n=int(input())
print(-n)

#6033 문자 1개를 입력받아 그 다음 문자를 출력_영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'
n = input()
n = ord(n) + 1
print(chr(n))

#6034 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램
a,b=input().split()
c=int(a)-int(b)
print(c)

#6035 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성
f1,f2=input().split()
m = float(f1) * float(f2)
print(m)

#6036 단어와 반복 횟수를 입력받아 여러 번 출력
w, n = input().split()
print(w*int(n))

#6037 반복 횟수와 문장을 입력받아 여러 번 출력
n = input()
s = input()
print(int(n)*s)

#6038 정수 2개(a, b)를 입력받아 a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성
a,b=input().split()
c=int(a)**int(b)
print(c)

#6039 실수 2개(f1, f2)를 입력받아 f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성
a,b=input().split()
c=float(a)**float(b)
print(c)

#6040 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력
a,b=map(int,input().split())
print(a//b)

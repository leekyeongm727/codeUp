#6041 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력
a,b=map(int,input().split())
print(a%b)

#6042 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력
x=float(input())
print(format(x,".2f"))

#6043 실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림
f1,f2=map(float, input().split())
print(format(f1/f2,".3f"))

#6044 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산
x,y=map(int,input().split())
print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x%y)
print(format(x/y,".2f"))

#6045 정수 3개를 입력받아 합과 평균을 출력
a,b,c=map(int,input().split())
print(a+b+c,end=" ")
print(format((a+b+c)/3,".2f"))

#6046 정수 1개를 입력받아 2배 곱해 출력
n=int(input())
print(n<<1)

#6047 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력_0 <= a <= 10, 0 <= b <= 10
a,b=map(int,input().split())
print(a<<b)

#6048 두 정수(a, b)를 입력받아 a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램
a,b=map(int,input().split())
print(a<b)

#6049 두 정수(a, b)를 입력받아 a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램
a,b=map(int,input().split())
print(a==b)

#6050 두 정수(a, b)를 입력받아 b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램
a,b=map(int,input().split())
print(a<=b)
#6021 -> 알파벳과 숫자로 이루어진 단어 1개가 입력&입력받은 단어의 각 문자를 한 줄에 한 문자씩분리해 출력하기
s=input()
for i in range(5):
    print(s[i])

#6022 -> 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력하기
s=input()
print(s[0:2],end=' ')
print(s[2:4],end=' ')
print(s[4:])

#6023 -> 시:분:초 형식으로 시간이 입력될 때 분만 출력하기
time=list(input().split(':'))

#6024 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아 순서대로 붙여 출력하는 프로그램을 작성
w1,w2=input().split()
print(w1+w2)

#6025 정수 2개를 입력받아 합을 출력하는 프로그램을 작성
a,b=map(int,input().split())
print(a+b)

#6026 실수 2개를 입력받아 합을 출력하는 프로그램을 작성
a=float(input())
b=float(input())
print(a+b)

#6027 10진수를 입력받아 16진수(hexadecimal)로 출력
a=int(int(input()))
print('%x'%a)

#6028 10진수를 입력받아 16진수(hexadecimal)로 출력_대문자
a=int(int(input()))
print('%X'%a)

#6029 16진수를 입력받아 8진수(octal)로 출력
a=int(int(input(),16))
print('%o'%a)

#6030 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력
n=ord(input())
print(n)


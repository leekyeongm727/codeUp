#6051 두 정수(a, b)를 입력받아 a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력
a,b=map(int,input().split())
if a==b:
    print('False')
else:
    print('True')

#6052 입력된 값이 0이면 False, 0이 아니면 True 를 출력_ bool( ) 을 이용
n=int(input())
print(bool(n))
#6053 정수값이 입력될 때, 그 불 값을 반대로 출력
n=int(input())
n=bool(n)
print(not n)

#6054 2개의 정수값이 입력될 때, 그 불 값이 모두 True 일 때에만 True 를 출력
a,b=map(int, input().split())
a=bool(a)
b=bool(b)
if a==True and b==True:
    print('True')
else:
    print('False')
# =>print(bool(a) and bool(b))

#6055 2개의 정수값이 입력될 때, 그 불 값이 하나라도 True 일 때에만 True 를 출력
a,b=map(int, input().split())
print(bool(a) or bool(b))

#6056 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력
a,b=map(int, input().split())
c = bool(a)
d = bool(b)
print((c and (not d)) or ((not c) and d))

#6057 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력
a,b=map(int, input().split())
c = bool(a)
d = bool(b)
print((c and d) or ((not c) and (not d)))

#6058 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력
a,b=map(int, input().split())
c = bool(a)
d = bool(b)
print((not c) and (not d))

#6059 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력
a=int(input())
print(~a)

#6060 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력
a,b=map(int,input().split())
print(a&b)

# a = input().split()
# print(a)

# input() : 사용자에게서 입력을 받아 str 형으로 반환.
# split('/') : 파라미터를 기준으로 문자를 자른 후 리스트(배열)로 반환
# ex) a/b/c/d/e ==> split('/') --> [a, b, c, d, e]
# ex) a/b/c/d/e ==> split('c') --> [a/b/, /d/e]
# split(): ' ' 로 인식
a = input().split()
print(int(a[0]) + int(a[1]))  # A


"""

if condition:
    execute conditions
elif other conditions:
    execute conditions

"""

# print(sum(list(map(int, input().split()))))

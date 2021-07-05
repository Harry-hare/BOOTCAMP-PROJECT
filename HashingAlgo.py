import hashlib


def menu():
    print(" a. md5\n b. sha1\n c. sha256\n d. sha224\n")


def a1(hi):
    m = hashlib.md5(hi.encode())
    return m


def b1(hi):
    s1 = hashlib.sha1(hi.encode())
    return s1


def c1(hi):
    s2 = hashlib.sha256(hi.encode())
    return s2


def d1(hi):
    s3 = hashlib.sha224(hi.encode())
    return s3


print("Enter your String below:")
st = input()
menu()
print("Enter your choice {a,b,c,d}:")
ch = input()

if ch == 'a':
    out = a1(ch)
    print("The Hash value is :", end="")
    print(out.digest())


elif ch == 'b':
    out = b1(ch)
    print("The Hash value is :", end="")
    print(out.digest())


elif ch == 'c':
    out = c1(ch)
    print("The Hash value is :", end="")
    print(out.digest())


elif ch == 'd':
    out = d1(ch)
    print("The Hash value is :", end="")
    print(out.digest())


else:
    print("Invalid input!!!")

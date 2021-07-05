import hashlib

print("Enter your string :")
sh = input()
salt = 'f2wwa3j45k676b1'  # the salt value

st = sh + salt  # adds salt to the string entered by user

print("The salted value is :", end="")
print(st)  # prints the salted string
h = hashlib.md5(st.encode())

for i in range(20):
    print("++++", end="")

print("The salted hash value is : ", end="")
print(h.digest())  # prints the hash value of the salted string


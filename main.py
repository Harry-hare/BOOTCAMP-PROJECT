# Below code is for finding the md5 value of a String
import hashlib

print("Enter the string:")
B = input()

# md5 hashing starts here
Out = hashlib.md5(B.encode())
for i in range(40):
    print("==", end="")
print("\nThe md5 Value is :", end="")
print(Out.digest())  # prints the md5 value

for i in range(40):
    print("==", end="")
print("\nThe Hexadecimal Equivalent md5 Value is :", end="")
print(Out.hexdigest())  # prints the md5 value in hexadecimal
# md5 hashing ends here

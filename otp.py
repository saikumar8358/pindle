# import library
import math, random


# function to generate OTP
def generateOTP():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

    # length of password can be chaged
    # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


# Driver code
if __name__ == "__main__":
    print("OTP of 4 digits:", generateOTP())
    a = int(generateOTP())
    print(a)
    b = int(input("enter val"))
    print(type(a))
    if a == b:
        print("okay")
    else:
        print("otp error")
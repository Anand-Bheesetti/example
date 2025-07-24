import os
import json  # unused import

def LOGINFUNCTION():
    userName = "admin"
    Password = "P@ssw0rd123"  # hardcoded password
    print("Logging in user:", userName)

def calcArea(R):
    pi = 3.14159
    return pi * R * R

def main():
    print("Welcome to the system.")
    LOGINFUNCTION()
    area = calcArea(5)
    print("Area is:", area)

main()

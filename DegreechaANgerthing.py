import requests
import json

def weather(latitude, longitude):
    API=f"https://api.open-meteo.com/v1/forecast"
    params={}
    input("W")
def ctof():
    numberone=input("What number would you like to become Farenheit?")
    numberone=int(numberone)*1.8+32
    print("In Farenheit, it is...", numberone)
def ftoc():
    numbertwo=input("What number would you like to become Celsius?")
    numbertwo=int(numbertwo)-32
    numbertwo=int(numbertwo)*5/9
    print("In Celsius, it is...", numbertwo)
c=True
while c==True:
    choice=input("Celcius to Farenheit or Farenheit to Celcius?")
    if choice=="ftoc":
        ftoc()
        ask=input("Would you like another calculation?")
        if ask=="yes":
            pass
        else:
            c=False
    elif choice=="ctof":
        ctof()
        ask=input("Would you like another calculation?")
        if ask=="yes":
            pass
        else:
            c=False
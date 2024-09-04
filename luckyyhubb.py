print("LLUUCCKKYY HHUUBB")

print("made by luckyy")
      
print("Enter Password.")
password = input()
if password == "LKY123!":
    print("Access Granted.")
else:
    print("Access Denied")
    exit()
print("Enter Name.")
name = input()
print("Hello", name, "welcome to luckyy hub")
print("Choose what you want to use.")
print("1. Webhook Spammer")
program = input()
if program == "1":
    print("Webhook Spammer chosen.")
    print("Press Enter to start!")
    enter = input()
    import requests
    print("Script Made by luckyy DONT CLAIM!.")
    print('Put your Webhook here:')
    inputString = input()
    mUrl = inputString
    print('What text you want to be spammed?')
    inputString = input()
    efs = 0
    esfes = 1
    while efs != esfes:
       data = {"content": inputString}
       response = requests.post(mUrl, json=data)
       pass

import requests
city = input("Enter your city : ")
url = f'https://wttr.in/{city}'
try:
    data = requests.get(url)
    w = data.text
except:
    w = "Error!!!"
print(w)

print("See you again!:)")
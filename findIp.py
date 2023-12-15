from requests import get

ip = get("https://api.ipify.org").text
print("Cloning your ip address............")
print(ip)
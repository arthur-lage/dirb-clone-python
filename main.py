import requests

def search_for_directories(url):
    index = 0
    new_url = ""
    if list(url)[-1] == "/":
        new_url = url
    else:
        new_url = url + "/"
    
    default_url = new_url

    common_paths = ["admin", "login", "dashboard", "login.php", "livro"]

    for path in common_paths:
        new_url = default_url
        new_url += common_paths[index]
        response = requests.get(new_url)
        if response.status_code != 200:
            print(f"{new_url} is not a valid url! Status: {response.status_code}")
        else:
            print(f"{new_url} is a valid url! Status: {response.status_code}")
        index += 1

search_for_directories("https://tecnicasdeinvasao.com")    
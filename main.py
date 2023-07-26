import requests


def control(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_input = input("Enter Your Target website: ")

with open("wordList.txt", "r") as subdomain_list:
    for x in subdomain_list:
        x = x.strip()
        url ="http://"+ x +"." +target_input
        response = control(url)
        if response and response.status_code == 200:
            print("Found subdomain --->"+ url)


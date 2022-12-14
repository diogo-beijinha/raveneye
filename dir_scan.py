import requests

wordlist_path = input("Insert Wordlist Path: ")

def directory_scanning(ip_addr):
    with open(wordlist_path) as f:
        prefix_array = [line.split() for line in list(f)]
    prefix_not404_array = []
    for prefix in prefix_array:
        dir = requests.get(f'https://{ip_addr}/' + str(prefix))
        if dir.status_code != 404:
            prefix_not404_array.append(prefix)
    print(prefix_not404_array)

import requests

def directory_scanning(ip_addr):
    prefix_array = ["php", "PYTHON"]
    prefix_200_array = []
    for prefix in prefix_array:
        dir = requests.get(f'https://{ip_addr}/' + prefix)
        print(dir.status_code)
        if dir.status_code == 200:
            prefix_200_array.append(prefix)
    print(prefix_200_array)

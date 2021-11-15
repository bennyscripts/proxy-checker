import requests
import colorama

url = input("url to check on: ")
proxies = open('proxies.txt', 'r').readlines()
valid = []
invalid = []

for proxy in proxies:
    proxy = proxy.strip()

    try:
        response = requests.get(url, proxies={"http": f"socks4://{proxy}"}, timeout=2)
    except (requests.exceptions.ProxyError, requests.exceptions.SSLError, requests.exceptions.Timeout):
        print(f"{colorama.Fore.RED}[-]{colorama.Fore.WHITE} {proxy}")
        invalid.append(proxy)
    else:
        print(f"{colorama.Fore.GREEN}[+]{colorama.Fore.WHITE} {proxy}")
        valid.append(proxy)

print(" ")
print(f"{colorama.Fore.BLUE}[~]{colorama.Fore.WHITE} {len(valid)} valid proxies")
print(f"{colorama.Fore.BLUE}[~]{colorama.Fore.WHITE} {len(invalid)} invalid proxies")
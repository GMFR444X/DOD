import requests
import random
import sys

def load_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def visit_website(url, user_agents, proxies):
    user_agent = random.choice(user_agents)
    proxy = random.choice(proxies)

    headers = {'User-Agent': user_agent}
    proxy_dict = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}

    try:
        response = requests.get(url, headers=headers, proxies=proxy_dict, timeout=10)
        print(f"Visited {url} with {user_agent} through {proxy} - Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to visit {url} with {user_agent} through {proxy} - Error: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 web.py <url> <ua.txt> <proxy.txt>")
        return

    url = sys.argv[1]
    ua_file = sys.argv[2]
    proxy_file = sys.argv[3]

    user_agents = load_file(ua_file)
    proxies = load_file(proxy_file)

    visit_website(url, user_agents, proxies)

if __name__ == "__main__":
    main()
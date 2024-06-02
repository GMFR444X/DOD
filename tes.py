import requests
import random
import sys

def load_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def visit_website(url, user_agents):
    user_agent = random.choice(user_agents)
    headers = {'User-Agent': user_agent}

    try:
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        print(f"Visited {url} with {user_agent} - Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to visit {url} with {user_agent} - Error: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 web.py <url> <ua.txt>")
        return

    url = sys.argv[1]
    ua_file = sys.argv[2]

    user_agents = load_file(ua_file)

    visit_website(url, user_agents)

if __name__ == "__main__":
    main()
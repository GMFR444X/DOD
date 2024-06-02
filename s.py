import random
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def visit_website(url, user_agents, proxies):
    user_agent = random.choice(user_agents)
    proxy = random.choice(proxies)

    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument(f"--proxy-server=http://{proxy}")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    try:
        # Tunggu sampai halaman selesai dimuat
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Coba tutup iklan pop-up jika ada
        try:
            pop_up = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="close-button"]')))
            pop_up.click()
            print("Pop-up closed")
        except:
            print("No pop-up found")

        # Coba klik video jika ada
        try:
            video = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//video')))
            video.click()
            print("Video clicked")
        except:
            print("No video found")

        # Tambahkan tindakan lain sesuai kebutuhan
        # ...

    except Exception as e:
        print(f"Error visiting {url} with {user_agent} through {proxy}: {e}")

    finally:
        driver.quit()

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
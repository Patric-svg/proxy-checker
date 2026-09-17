import concurrent.futures
import requests

# Cloudflare trace endpoint
TEST_URL = "https://1.1.1.1/cdn-cgi/trace"
TIMEOUT = 8
MAX_THREADS = 15

def test_proxy(line):
    line = line.strip()
    if not line:
        return None
    parts = line.split(":")
    if len(parts) != 4:
        return None

    ip, port, user, pwd = parts
    
    # Test 1: SOCKS5
    try:
        socks_url = f"socks5h://{user}:{pwd}@{ip}:{port}"
        proxies = {"http": socks_url, "https": socks_url}
        resp = requests.get(TEST_URL, proxies=proxies, timeout=TIMEOUT)
        if resp.status_code in (200, 204):
            print(f"[+] WORKING (SOCKS5): {ip}:{port}")
            return f"{line} (SOCKS5)"
    except Exception:
        pass

    # Test 2: HTTP
    try:
        http_url = f"http://{user}:{pwd}@{ip}:{port}"
        proxies = {"http": http_url, "https": http_url}
        resp = requests.get(TEST_URL, proxies=proxies, timeout=TIMEOUT)
        if resp.status_code in (200, 204):
            print(f"[+] WORKING (HTTP): {ip}:{port}")
            return f"{line} (HTTP)"
    except Exception:
        pass

    return None

def main():
    with open("proxies.txt", "r") as f:
        proxy_list = [line.strip() for line in f if line.strip()]

    print(f"Testing {len(proxy_list)} proxies against Cloudflare...")
    working = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        results = executor.map(test_proxy, proxy_list)
        for res in results:
            if res:
                working.append(res)

    with open("working_proxies.txt", "w") as f:
        for p in working:
            f.write(p + "\n")

    print(f"\nFinished! Found {len(working)} working proxies.")

if __name__ == "__main__":
    main()
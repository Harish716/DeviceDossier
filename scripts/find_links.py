import urllib.request
import ssl
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for target in ["https://cdsco.gov.in", "https://cdscomdonline.gov.in"]:
    try:
        req = urllib.request.Request(target, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            links = []
            for a in soup.find_all('a', href=True):
                href = a['href']
                text = a.get_text(strip=True)
                full_url = urljoin(target, href)
                if any(k in href.lower() or k in text.lower() for k in ['device', 'classif', 'rule', 'mdr', 'notif', 'pdf', 'samd']):
                    links.append((text, full_url))
            print(f"=== Found {len(links)} relevant links on {target} ===")
            for text, url in links[:25]:
                print(f"[{text[:40]}] -> {url}")
    except Exception as e:
        print(f"Error checking {target}: {e}")

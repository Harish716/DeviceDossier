import urllib.request
import ssl
from bs4 import BeautifulSoup
from urllib.parse import urljoin

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

target_pages = [
    "https://cdsco.gov.in/opencms/opencms/en/Acts-and-rules/Medical-Devices-Rules/",
    "https://cdsco.gov.in/opencms/opencms/en/Medical-Device-Diagnostics/Medical-Device-Diagnostics/",
    "https://cdsco.gov.in/opencms/opencms/en/Medical-Device-Diagnostics/InVitro-Diagnostics/",
    "https://cdsco.gov.in/opencms/opencms/en/Acts-and-rules/Guidance-documents/",
    "https://cdsco.gov.in/opencms/opencms/en/Notifications/Public-Notices/",
]

all_pdfs = set()

for page in target_pages:
    try:
        req = urllib.request.Request(page, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            print(f"\n=== Target: {page} ===")
            sub_links = []
            for a in soup.find_all('a', href=True):
                href = a['href']
                text = a.get_text(strip=True)
                full = urljoin(page, href)
                if href.lower().endswith('.pdf') or '.pdf' in href.lower():
                    all_pdfs.add((text, full))
                    print(f"  [PDF] {text} -> {full}")
                elif any(x in href.lower() for x in ['classif', 'device', 'mdr', 'rule', 'notice']):
                    sub_links.append((text, full))
            print(f"  Found {len(sub_links)} other related sublinks")
            for t, l in sub_links[:10]:
                print(f"    Sub: {t} -> {l}")
    except Exception as e:
        print(f"Error {page}: {e}")

print(f"\nTOTAL UNIQUE PDFS FOUND: {len(all_pdfs)}")

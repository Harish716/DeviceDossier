import urllib.request
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    "https://cdsco.gov.in",
    "https://cdsco.gov.in/opencms/opencms/en/Medical-Device/Classification/",
    "https://cdsco.gov.in/opencms/export/system/modules/CDSCO.WEB/resources/downloads/Medical_Device/Medical%20Devices%20Rules,%202017.pdf",
    "https://cdscomdonline.gov.in",
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            print(f"URL: {url} -> Status: {resp.status}, Content-Length: {resp.headers.get('Content-Length')}, Content-Type: {resp.headers.get('Content-Type')}")
    except Exception as e:
        print(f"URL: {url} -> Error: {e}")

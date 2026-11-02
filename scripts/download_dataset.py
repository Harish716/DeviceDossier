"""Download script to fetch CDSCO medical device regulation documents for DeviceDossier."""
import ssl
import urllib.request
from pathlib import Path
from pypdf import PdfReader

DOCUMENTS = [
    (
        "md_software_guidance_mdr_2017.pdf",
        "https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/Guidance-document-on-Medical-Device-Software-under-MDR-2017.pdf",
        "Guidance Document on Medical Device Software under MDR-2017",
    ),
    (
        "faq_medical_device_rules_2017.pdf",
        "https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/MDfAq24.pdf",
        "FAQ on Medical Devices Rules, 2017",
    ),
    (
        "essential_principles_safety_performance.pdf",
        "https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/medical-device/Essentialprinciples25.pdf",
        "Essential Principles for Safety & Performance of Medical Devices",
    ),
    (
        "guidance_grouping_medical_devices.pdf",
        "https://cdsco.gov.in/opencms/export/sites/CDSCO_WEB/Pdf-documents/mdGroupingFAQ.pdf",
        "Medical Device Grouping Guideline with FAQ",
    ),
]


def download_dataset() -> None:
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    total_pages = 0
    for filename, url, title in DOCUMENTS:
        dest = raw_dir / filename
        if not dest.exists():
            print(f"Downloading {title} from {url}...")
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
                dest.write_bytes(resp.read())
        reader = PdfReader(str(dest))
        pages = len(reader.pages)
        total_pages += pages
        print(f"✓ {filename}: {pages} pages ({dest.stat().st_size:,} bytes)")

    print(f"\nTotal dataset pages collected: {total_pages}")


if __name__ == "__main__":
    download_dataset()

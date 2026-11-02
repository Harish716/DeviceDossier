# DeviceDossier

> AI-powered regulatory compliance assistant for Indian CDSCO Medical Devices Rules (MDR-2017) and Software as a Medical Device (SaMD) guidelines.

## Problem

Indian MedTech startups, medical device manufacturers, and regulatory affairs professionals struggle to navigate the complex web of Central Drugs Standard Control Organisation (CDSCO) Medical Devices Rules, 2017 (MDR-2017). Determining risk-based device classifications (Class A to D), identifying applicable licensing forms (e.g., MD-7, MD-8, MD-14), distinguishing wellness software from regulated Software as a Medical Device (SaMD), and verifying testing standards requires sifting through hundreds of pages of gazette notifications and FAQs. DeviceDossier changes this by providing an intelligent compliance assistant that delivers verifiable answers grounded with exact document and page citations.

## Who it is for

1. Regulatory Affairs (RA) Specialists and QA Managers at Indian medical technology manufacturers and health-tech AI startups in hubs like Bengaluru, Hyderabad, and Pune.
2. Biomedical Compliance Consultants preparing license applications and dossier submissions on the CDSCO Sugam portal.

## Signature feature

Multi-tier regulatory classification and licensing roadmap generator that maps product claims to CDSCO risk classes (Class A–D), required statutory forms, and QMS standards (ISO 13485 / IEC 62304) with exact page-level citations.

## Hardest problem (my interview story)

Resolving subtle boundary classifications for AI and standalone software (SaMD)—where differences in clinical intended use (e.g., wellness tracking vs. automated triage of intracranial hemorrhage) determine whether an algorithm is exempt or requires Class C/D central licensing with mandatory clinical performance evaluations—without hallucinating regulatory requirements.

## Dataset

| Source | Link | Documents | Pages | Licence / terms |
| ------ | ---- | --------- | ----- | --------------- |
| CDSCO Medical Devices Division | https://cdsco.gov.in | 4 | 165 | Open Government Data / Public Domain (Govt. of India) |


## 10 real questions

See [docs/QUESTIONS.md](docs/QUESTIONS.md).

## Run it

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env                                 # Windows: copy .env.example .env
uvicorn app.main:app --reload
curl localhost:8000/health
```

## Live link

<Added in Week 2>

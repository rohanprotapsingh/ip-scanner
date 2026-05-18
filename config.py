# -*- coding: utf-8 -*-
AKAMAI_RANGES = [
    "23.32.0.0/16", "23.64.0.0/14", "23.192.0.0/11",
    "104.64.0.0/10", "184.24.0.0/13", "184.50.0.0/15",
    "184.84.0.0/14", "2.16.0.0/13", "95.100.0.0/15",
    "92.122.0.0/15",
]

FASTLY_RANGES = [
    "151.101.0.0/16", "157.52.64.0/18", "167.82.0.0/17",
    "167.82.128.0/20", "167.82.160.0/20", "167.82.224.0/20",
    "172.111.64.0/18", "185.31.16.0/22", "199.27.72.0/21",
    "203.57.145.0/24",
]

OPERATORS = {
    "none": {"name": "No Operator (Direct)", "dns": []},
    "mci": {"name": "Hamrah-e Aval (MCI)", "dns": ["10.202.10.10"]},
    "irancell": {"name": "Irancell (MTN)", "dns": ["10.202.10.10"]},
    "rightel": {"name": "Rightel", "dns": []},
    "samantel": {"name": "Samantel", "dns": []},
    "mokhaberat": {"name": "Mokhaberat (TCI)", "dns": ["10.202.10.10"]},
    "shatel": {"name": "Shatel", "dns": ["85.15.1.14"]},
    "shatel_mobile": {"name": "Shatel Mobile", "dns": ["85.15.1.14"]},
    "aptel": {"name": "Aptel", "dns": []},
    "asiatech": {"name": "Asiatech", "dns": ["194.36.174.161"]},
    "pishgaman": {"name": "Pishgaman", "dns": []},
}

TELEGRAM_ENABLED = True
DEFAULT_PORTS = [443, 80]
DEFAULT_THREADS = 200
DEFAULT_TIMEOUT = 1.5
MAX_THREADS = 600
SERVER_PORT = 9000

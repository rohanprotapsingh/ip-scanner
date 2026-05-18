# -*- coding: utf-8 -*-
import ipaddress


def parse_ip_input(text):
    ips = []
    text = text.strip()
    if not text or text.startswith('#'):
        return ips
    if '/' in text:
        try:
            net = ipaddress.IPv4Network(text, strict=False)
            for ip in net.hosts():
                ips.append(str(ip))
        except ValueError:
            pass
        return ips
    if '-' in text:
        parts = text.split('-', 1)
        s = parts[0].strip()
        e = parts[1].strip()
        if '.' in e:
            try:
                si = int(ipaddress.IPv4Address(s))
                ei = int(ipaddress.IPv4Address(e))
                for x in range(si, ei + 1):
                    ips.append(str(ipaddress.IPv4Address(x)))
            except ValueError:
                pass
        else:
            try:
                bp = s.split('.')
                sl = int(bp[3])
                el = int(e)
                base = '.'.join(bp[:3])
                for i in range(sl, el + 1):
                    ips.append("{}.{}".format(base, i))
            except (ValueError, IndexError):
                pass
        return ips
    try:
        ipaddress.IPv4Address(text)
        ips.append(text)
    except ValueError:
        pass
    return ips


def unique_ips(ips):
    seen = set()
    out = []
    for ip in ips:
        if ip not in seen:
            seen.add(ip)
            out.append(ip)
    return out


def detect_cdn(server_header):
    s = server_header.lower()
    if 'akamai' in s:
        return 'Akamai'
    if 'fastly' in s or 'varnish' in s:
        return 'Fastly'
    if 'cloudflare' in s:
        return 'Cloudflare'
    if 'nginx' in s:
        return 'Nginx'
    if 'apache' in s:
        return 'Apache'
    if server_header:
        return server_header[:15]
    return 'Unknown'

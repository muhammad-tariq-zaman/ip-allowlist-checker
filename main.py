"""Check whether IP addresses are inside any CIDR range in an allowlist file.

Usage: python3 main.py allowlist.txt 203.0.113.5 10.0.0.9
"""
import argparse
import ipaddress
import sys


def load_allowlist(text):
    nets = []
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            nets.append(ipaddress.ip_network(line, strict=False))
    return nets


def allowed(nets, ip):
    addr = ipaddress.ip_address(ip)
    return any(addr.version == n.version and addr in n for n in nets)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("allowlist", help="File with one CIDR per line")
    parser.add_argument("ips", nargs="+", help="IP addresses to check")
    args = parser.parse_args(argv)
    with open(args.allowlist, encoding="utf-8") as f:
        nets = load_allowlist(f.read())
    for ip in args.ips:
        print(f"{ip}: {'ALLOWED' if allowed(nets, ip) else 'DENIED'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

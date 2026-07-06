#!/usr/bin/env python3
"""
port_scanner.py — Simple TCP port scanner
Author: Amirmohammad Alipour
"""

import socket
import argparse
from datetime import datetime


def scan_port(target, port, timeout=0.5):
    """Prova la connessione a una singola porta. True se aperta."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((target, port))
    sock.close()
    return result == 0


def scan_range(target, start_port, end_port):
    """Scansiona un range di porte e stampa quelle aperte."""
    print(f"\n[*] Target: {target}")
    print(f"[*] Port range: {start_port}-{end_port}")
    print(f"[*] Avviato alle: {datetime.now().strftime('%H:%M:%S')}\n")

    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"[+] Porta {port} APERTA")
            open_ports.append(port)

    print(f"\n[*] Scan completato — {len(open_ports)} porta/e aperta/e.")
    return open_ports


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("target", help="IP o hostname del bersaglio")
    parser.add_argument("-p", "--ports", default="1-1024",
                         help="Range porte da scansionare (default: 1-1024)")
    args = parser.parse_args()

    start, end = map(int, args.ports.split("-"))
    scan_range(args.target, start, end)

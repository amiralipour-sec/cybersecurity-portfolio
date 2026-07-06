#!/usr/bin/env python3
"""
banner_grabber.py — Grabs service banners from a target host/port
Author: Amirmohammad Alipour
"""

import socket
import argparse


def grab_banner(target, porta, timeout=5):
    """Si connette e prova a leggere il banner del servizio."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((target, porta))
        sock.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        banner = sock.recv(1024)
        sock.close()
        return banner
    except Exception as errore:
        return f"nessun banner disponibile ({errore})"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple banner grabber")
    parser.add_argument("target", help="IP o hostname del bersaglio")
    parser.add_argument("port", type=int, help="Porta da interrogare")
    args = parser.parse_args()

    risultato = grab_banner(args.target, args.port)
    print(risultato)

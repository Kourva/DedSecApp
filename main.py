#!/usr/bin/env python3
"""DEDSEC // TERMINAL - Kali/sqlmap style animation. EVERYTHING IS ."""

import hashlib
import os
import random
import re
import shutil
import sys
import time
from datetime import datetime

os.system("")  # enable ANSI on Windows

# ---------- ANSI colors ----------
R = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GRN = "\033[92m"
YEL = "\033[93m"
BLU = "\033[94m"
MAG = "\033[95m"
CYN = "\033[96m"
WHT = "\033[97m"

FAST = "--fast" in sys.argv
LOOP = "--loop" in sys.argv

# ---------- Skull ASCII art (original, untouched) ----------
SKULL_INICIO = """\
[red]⠀⠀⣿⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⣸⡏⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[/red]
[red]⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀ ⡰⠋⢙⣿⣦⡀⠀⠀⠀⠀⠀[/red]
[red]⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣦⣮⣤⡀⣸⣿⣿⣿⣆⠀⠀⠀⠀[/red]
[red]⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⣿⢟⣫⠟⠋⠀⠀⠀⠀[/red]
[red]⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣷⣷⣿⡁⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢹⣿⣿⣧⣿⣿⣆⡹⣖      [/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣤⣿⣿⣿⡟⠹⣿⣿⣿⣿⣷⡀   [/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⣿⠏⢧⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠈⢳⡀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⢳[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀[/red]
[red]⠀⠀⠀⠀⠀⠀⠀⠛⠻⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⠏⠀⠀⠀⠀⠀⠀[/red]"""

# rich-style tags -> ANSI (lets us keep the art exactly as written)
TAGS = {"red": RED}
TAG_RE = re.compile(r"\[(red)\](.*?)\[/\1\]")


def rich_to_ansi(line):
    return TAG_RE.sub(lambda m: f"{TAGS[m.group(1)]}{m.group(2)}{R}", line)


def wait(t):
    time.sleep(t / 3 if FAST else t)


def out(s="", end="\n"):
    sys.stdout.write(s + end)
    sys.stdout.flush()


def clear():
    out("\033[2J\033[H", end="")


# ---------- sqlmap-style logs ----------
LEVELS = {
    "INFO": GRN,
    "WARNING": YEL,
    "CRITICAL": RED,
    "DEBUG": BLU,
    "PAYLOAD": MAG,
}


def log(level, msg, delay=0.15):
    ts = datetime.now().strftime("%H:%M:%S")
    c = LEVELS.get(level, GRN)
    out(f"[{WHT}{ts}{R}] [{c}{BOLD}{level}{R}] {msg}")
    wait(delay + random.uniform(0, delay))


def log_ok(msg):
    log("INFO", f"{GRN}{msg}{R}")


# ---------- Skull + banner ----------
def show_skull():
    pad = " " * 4
    for line in SKULL_INICIO.splitlines():
        out(pad + rich_to_ansi(line))
        wait(0.06)
    out()


BANNER = r"""
   ____  _____ ____  ____  _____ ____
  |  _ \| ____|  _ \/ ___|| ____/ ___|
  | | | |  _| | | | \___ \|  _|| |
  | |_| | |___| |_| |___) | |__| |___
  |____/|_____|____/|____/|_____\____|
"""


def banner():
    out(CYN + BOLD + BANNER + R)
    out(f"{WHT}        {{1.0.{random.randint(1, 99)}#simulation}}{R}")
    out(f"{BLU}        https://dedsec.local{R}\n")
    out(f"{YEL}[!] notice: this is a visual SIMULATION. It performs no real attacks LOL{R}\n")
    wait(0.5)


# ---------- Matrix rain (ASCII only) ----------
def matrix_rain(seconds=2.5):
    cols = shutil.get_terminal_size((100, 30)).columns
    chars = "01$#@%&*<>/\\|ABCDEF0123456789"
    end = time.time() + (seconds / 3 if FAST else seconds)
    drops = [0] * cols
    while time.time() < end:
        line = ""
        for i in range(cols):
            if random.random() < 0.06:
                drops[i] = random.randint(4, 12)
            if drops[i] > 0:
                c = WHT if drops[i] > 10 else GRN
                line += f"{c}{random.choice(chars)}{R}"
                drops[i] -= 1
            else:
                line += " "
        out(line)
        time.sleep(0.03)
    clear()


# ---------- Progress bars ----------
# style -> (filled char, empty char, head char)
STYLES = {
    "block": ("█", "░", ""),
    "hash": ("#", "-", ""),
    "arrow": ("=", ".", ">"),
    "dots": ("●", "○", ""),
    "slash": ("/", " ", ""),
}


def make_bar(frac, steps, style):
    fill, empty, head = STYLES[style]
    n = int(frac * steps)
    if head and n < steps:
        return fill * n + head + empty * (steps - n - 1)
    return fill * n + empty * (steps - n)


def progress(label, duration=1.5, color=GRN, style="block", steps=40, stalls=True):
    """Single bar that fills in ~`duration` seconds (with random jitter/stalls)."""
    for i in range(steps + 1):
        pct = int(i / steps * 100)
        bar = make_bar(i / steps, steps, style)
        out(f"\r{CYN}{label:<28}{R} [{color}{bar}{R}] {WHT}{pct:3d}%{R}", end="")
        step_t = duration / steps * random.uniform(0.4, 1.6)
        if stalls and random.random() < 0.05:
            step_t += duration * 0.05  # brief "hang"
        wait(step_t)
    out()


def multi_progress(tasks, steps=30):
    """Several bars running in parallel, each with its own duration.
    tasks: list of (label, duration_seconds, color, style)"""
    tick = 0.05
    state = [0.0] * len(tasks)
    scale = 3 if FAST else 1
    for _ in tasks:
        out()
    while any(s < 1 for s in state):
        out(f"\033[{len(tasks)}A", end="")
        for i, (label, dur, color, style) in enumerate(tasks):
            if state[i] < 1:
                state[i] = min(1.0, state[i] + tick * scale / dur * random.uniform(0.5, 1.5))
            done = state[i] >= 1
            bar = make_bar(state[i], steps, style)
            tag = f"{GRN}DONE{R}" if done else f"{WHT}{int(state[i] * 100):3d}%{R}"
            out(f"\r\033[K{CYN}{label:<22}{R} [{color}{bar}{R}] {tag}")
        time.sleep(tick)


def spinner(label, seconds=1.5):
    frames = "|/-\\"
    end = time.time() + (seconds / 3 if FAST else seconds)
    i = 0
    while time.time() < end:
        out(f"\r{YEL}[{frames[i % 4]}]{R} {label}", end="")
        time.sleep(0.08)
        i += 1
    out(f"\r{GRN}[+]{R} {label} {GRN}OK{R}   ")


# ---------- Fake data ----------
def fake_ip():
    return f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(2, 254)}"


def fake_hash(word):
    return hashlib.md5(word.encode()).hexdigest()


SERVICES = [
    (22, "ssh", "OpenSSH 8.9p1"),
    (53, "domain", "dnsmasq 2.86"),
    (80, "http", "nginx 1.22.1"),
    (443, "https", "nginx 1.22.1"),
    (3306, "mysql", "MySQL 8.0.33"),
    (8080, "http-proxy", "Apache Tomcat"),
    (5432, "postgresql", "PostgreSQL 15"),
    (21, "ftp", "vsftpd 3.0.5"),
]


def nmap_scan(target):
    log("INFO", f"starting  port scan on {CYN}{target}{R}")
    progress("SYN scan", duration=2.5, color=CYN, style="block")
    ports = sorted(random.sample(SERVICES, random.randint(3, 6)))
    out(f"\n{WHT}PORT       STATE  SERVICE      VERSION{R}")
    for port, svc, ver in ports:
        out(f"{GRN}{str(port) + '/tcp':<10} open   {svc:<12} {ver}{R}")
        wait(0.2)
    out()
    progress("service fingerprinting", duration=1.2, color=YEL, style="hash")
    out()
    return ports


def injection_tests():
    tests = [
        "boolean-based blind",
        "error-based",
        "time-based blind",
        "UNION query",
        "stacked queries",
    ]
    log("INFO", "testing  GET parameter 'id'")
    for t in tests:
        log("PAYLOAD", f"testing '{t}'", 0.25)
        if random.random() < 0.45:
            log("WARNING", f"parameter 'id' appears to be {YEL}vulnerable{R} to '{t}' ")
    log_ok("parameter 'id' is 'injectable' ")
    out()


def dump():
    users = ["admin", "root", "ghost", "Zoey", "trinity", "owner", "operator", "guest"]
    words = ["password", "letmein", "hunter2", "qwerty", "dragon", "shadow", "welcome"]
    rows = random.sample(users, 5)
    out(f"{WHT}Database: dedsec_sim\nTable: users\n[{len(rows)} entries]{R}")
    line = "+----+------------+----------------------------------+"
    out(CYN + line + R)
    out(f"{CYN}|{R} {WHT}id{R} {CYN}|{R} {WHT}username{R}   {CYN}|{R} {WHT}password (md5){R}                   {CYN}|{R}")
    out(CYN + line + R)
    for i, u in enumerate(rows, 1):
        h = fake_hash(random.choice(words) + str(random.randint(0, 999)))
        out(f"{CYN}|{R} {i:<2} {CYN}|{R} {GRN}{u:<10}{R} {CYN}|{R} {YEL}{h}{R} {CYN}|{R}")
        wait(0.25)
    out(CYN + line + R + "\n")


def crack_sim():
    log("INFO", "starting  hash cracking")
    for _ in range(18):
        cand = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=random.randint(5, 9)))
        out(f"\r{DIM}{GRN}[trying] {cand:<12} -> {fake_hash(cand)}{R}", end="")
        wait(0.06)
    out()
    log_ok("3/5 hashes 'recovered'")


def access_granted():
    out()
    out(f"{GRN}{BOLD}╔══════════════════════════════════════╗{R}")
    out(f"{GRN}{BOLD}║             ACCESS GRANTED           ║{R}")
    out(f"{GRN}{BOLD}╚══════════════════════════════════════╝{R}\n")


def random_stream(n=25):
    """Random log stream, like the original app."""
    msgs = [
        ("INFO", "Encryption module initialized"),
        ("INFO", "Establishing secure sandbox..."),
        ("DEBUG", "Memory allocation: OK"),
        ("DEBUG", " packets received"),
        ("WARNING", "Anomaly detected in sample dataset"),
        ("INFO", "Firewall status: ACTIVE"),
        ("INFO", f"Session ID: {random.randint(10**7, 10**8)}"),
        ("DEBUG", f"Latency to node: {random.randint(8, 120)}ms"),
        ("CRITICAL", "Intrusion signature matched "),
        ("INFO", "Traffic running..."),
    ]
    for _ in range(n):
        lvl, m = random.choice(msgs)
        log(lvl, m, 0.08)


def run_once():
    target = fake_ip()
    show_skull()
    banner()
    log("INFO", "DEDSEC TERMINAL v1.0 ")
    log("INFO", f"target: {CYN}http://{target}/index.php?id=1{R}")
    spinner("resolving host ()")
    spinner("loading modules")
    progress("loading payload database", duration=1.0, color=MAG, style="hash")
    out()
    nmap_scan(target)
    injection_tests()
    log("INFO", "launching parallel modules")
    multi_progress([
        ("session brute-force", 2.0, GRN, "block"),
        ("parameter fuzzing", 3.5, CYN, "arrow"),
        ("schema enumeration", 5.0, YEL, "dots"),
        ("blob decryption", 7.0, MAG, "slash"),
    ])
    out()
    log("INFO", "enumerating databases")
    out(f"{GRN}available databases [3]:\n[*] dedsec_sim\n[*] information_schema\n[*] mysql{R}\n")
    wait(0.4)
    dump()
    crack_sim()
    progress("exfiltrating data", duration=5.0, color=RED, style="arrow")
    progress("covering tracks", duration=0.8, color=BLU, style="dots", steps=30)
    access_granted()
    random_stream()
    log("INFO", f"session saved to {CYN}/tmp/dedsec/{target}/session.sqlite{R}")
    ("INFO", "simulation finished at: "),log


def main():
    try:
        clear()
        while True:
            run_once()
            if not LOOP:
                break
            wait(2)
            clear()
    except KeyboardInterrupt:
        out(f"\n{RED}[!] interrupted by user{R}")


if __name__ == "__main__":
    main()
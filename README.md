# Active_Deception_Vaccine
# 💉 VAXBOX v4.0: Next-Gen Malware Vaccine & Cyber Deception Tool

VAXBOX is an advanced pro-active defense tool developed in Python for Linux (Kali Linux Cores). It implements **Cyber Deception** and **Hardware Gaslighting** to trick advanced malware into self-destruction by spoofing multi-layered sandbox environments and anti-analysis indicators (IoCs).

Developed during the **Cybercrimes and Digital Forensics Bootcamp** at **Tuwaiq Academy 💜**.

---

## 🚀 Core Features

- **Module 1: Vaccine Activation:** Injects static artifacts, dynamic ghost processes (`/tmp/tcpdump`), and a comprehensive Threat-Intelligence Mutex Array into Shared Memory (`/dev/shm`).
- **Module 2: Real-time Status Check:** Queries the kernel and file system to audit all active deception traps.
- **Module 3: Forensic Audit Report:** Compiles a full report mapped with live PIDs and timestamps, dedicated to DFIR (Digital Forensics & Incident Response) analysts.
- **Module 4: Secure Rollback & Purge:** Cleanly detaches and completely erases all environment modifications with zero resource leaks.

---

## 🎨 Tool Architecture & Deception Mechanism

Malware in 2026 relies heavily on environment checking (Anti-Sandbox). VAXBOX uses **Reverse Psychology**:
1. It simulates an environment under heavy network monitoring.
2. It claims mutex locks of active ransomware/stealers (e.g., WannaCry, Lumma Stealer).
3. It emulates restricted hardware capability (1 Core CPU / 1.75 GB RAM) through user-space gaslighting.
4. Result: The malware code halts and triggers its own **Self-Destruction module** without damaging the host system.

---

## 🛠️ Installation & Usage Instructions

### Prerequisites
VAXBOX requires **ROOT** privileges because it interacts directly with OS Shared Memory and Kernel process mapping.

```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/VAXBOX.git](https://github.com/YOUR_USERNAME/VAXBOX.git)

# Navigate to the tool directory
cd VAXBOX

# Run VAXBOX with root privileges
sudo python3 vaxbox.py

# 💉 Active Deception Vaccine (VAXBOX)

An elegant, lightweight proactive active-defense tool developed in Python for Linux environments (Kali Linux Cores). It implements core concepts of **Cyber Deception** and **Hardware Gaslighting** to trick sophisticated anti-analysis malware into automatic self-destruction. 

This project explores defensive reverse-psychology, demonstrating how simple Command Line Interface (CLI) tools can effectively manipulate system indicators to neutralize threats before they execute.

---

## 💡 What is an Active Deception Vaccine?

Instead of traditional reactive defense (chasing malware after infection), this project utilizes **Reverse Engineering against Malware Logic**. Modern malware contains sophisticated "Anti-Sandbox" modules to evade analysis. **Active Deception Vaccine** manipulates the environment by injecting multi-layered deceptive artifacts, forcing the malware to believe it is being monitored inside a high-security sandbox. As a result, the malware triggers its own **self-destruction phase** to protect its command-and-control (C2) servers.

---

## 🛠️ Built With & Used Tools

This project utilizes native system APIs and network utility suites to maintain a zero-dependency footprint:
* **Python 3:** Core logic architecture and CLI administration menu.
* **Ncat / Netcat:** Network utility engine used to host the external attacker listener session.

---

## ⚙️ Installation & Deployment

To deploy the vaccine or inspect the simulation files, clone the repository and navigate to the root directory:

```bash
# Clone the repository
git clone [https://github.com/Shooq-10/Active_Deception_Vaccine.git](https://github.com/Shooq-10/Active_Deception_Vaccine.git)

# Navigate to the tool directory
cd Active_Deception_Vaccine

# Run the Vaccine Control Panel with root privileges
sudo python3 vaxbox.py

```

> 💡 **Note:** Both the core defense utility (`vaxbox.py`) and the pre-built target verification Trojan (`kittens.py`) are pre-packaged within this repository. No external scripts creation is required.

---

## 🚀 Core Modules & Features

* **Module 1: Activate Vaccine (Multi-Layered Injection):**
* **Static Artifacts:** Injects fake sandbox directories (`/home/sandbox_user/.cuckoo`) and VirtualBox configurations (`/etc/modprobe.d/vboxguest.conf`).
* **Ghost Process:** Deploys a persistent background process masquerading as an intensive network sniffer (`/tmp/tcpdump`).
* **Threat-Intelligence Mutex Array:** Injects locked POSIX semaphores/mutexes into Shared Memory matching active malware families (WannaCry, Lumma Stealer, CobaltStrike).
* **Hardware Gaslighting:** Injects spoofed low-resource hardware responses via user-space memory files.


* **Module 2: Check Vaccine Status:**
* Performs an automated diagnostic sweep across the OS and memory to verify that all deceptive traps and defensive shields are active and running.


* **Module 3: Generate Advanced Audit Report:**
* Compiles a technical overview report logging all active deceptive indicators and live process PIDs for immediate environment verification.


* **Module 4: Secure Rollback & Purge:**
* Completely cleanses the environment by safely removing all injected mutexes, terminating the ghost processes, and deleting fake profiles with **Zero Resource Leak**.



---

## 🔬 Hands-on Lab: My Full Attack & Defense Testing Scenario

You can reproduce this exact lab scenario on your own Kali Linux environment to understand how the interaction works:

### 🛑 Pre-requisite Notes:

1. The tool requires **ROOT** privileges to interact with Shared Memory and Kernel process mapping.
2. When testing, remember to edit `kittens.py` and **change the IP** inside the script to match your attacker machine's IP address.
3. You must start your **Ncat / Netcat Listener** on the attacker machine to capture the reverse connection before launching the attack.

---

### 📂 Step 1: Create the Sensitive Target File

First, I created a mock text file containing simulated highly sensitive bank account information to serve as the target for the asset-theft simulation:

```bash
echo -e "--- VICTIM SENSITIVE DATA ---\nUsername Bank Account: shooq\nPassword: 123456\nStatus: Active" > /tmp/top_secret.txt

```

---

### 📡 Step 2: Launch the Attacker Listener

On your attacker machine/terminal window, spin up an **Ncat / Netcat** listener on port `4444` to catch the incoming exfiltrated file buffer:

```bash
nc -lvnp 4444

```

---

### 🧪 Step 3: Phase 1 Testing (Attack Execution without VAXBOX)

Run the pre-configured Trojan script while the host system is unprotected:

```bash
python3 kittens.py

```

**🔴 Observed Result (Successful Attack):**
The Trojan passes its environment validation seamlessly because no deceptive markers exist. It immediately accesses `/tmp/top_secret.txt` and transmits the data straight to your open Ncat listener screen.

---

### 💉 Step 4: Phase 2 Testing (Activating VAXBOX & Vaccine Self-Destruction)

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

### 🧹 Step 5: Post-Lab Clean Up

To restore your Linux core environment back to its native condition:

1. Return to the VAXBOX CLI terminal dashboard.
2. Select **`Option 4 (Secure Rollback & Purge)`**.
3. All injected file paths, mock memory artifacts, and network ghost PIDs will be thoroughly unlinked instantly.

---

## 👤 Developer

* **Shouq Aldawsari**

---

## 📄 License & Disclaimer

This tool is built strictly for educational, defensive research, and system immunization purposes.

```


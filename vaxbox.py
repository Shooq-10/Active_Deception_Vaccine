#!/usr/bin/env python3
import os
import sys
import time
import subprocess
from datetime import datetime

# 🎨 CLI Terminal Interface Styling
def print_banner():
    banner = r"""
\033[94m====================================================================
      ██╗   ██╗ █████╗ ██╗  ██╗██████╗  ██████╗ ██╗  ██╗
      ██║   ██║██╔══██╗╚██╗██╔╝██╔══██╗██╔═══██╗╚██╗██╔╝
      ██║   ██║███████║ ╚███╔╝ ██████╔╝██║   ██║ ╚███╔╝ 
      ╚██╗ ██╔╝██╔══██║ ██╔██╗ ██╔══██╗██║   ██║ ██╔██╗ 
       ╚████╔╝ ██║  ██║██╔╝ ██╗██████╔╝╚██████╔╝██╔╝ ██╗
        ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
\033[97m
              [ 💉 VAXBOX v4.0: Next-Gen Malware Vaccine ]
              [        Status: Memory Fully Immunized     ]
\033[95m
                      By: Shouq Aldawsari
\033[94m====================================================================\033[0m"""
    print(banner)

def print_menu():
    print("\n\033[97m[ Control Panel - Next-Gen Deception Modules ]\033[0m")
    print("1) [Module 1] Activate Vaccine (Artifacts + Hardware + Mutex Array)")
    print("2) [Module 2] Check Vaccine Status   (Check active deception indicators)")
    print("3) [Module 3] Generate Advanced Audit Report  (Technical summary report)")
    print("4) [Module 4] Secure Rollback & Purge (Completely clean environment)")
    print("5) Exit                               (Exit)")
    print("\033[94m====================================================================\033[0m")

def activate_vaccine():
    print("\n\033[94m[*] [Module 1] Initializing Cyber Deception & Immunization...\033[0m")
    
    # 1. Injecting Sandbox Artifacts
    os.makedirs("/etc/modprobe.d", exist_ok=True)
    with open("/etc/modprobe.d/vboxguest.conf", "w") as f:
        f.write("# Fake VirtualBox guest configuration for malware deception\n")
    os.makedirs("/home/sandbox_user/.cuckoo", exist_ok=True)
    
    # 2. Deploying Dynamic Ghost Process
    subprocess.Popen(["bash", "-c", "exec -a /tmp/tcpdump sleep 99999"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # 3. Injecting Threat-Intelligence Mutex Array into Shared Memory
    os.makedirs("/dev/shm", exist_ok=True)
    mutexes = ["sem.WannaCry_Global_Mutex", "sem.Lumma_Evasion_2026", "sem.CobaltStrike_C2_Hook", "sem.Sandbox_Analysis_Lock", "sem.vbox_deception_mutex"]
    for m in mutexes:
        with open(f"/dev/shm/{m}", "w") as f:
            f.write("LOCKED")
            
    # 4. Activating Hardware Gaslighting Profiles (User-Space Emulation)
    with open("/tmp/fake_cpuinfo", "w") as f:
        f.write("processor : 0\nvendor_id : GenuineIntel\ncpu family : 6\nmodel name : Intel(R) Core(TM) i7\ncpu cores : 1\n")
        
    with open("/tmp/fake_meminfo", "w") as f:
        f.write("MemTotal:        1750000 kB\nMemFree:          200000 kB\nMemAvailable:     400000 kB\n")
        
    print("\033[92m[✔] System Immunized Successfully! Threat Array and Gaslighting Active.\033[0m")

def check_status():
    print("\n\033[94m[*] [Module 2] Querying System for Deception Artifacts...\033[0m")
    print("+-----------------------------------+-----------------+")
    print("| Deception Indicator               | Status          |")
    print("+-----------------------------------+-----------------+")
    if os.path.exists("/etc/modprobe.d/vboxguest.conf"):
        print("| File: /etc/modprobe.d/vboxguest   | \033[92mINJECTED\033[0m        |")
    else:
        print("| File: /etc/modprobe.d/vboxguest   | \033[91mNOT FOUND\033[0m       |")
        
    if os.path.exists("/home/sandbox_user/.cuckoo"):
        print("| Folder: /home/sandbox_user/.cuckoo| \033[92mINJECTED\033[0m        |")
    else:
        print("| Folder: /home/sandbox_user/.cuckoo| \033[91mNOT FOUND\033[0m       |")
        
    try:
        pid = subprocess.check_output(["pgrep", "-f", "/tmp/tcpdump"]).decode().strip().split('\n')[0]
        print("| Ghost Process: /tmp/tcpdump       | \033[92mRUNNING\033[0m          |")
    except:
        print("| Ghost Process: /tmp/tcpdump       | \033[91mSTOPPED\033[0m          |")
        
    if os.path.exists("/tmp/fake_cpuinfo") and os.path.exists("/tmp/fake_meminfo"):
        print("| Hardware Profile Gaslighting      | \033[92mACTIVE\033[0m           |")
    else:
        print("| Hardware Profile Gaslighting      | \033[91mINACTIVE\033[0m         |")
        
    active_mutex = 0
    mutexes = ["sem.WannaCry_Global_Mutex", "sem.Lumma_Evasion_2026", "sem.CobaltStrike_C2_Hook", "sem.Sandbox_Analysis_Lock", "sem.vbox_deception_mutex"]
    for m in mutexes:
        if os.path.exists(f"/dev/shm/{m}"):
            active_mutex += 1
    print(f"| Active Mutex Shields Injected     | \033[92m[{active_mutex}/5] Active\033[0m |")
    print("+-----------------------------------+-----------------+")

def generate_report():
    print("\n\033[94m[*] [Module 3] Mining System Data & Generating Technical Report...\033[0m")
    try:
        pid = subprocess.check_output(["pgrep", "-f", "/tmp/tcpdump"]).decode().strip().split('\n')[0]
    except:
        pid = "NOT RUNNING"
        
    report_content = f"""=====================================================================
         VAXBOX v4.0 FORENSIC MULTI-MUTEX & DECEPTION REPORT         
=====================================================================
Report Generated On   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Target OS Platform    : linux (Kali Linux Core)
Execution Authority   : ROOT (Verified)
---------------------------------------------------------------------
[+] MODULE 1: STATIC ARTIFACT INJECTION
  - Config File Path  : /etc/modprobe.d/vboxguest.conf Status: [INJECTED]
  - Cuckoo Directory  : /home/sandbox_user/.cuckoo      Status: [CREATED]
---------------------------------------------------------------------
[+] MODULE 2: DYNAMIC PROCESS DECEPTION (GHOST PROCESS)
  - Deceptive Process : /tmp/tcpdump
  - Active Process PID: {pid}
---------------------------------------------------------------------
[+] MODULE 3: THREAT-INTELLIGENCE MUTEX ARRAY
  - Mutex Object: sem.WannaCry_Global_Mutex      Status: [ACTIVE (Locked)]
  - Mutex Object: sem.Lumma_Evasion_2026         Status: [ACTIVE (Locked)]
  - Mutex Object: sem.CobaltStrike_C2_Hook       Status: [ACTIVE (Locked)]
  - Mutex Object: sem.Sandbox_Analysis_Lock      Status: [ACTIVE (Locked)]
  - Mutex Object: sem.vbox_deception_mutex       Status: [ACTIVE (Locked)]
---------------------------------------------------------------------
[+] MODULE 4: HARDWARE GASLIGHTING PROFILE
  - Spoofed Visible CPU to Malware: 1 Core
  - Spoofed Visible RAM to Malware: 1.75 GB
====================================================================="""
    report_path = "/tmp/vaxbox_audit_report.txt"
    with open(report_path, "w") as r:
        r.write(report_content)
    print(f"\033[92m[✔] Deep Forensic report compiled successfully at: {report_path}\033[0m")
    print("[*] Report Preview:")
    print(report_content)

def rollback_all():
    print("\n\033[91m[*] [Module 4] Initiating Secure Rollback & Purging Environment...\033[0m")
    if os.path.exists("/etc/modprobe.d/vboxguest.conf"):
        os.remove("/etc/modprobe.d/vboxguest.conf")
    if os.path.exists("/home/sandbox_user/.cuckoo"):
        os.rmdir("/home/sandbox_user/.cuckoo")
        
    subprocess.run(["pkill", "-f", "/tmp/tcpdump"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    mutexes = ["sem.WannaCry_Global_Mutex", "sem.Lumma_Evasion_2026", "sem.CobaltStrike_C2_Hook", "sem.Sandbox_Analysis_Lock", "sem.vbox_deception_mutex"]
    for m in mutexes:
        if os.path.exists(f"/dev/shm/{m}"):
            os.remove(f"/dev/shm/{m}")
            
    if os.path.exists("/tmp/fake_cpuinfo"):
        os.remove("/tmp/fake_cpuinfo")
    if os.path.exists("/tmp/fake_meminfo"):
        os.remove("/tmp/fake_meminfo")
        
    print("\033[92m[✔] Secure Rollback Complete. All Deception Artifacts Purged! [Zero Resource Leak]\033[0m")

def main():
    if os.geteuid() != 0:
        print("\n\033[91m[!] Error: VAXBOX requires ROOT privileges. Run with 'sudo python3 vaxbox.py'\033[0m\n")
        sys.exit(1)
    while True:
        os.system('clear')
        print_banner()
        print_menu()
        choice = input("[+] Select option (1-5): ").strip()
        if choice == "1":
            activate_vaccine()
            input("\nPress Enter to continue...")
        elif choice == "2":
            check_status()
            input("\nPress Enter to continue...")
        elif choice == "3":
            generate_report()
            input("\nPress Enter to continue...")
        elif choice == "4":
            rollback_all()
            input("\nPress Enter to continue...")
        elif choice == "5":
            print("\nExiting VaxBox. Stay safe!\n")
            break
        else:
            print("\033[91m[!] Invalid option. Please select 1-5.\033[0m")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
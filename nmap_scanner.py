import os
import subprocess
from colorama import Fore, Style, init
import ipaddress
import sys
import logging

# Initialize colorama
init(autoreset=True)

# Color definitions using colorama
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT
DIM = Style.DIM

# Custom underline ANSI escape code
UNDERLINE = '\033[4m'

# Logger setup
logging.basicConfig(filename='nmap_scanner.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clear_console():
    """Clear console screen for a cleaner interface."""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_sudo():
    """Check if the script is run with sudo."""
    if os.geteuid() != 0:
        print(f"{RED}{BOLD}Error: This script requires sudo access. Please run with 'sudo'.{RESET}")
        sys.exit(1)

def is_valid_ip(ip):
    """Validate the IP address format."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def run_nmap_command(command):
    """Run the Nmap command and return the output."""
    try:
        logging.info(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"{RED}{BOLD}Nmap Error: {e}{RESET}")
        logging.error(f"Nmap Error: {e}")
        return None

def parse_nmap_output(output):
    """Parse the Nmap output to display key results and vulnerabilities."""
    if output:
        print(f"{GREEN}{BOLD}=== Scan Results ==={RESET}")
        lines = output.split('\n')
        open_ports = []
        vulnerabilities = []
        errors = []

        for line in lines:
            if line.startswith("PORT"):
                print(f"{MAGENTA}{BOLD}{line}{RESET}")
            elif "/tcp" in line or "/udp" in line:
                open_ports.append(line)
            elif "|" in line or "_|_" in line:
                if "ERROR" in line or "Couldn't find" in line:
                    errors.append(line)
                elif "VULNERABILITY" in line or "vuln" in line:
                    vulnerabilities.append(line)
                else:
                    print(f"{CYAN}{line}{RESET}")

        if open_ports:
            print(f"{CYAN}{BOLD}Open Ports:{RESET}")
            for port in open_ports:
                print(f"{CYAN}{port}{RESET}")

        if vulnerabilities:
            print(f"{RED}{BOLD}Vulnerabilities:{RESET}")
            for vuln in vulnerabilities:
                print(f"{RED}{vuln}{RESET}")

        if errors:
            print(f"{YELLOW}{BOLD}Errors/Warnings:{RESET}")
            for error in errors:
                print(f"{YELLOW}{error}{RESET}")

        print(f"{GREEN}{BOLD}=== End of Scan Results ==={RESET}")

def nmap_port_scanner(target_ip, scan_option):
    """Run Nmap scan with the selected options."""
    print(f"{UNDERLINE}{BOLD}Target: {BLUE}{target_ip}{RESET}")
    logging.info(f"Scanning target: {target_ip} with option {scan_option}")

    # Define scan command options
    scan_commands = {
        1: ['nmap', '-Pn', '-sS', '-sV', '-O', '-p', '1-65535', '-T4', target_ip],  # Comprehensive scan
        2: ['nmap', '-Pn', '-sS', '-sV', '-p', '1-1024', '-T3', target_ip],  # Fast scan of well-known ports
        3: ['nmap', '-Pn', '-sU', '-sV', '-p', '1-1024', target_ip],  # UDP scan
        4: ['nmap', '-Pn', '-sV', '--script', 'http-csrf', target_ip],  # CSRF vulnerability scan
        5: ['nmap', '-Pn', '-p', '554', '-O', '--script', 'rtsp-url-brute', target_ip],  # RTSP URL brute force
        6: ['nmap', '-Pn', '--script', 'vuln', target_ip],  # Vulnerability assessment
        7: ['nmap', '-Pn', '-sS', '-sV', '-p', '1-65535', '-T5', '-A', target_ip],  # Aggressive scan with OS detection
        8: ['nmap', '-Pn', '-sS', '--script-updatedb', target_ip],  # Stealth scan
        9: ['nmap', '-Pn', '-sV', '-O', '--script', 'discovery', target_ip],  # Network discovery
        10: ['nmap', '-Pn', '--script=default,safe', target_ip],  # Default safe scripts
    }

    # Validate scan option
    if scan_option not in scan_commands:
        print(f"{RED}{BOLD}Invalid scan option. Please choose between 1 and 10.{RESET}")
        logging.error(f"Invalid scan option: {scan_option}")
        return

    # Run the Nmap scan with selected options
    command = scan_commands[scan_option]
    output = run_nmap_command(command)
    
    if output:
        parse_nmap_output(output)
        logging.info("Scan completed successfully.")
    else:
        logging.error("No output received from Nmap command.")

def main():
    clear_console()
    check_sudo()  # Ensure the script is run with sudo
    
    print(MAGENTA + f"""
             __                                              
  ____ _____/ /   __   ______________ _____  ____  ___  _____
 / __ `/ __  / | / /  / ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /| |/ /  (__  ) /__/ /_/ / / / / / / /  __/ /    
\__,_/\__,_/ |___/  /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                             
======================================
    Nexus Sec - Advanced Nmap Scanner
======================================
Developed by: Nexus Sec - Instagram: @nexussecelite
""" + RESET)

    print(f"{RED}WARNING: Unauthorized scanning may be illegal. Use responsibly and only with permission.{RESET}")

    target_ip = input(f"{GREEN}Enter the target IP address or website: {RESET}")

    if not is_valid_ip(target_ip):
        print(f"{RED}{BOLD}Invalid IP address or hostname. Please enter a valid IP address.{RESET}")
        logging.error(f"Invalid IP address or hostname entered: {target_ip}")
        exit()

    print("\nSelect scan option:")
    print(f"{YELLOW}1. Comprehensive scan")
    print("2. Fast scan of well-known ports")
    print("3. UDP scan")
    print(RED + "4. CSRF vulnerability scan")
    print("5. RTSP URL brute force")
    print(GREEN + "6. Vulnerability assessment")
    print("7. Aggressive scan with OS detection")
    print("8. Stealth scan")
    print("9. Network discovery")
    print("10. Default safe scripts" + RESET)

    try:
        scan_choice = int(input(f"{GREEN}Enter your choice (1-10): {RESET}"))
        nmap_port_scanner(target_ip, scan_choice)
    except ValueError as ve:
        print(f"{RED}Error: {ve}{RESET}")
        logging.error(f"ValueError: {ve}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_console()
        print(f"{RED}{BOLD}Force Exit{RESET}")
        logging.info("Script terminated by user.")
        sys.exit(0)

# Advanced Nmap Scanner

```
             __
  ____ _____/ /   __   ______________ _____  ____  ___  _____
 / __ `/ __  / | / /  / ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /| |/ /  (__  ) /__/ /_/ / / / / / / /  __/ /
\__,_/\__,_/ |___/  /____/\___/\__,_/_/ /_/_/ /_/\___/_/

======================================
                  Advanced Nmap Scanner
======================================
Developed by: Nexus Sec - Instagram: @nexussecelite
```

## Overview

One powerful tool made for network scanning and security evaluation is the Advanced Nmap Scanner. This application offers a variety of scan options to find open ports, services, vulnerabilities, and more by utilizing Nmap's potent capabilities. For network managers and security specialists, it is a vital tool.

## Features

- **Comprehensive Port Scanning**: Scans all ports or specified ranges to identify active services and their states.
- **Advanced Vulnerability Detection**: Uses Nmap scripts to detect common vulnerabilities and security issues.
- **Multiple Scan Types**: Includes options for comprehensive scans, fast scans, UDP scans, and more.
- **Professional and Clear Output**: The tool offers structured, color-coded output, making it easy to interpret results.

## Installation

1. **Install Nmap**: Ensure Nmap is installed on your system. You can download it from [Nmap's official website](https://nmap.org/download.html) or install it via your package manager:

   **For Debian/Ubuntu:**
   ```bash
   sudo apt-get install nmap
   ```

   **For CentOS/RHEL:**
   ```bash
   sudo yum install nmap
   ```

   **For macOS (using Homebrew):**
   ```bash
   brew install nmap
   ```

2. **Install Python and Dependencies**: Ensure you have Python installed (preferably version 3.x). Install the required Python package `colorama` for colored output:

   ```bash
   pip install colorama
   pip install python-nmap
   ```

3. **Clone the Repository**: Clone the repository to your local machine:

   ```bash
   git clone https://github.com/nexussecelite/Advanced-Nmap-Scanner.git
   cd Advanced-Nmap-Scanner
   ```

## Usage

1. **Run the script with sudo** to ensure necessary permissions for advanced scanning features.
2. **Enter the target IP address or hostname**: The tool validates the IP format to prevent errors.
3. **Select the desired scan option** from the provided list.

### Scan Options

1. **Comprehensive scan**: Scans all ports and identifies services.
2. **Fast scan of well-known ports**: Quick scan of common ports.
3. **UDP scan**: Scans for open UDP ports.
4. **CSRF vulnerability scan**: Checks for Cross-Site Request Forgery vulnerabilities.
5. **RTSP URL brute force**: Attempts to discover RTSP URLs.
6. **Vulnerability assessment**: General vulnerability detection.
7. **Aggressive scan with OS detection**: Includes OS detection and version detection.
8. **Stealth scan**: Minimizes the risk of detection during scanning.
9. **Network discovery**: Identifies active hosts and services.
10. **Default safe scripts**: Runs Nmap's default safe scripts for information gathering.

## Example

```
$ sudo python nmap_scanner.py
======================================
                  Advanced Nmap Scanner
======================================
Developed by: Nexus Sec - Instagram: @nexussecelite

WARNING: Unauthorized scanning may be illegal. Use responsibly and only with permission.

Enter the target IP address or website: 192.168.1.1

Select scan option:
1. Comprehensive scan
2. Fast scan of well-known ports
3. UDP scan
4. CSRF vulnerability scan
5. RTSP URL brute force
6. Vulnerability assessment
7. Aggressive scan with OS detection
8. Stealth scan
9. Network discovery
10. Default safe scripts

Enter your choice (1-10): 1
```

## Warning

**Unauthorized scanning of networks is illegal and unethical. Always ensure you have permission from the network owner before conducting scans. This tool is intended for ethical use only.**

Follow Me on Instagram [Nexus Sec](https://instagram.com/nexussecelite) - @nexussecelite

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

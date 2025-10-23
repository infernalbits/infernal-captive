# Captive-Mial: Captive Portal Bypass Tool

`captive-mial.sh` is a powerful shell script designed to bypass captive portals on Wi-Fi networks. It works by scanning the local network for already authenticated clients and then "hijacking" their session by spoofing their IP and MAC address.

This tool is designed for portability and ease of use, with automatic detection of network parameters and cross-platform support for both **Linux** and **macOS**.

## How It Works

1.  **Scans Network**: Identifies the current network configuration (IP, gateway, netmask, etc.).
2.  **Finds Victims**: Uses `nmap` to find other active clients on the same network.
3.  **Hijacks Session**: Iterates through the list of active clients, spoofing their MAC and IP address one by one.
4.  **Tests Connectivity**: After each attempt, it pings a public DNS server (8.8.8.8) to check for a successful internet connection.
5.  **Restores State**: If no successful connection is made, or when the script is terminated, it safely restores your original network configuration.

## Features

*   **Cross-Platform**: Works on both Linux and macOS.
*   **Automatic Detection**: Automatically discovers network parameters like your interface, gateway, and IP range.
*   **Manual Override**: Provides command-line flags to manually specify any network parameter.
*   **Safe**: Includes a cleanup function to restore your original MAC and IP address on exit.
*   **Robust Logging**: Creates a detailed log file in a temporary directory for easy troubleshooting.
*   **Debug Mode**: A `--debug` flag provides verbose output to diagnose issues.

## ⚠️ Disclaimer

This tool should be used for educational purposes and only on networks you are authorized to access in this manner. Using it on a public or private network without permission may violate its Terms of Service. The author is not responsible for any misuse of this script.

---

## Installation

### 1. Dependencies

First, you need to install the required command-line tools.

**On Debian / Ubuntu:**
```bash
sudo apt update
sudo apt install nmap sipcalc macchanger
```

**On Arch Linux:**
```bash
sudo pacman -S nmap sipcalc macchanger
```

**On macOS (using Homebrew):**
```bash
brew install nmap sipcalc
```
*(Note: `macchanger` is not required for macOS as the script uses `ifconfig`)*

### 2. Install the Script

To make the script runnable from anywhere in your terminal, follow these steps:

1.  **Make the script executable:**
    ```bash
    chmod +x captive-mial.sh
    ```

2.  **Move it to a directory in your `$PATH`:**
    A common location for user-installed scripts is `/usr/local/bin`.
    ```bash
    sudo mv captive-mial.sh /usr/local/bin/captive-mial
    ```

You can now run the script from any terminal window by typing `captive-mial`.

---

## Usage

The script **must be run with `sudo`** because it needs root privileges to change network interface settings.

### Basic Usage

In most cases, the script can auto-detect all required network parameters. Simply run:

```bash
sudo captive-mial
```

### Command-Line Options

You can use the `-h` or `--help` flag to see all available options.

```bash
sudo captive-mial --help
```

```text
captive-mial - Captive Portal Bypass Tool - Hijack IP and MAC for valid credentials

 captive-mial [parameters] 

Parameters:

-h ...  | ... --help                        ......... Show this help menu
-d ...  | ... --debug                       ......... Enable debug logging
-s ...  | ... --ssid=<name>             ......... Wifi SSID w/ Captive Portal
-i ...  | ... --iface=<name>           ......... Network Interface
-g ...  | ... --gateway=<ip>           ......... Network Gateway
-p ...  | ... --localip=<ip>           ......... Local IP address
-b ...  | ... --broadcast=<ip>        .......... Broadcast IP
-n ...  | ... --netmask=<cidr>        ......... Network Mask (CIDR, e.g. 24)
-m ... | ... --ipmask=<ip/cidr>     ......... IP with Mask (e.g. 192.168.1.10/24)
-w ...  | ... --network=<net/cidr>  ......... Network (e.g. 192.168.1.0/24)
-a ...  | ... --macaddress=<mac>     ......... Your original MAC Address
-S ...  | ... --netaddress=<ip>        ......... Network Address (e.g. 192.168.1.0)
```

### Troubleshooting

If the script fails or you want to see what's happening behind the scenes, use the `--debug` flag.

```bash
sudo captive-mial --debug
```

This will print detailed step-by-step information to a log file located in a temporary directory (e.g., `/tmp/hackaptive_XXXXXXXXXX/script.log`). The script will print the location of this directory when debug mode is enabled.

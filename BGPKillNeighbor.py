import sys
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import re

def validate_ip(ip):
    """Validate if the input is a valid IP address."""
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if pattern.match(ip):
        return all(0 <= int(octet) <= 255 for octet in ip.split('.'))
    return False

def validate_asn(asn):
    """Validate if the input is a valid ASN (integer)."""
    return asn.isdigit() and 1 <= int(asn) <= 4294967295  # 4-byte ASN range

def validate_delay(delay):
    """Validate if the input is a positive integer."""
    return delay.isdigit() and int(delay) > 0

def main():
    print("Welcome to the BGP graceful shutdown script!")
    
    # Collect user inputs with validation
    while True:
        asn = input("Enter your AS number: ")
        if validate_asn(asn):
            break
        print("Invalid ASN. Please enter a valid number between 1 and 4294967295.")

    while True:
        neighbor_ip = input("Enter the neighbor IP address: ")
        if validate_ip(neighbor_ip):
            break
        print("Invalid IP address. Please enter a valid IPv4 address.")

    while True:
        neighbor_as = input("Enter the neighbor's AS number: ")
        if validate_asn(neighbor_as):
            break
        print("Invalid ASN. Please enter a valid number between 1 and 4294967295.")

    while True:
        delay = input("Enter the graceful shutdown delay (in seconds): ")
        if validate_delay(delay):
            break
        print("Invalid delay. Please enter a positive integer.")

    # Device connection details
    device = {
        "device_type": "cisco_ios",  # Change this to match your device type (e.g., juniper, arista)
        "host": input("Enter the device IP address: "),
        "username": input("Enter your device username: "),
        "password": input("Enter your device password: "),
        "secret": input("Enter your device enable password (if applicable): ")
    }

    # Constructing the BGP configuration commands
    bgp_commands = [
        f"router bgp {asn}",
        f"neighbor {neighbor_ip} remote-as {neighbor_as}",
        f"neighbor {neighbor_ip} shutdown graceful {delay}"
    ]

    try:
        # Connect to the device
        print("Connecting to the device...")
        connection = ConnectHandler(**device)
        connection.enable()

        # Send the configuration commands
        print("Sending configuration commands...")
        connection.send_config_set(bgp_commands)

        # Verify the configuration
        print("Verifying the configuration...")
        output = connection.send_command(f"show bgp neighbor {neighbor_ip}")
        print(output)

        # Disconnect
        connection.disconnect()
        print("BGP graceful shutdown configuration applied successfully!")

    except NetmikoTimeoutException:
        print("Error: Connection timed out. Please check the device IP address and network connectivity.")
    except NetmikoAuthenticationException:
        print("Error: Authentication failed. Please check your uname and pwd.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

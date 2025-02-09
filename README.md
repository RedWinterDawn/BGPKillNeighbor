# BGPKillNeighbor
This script is a Python program for generating BGP (Border Gateway Protocol) graceful shutdown commands.
----

BGP Graceful Shutdown Automation Script
This Python script automates the process of configuring a BGP graceful shutdown for a specified neighbor. It leverages the Netmiko library to connect to network devices, apply the configuration commands, and verify the changes.

Features
Automates BGP Configuration: Constructs and sends BGP graceful shutdown commands to the specified network device.
Validation: Ensures input values like ASN, IP address, and delay are valid before proceeding.
Error Handling: Handles common errors such as:
Connection timeouts.
Authentication failures.
Unexpected issues during execution.
Verification: Displays the show bgp neighbor command output to confirm the configuration.
Prerequisites
Python: Ensure you have Python 3.6 or newer installed.
Netmiko: Install the Netmiko library using:
bash

pip install netmiko
Network Device: The target device should support SSH and have a CLI similar to Cisco IOS (or another supported device_type).
Installation
Clone or download this repository to your local machine.
Install the required dependencies:
bash

pip install netmiko
Save the script as bgp_graceful_shutdown.py or another appropriate name.
Usage
Run the script:
bash

python bgp_graceful_shutdown.py
Enter the following details when prompted:
Your AS number (e.g., 65001).
Neighbor's IP address (e.g., 192.168.1.1).
Neighbor's AS number (e.g., 65002).
Graceful shutdown delay (e.g., 300 seconds).
Target device details:
Device IP address.
Username.
Password.
Enable password (if applicable).
The script will:
Connect to the device via SSH.
Apply the BGP graceful shutdown configuration.
Verify the configuration with the show bgp neighbor command.
Disconnect from the device.
Example
Input:
mathematica

Enter your AS number: 65001
Enter the neighbor IP address: 192.168.1.1
Enter the neighbor's AS number: 65002
Enter the graceful shutdown delay (in seconds): 300
Enter the device IP address: 192.168.0.1
Enter your device username: admin
Enter your device password: ********
Enter your device enable password (if applicable): ********
Output:
vbnet

Connecting to the device...
Sending configuration commands...
Verifying the configuration...
BGP graceful shutdown configuration applied successfully!
Neighbor information:
BGP neighbor is 192.168.1.1
 Remote AS 65002, local AS 65001
  Graceful Shutdown configured: Delay 300 seconds
Error Handling
The script handles the following scenarios gracefully:

Invalid Input: Prompts for correct values if ASNs, IPs, or delay are invalid.

Connection Timeout: Notifies the user if the device cannot be reached.
Authentication Failure: Alerts the user if the username/password is incorrect.
Unexpected Errors: Displays a descriptive error message for debugging.
Supported Platforms
This script is designed for devices with the following CLI platforms:

Cisco IOS (device_type: cisco_ios)
Juniper (device_type: juniper)
Arista EOS (device_type: arista_eos)
For other platforms, modify the device_type in the script as needed.

Customization
Additional Commands: To add or modify commands, edit the bgp_commands list in the script.
Device Type: Update the device_type field in the device dictionary to match your network device.
Troubleshooting

SSH Not Enabled: Ensure SSH is enabled on your device and the IP address is reachable.
Permissions: Verify the provided credentials have the required privileges to execute configuration commands.

Dependencies: Ensure Netmiko is installed and up to date:
bash
pip install --upgrade netmiko

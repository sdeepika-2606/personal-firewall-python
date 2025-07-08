# Personal Firewall Using Python

## Introduction  
This project implements a lightweight personal firewall built in Python that monitors and filters network traffic based on customizable rules. It allows users to block or allow IP addresses, ports, and protocols, logs suspicious packets, and provides a graphical interface for real-time monitoring.

## Features  
- Packet sniffing using **Scapy**  
- Rule-based filtering with JSON-configured rules  
- Logging of blocked packets to a file  
- Optional GUI with **Tkinter** to view logs and current firewall rules  
- Clear logs functionality from GUI  

## Tools Used  
- Python 3  
- Scapy (Packet sniffing and manipulation)  
- Tkinter (GUI)  
- JSON (Rules configuration)  
Install dependencies:

#Install dependencies: pip install scapy
#Run the firewall: python firewall.py
#Run the GUI to monitor logs: python gui.py

#Usage
Customize rules by editing rules.json.

Firewall runs on CLI, sniffing network traffic and blocking based on rules.

GUI shows live logs and current rules, with the option to clear logs.

#Future Enhancements
Add GUI-based rule editing.

Implement iptables integration for system-level enforcement (Linux).

Add alert notifications for suspicious activity.






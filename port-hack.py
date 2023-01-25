import os
import sys

def hack_tool():
    print("Welcome to the new hack tool!")

    target = input("Please enter the target's IP address: ")

    print("Scanning target...")

    # Perform a port scan on the target IP address
    os.system("nmap -Pn -sC -sV " + target)

    # Get a list of open ports on the target machine
    open_ports = input("Please enter a list of open ports on the target machine: ").split(",")

    # Try to exploit each open port
    for port in open_ports:
        print("Trying to exploit port " + port + "...")
        os.system("exploit -t " + target + ":" + port)

    print("Hack tool finished!")

hack_tool()

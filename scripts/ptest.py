import os
import time
import requests
import psutil

# Tenda Router Configuration
router_ip = "http://192.168.10.1"  # Common Tenda router IP, update if different
username = "admin"  # Default username
password = "nimda12345"  # Your password

# Router Reboot URL (Tenda routers use a specific endpoint for rebooting, adjust as necessary)
router_reboot_url = f"{router_ip}/goform/reboot"  # Common Tenda reboot URL, but verify in your manual

# Google DNS
dns_servers = "8.8.8.8 8.8.4.4"  # Google DNS for stability

# Function to ping a server to check the connection status
def ping(host="8.8.8.8", count=5):
    response = os.system(f"ping -c {count} {host}")
    return response == 0

# Function to reboot the Tenda router remotely
def reboot_router():
    try:
        session = requests.Session()
        session.auth = (username, password)
        response = session.get(router_reboot_url)  # Send a GET request to reboot
        if response.status_code == 200:
            print("Router rebooted successfully.")
        else:
            print(f"Failed to reboot the router. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error rebooting router: {e}")

# Function to flush DNS cache
def flush_dns():
    print("Flushing DNS cache...")
    os.system("ipconfig /flushdns")

# Function to set DNS servers to Google DNS
def set_dns():
    interface = "Ethernet"  # Or "Wi-Fi" for wireless
    print(f"Setting DNS to {dns_servers}...")
    os.system(f'netsh interface ip set dns name="{interface}" static {dns_servers}')

# Function to monitor network bandwidth usage
def get_network_usage():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

# Main function to monitor and stabilize the connection
def monitor_connection():
    while True:
        print("Checking internet stability...")
        
        # Ping test to check if the internet is stable
        if not ping():
            print("Internet connection lost. Attempting to stabilize...")
            
            # Optionally, reboot the router if there is no internet
            reboot_router()
            
            # Optionally, flush the DNS cache to resolve any DNS-related issues
            flush_dns()
            
            # Optionally, set DNS to a more reliable server like Google's
            set_dns()
        else:
            print("Internet is stable.")
        
        # Monitor network usage
        sent, recv = get_network_usage()
        print(f"Bytes Sent: {sent}, Bytes Received: {recv}")
        
        # Check every 5 minutes
        time.sleep(300)  # Check every 5 minutes (300 seconds)

if __name__ == "__main__":
    monitor_connection()

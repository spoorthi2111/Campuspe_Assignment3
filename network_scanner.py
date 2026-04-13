import socket
import time

def scan_network():
    target = input("Enter target IP address (e.g., 127.0.0.1): ")
    port_input = input("Enter ports to scan separated by commas (e.g., 22,80,443): ")
    
    ports = [int(p.strip()) for p in port_input.split(",")]
    
    print(f"\nStarting scan on {target}...")
    start_time = time.time()
    
    results = []

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) 
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSED"
            
        res_str = f"Port {port}: {status}"
        print(res_str)
        results.append(res_str)
        s.close()

   
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    
    summary = f"\nScan completed in {duration} seconds."
    print(summary)

    with open("scan_results.txt", "w") as f:
        f.write(f"Scan Report for {target}\n")
        f.write("\n".join(results))
        f.write(summary)

if __name__ == "__main__":
    scan_network()

import subprocess
import sys
import os

def run_nmap(target_file):
    if not os.path.exists(target_file):
        print(f"[!] Error: File '{target_file}' not found.")
        return
    output_file = "scan_results.txt"
    
    command = [
        "nmap",
        "-iL", target_file,
        "-sV",
        "-Pn",
        "-oN", output_file
    ]

    print(f"[*] Reading targets from: {target_file}")
    print(f"[*] Running command: {' '.join(command)}\n")

    try:
        process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT, 
            text=True,
            bufsize=1
        )

        for line in process.stdout:
            print(line, end="")

        process.wait()
        print(f"\n[+] Scan complete. Results saved to: {output_file}")
        
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        process.terminate()
    except FileNotFoundError:
        print("[!] Error: nmap is not installed or not in your PATH.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run_nmap.py <path_to_targets.txt>")
        print("Example: python3 run_nmap.py my_targets.txt")
    else:
        run_nmap(sys.argv[1])

# quick description for nmap commands used. 
#-iL <file> (Input List): Instead of typing IP addresses manually, tell Nmap to "read this text file" for the list of targets.
#-sV (Service Version): It asks the service, "What version of software are you running?" (e.g., Apache 2.4.41).
#-Pn (No Ping): Tells Nmap, "Don't check if the host is 'alive' first—just start scanning." Very crucial if a firewall is blocking ping requests.
#-oN <file> (Output Normal): Saves your results into a text file.
# also, stop being a hypocrite; it's as if you don't use AI to 'vibe code,' lmao. -codeakyra

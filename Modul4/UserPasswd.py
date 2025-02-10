import paramiko

def ssh_command_with_password(hostname, username, password, command):
    """
    Logger på SSH-server med brugernavn + kodeord og kører en given kommando.
    Returnerer stdout og stderr fra kommandoen.
    """
    # Opret SSHClient-objekt
    client = paramiko.SSHClient()
    
    # Indstil policy for håndtering af ukendte nøgler (AutoAddPolicy godkender alle).
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Forbind til SSH-server
        client.connect(
            hostname=hostname,
            username=username,
            password=password,
            # port=22,  # Hvis du bruger en anden port, tilføj denne parameter
            look_for_keys=False
        )
        
        # Eksekvér kommandoen
        stdin, stdout, stderr = client.exec_command(command)
        
        # Læs output
        out = stdout.read().decode('utf-8')
        err = stderr.read().decode('utf-8')
        
        return out, err
    except Exception as e:
        print(f"Fejl ved SSH-forbindelse: {e}")
        return None, None
    finally:
        client.close()


if __name__ == "__main__":
    HOST = "192.168.111.128"   # IP eller hostname
    USER = "ihn"
    PASS = "MaaGodt*7913"
    CMD  = "ls -la"        # Den kommando/program, du ønsker at køre
    
    stdout_data, stderr_data = ssh_command_with_password(HOST, USER, PASS, CMD)
    
    print("=== STDOUT ===")
    print(stdout_data)
    print("=== STDERR ===")
    print(stderr_data)

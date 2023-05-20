import platform
import subprocess

def main():
    # Display basic system information
    print("Sistema: ", platform.system())
    print("Hostname: ", platform.node())
    print("Kernel: ", platform.release())
    print("Version: ", platform.version())

    # Display CPU information
    output = subprocess.run("cat /proc/cpuinfo | grep 'model name' | uniq",
                            shell=True, stdout=subprocess.PIPE)
    cpu_model = output.stdout.decode().strip().split(':')[1].lstrip()

    output = subprocess.run("nproc", shell=True, stdout=subprocess.PIPE)
    cpu_cores = output.stdout.decode().strip()

    print("CPU: ", cpu_model)
    print("Nucleos CPU: ", cpu_cores)

    # Display memory information
    output = subprocess.run("free -h | awk '/^Mem/ {print $2}'", 
                            shell=True, stdout=subprocess.PIPE)
    memory_total = output.stdout.decode().strip()
    print("Memoria RAM: ", memory_total)

if __name__ == '__main__':
    main()


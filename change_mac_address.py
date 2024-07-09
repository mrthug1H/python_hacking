import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to use")
    parser.add_option("-m", "--mac", dest="mac_address", help="New MAC address")
    return parser.parse_args()

def change_mac_address(interface, mac_address):
    # notification for the user
    print("[+] Changing MAC address of " + interface + " to " + mac_address)
    # shell code for terminal
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_argument()

if options.interface and options.mac_address:
    change_mac_address(options.interface, options.mac_address)
else:
    print("[-] Please specify both an interface and a MAC address. Use --help for more info.")

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
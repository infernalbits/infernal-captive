
# imports that will probably be needed
import platform
import nmap, socket, ipaddress, netifaces
import subprocess, sys, os, argparse
from get_mac import get_mac_address as getMac
from alive_progress import alive_bar; import time

script = 'escCaptivity.py'
version = '2.0'
pyVersion = '3.1x'
author = 'dropdeadRedd'
company = 'Soapy Toaster Solutions'
github = 'https://github.com/drpdeadredd/escCaptivity.git'
desc = '''
This script helps to pass through the captive portals in     
public Wi-Fi networks. It hijacks IP and MAC from somebody   
who is already connected and authorized on captive portal.   
Tested with different captive portals in airports & hotels 
all over the world.
'''
pyRequires = ' for python see requirements.txt'
bashRequires = 'bash/linux version requires coreutils, sipcalc, and nmap'
mentions = '''
Original linux-only verison written in bash by the developer
Stanislav "systematicat" Kotivetc.
Additions, translations, Compatibility Upgrades by dropdeadredd.

'''
notes = 'Acess to, and the use of, Information is an unalienable human right and should not be used for profit.'
notesCont = 'Justified subversive acts are a form of patriotism and when made illegal are gross misappropriations of justice.'

with alive_bar(total) as bar:
    for _ in range(1000):
        time.sleep(.001)
        bar()
            

def findOS():
    from time import sleep
    ops = ['Linux', 'Windows']
    check_ops = platform.system()
    if check_ops != ops[:]:
        print('You are running an incompatible Operating System.')
        sleep(10)
        print('Please stop being a hipster...')
        sleep(5)
        print('Install either Linux or Windows to [esc] Captivity.')
        exit(1)
    elif check_ops != ops[-1]:
        linuxParams()
    else:
        netParams()



netParams = [] # output of wifi parameters in either list of dict with name:output for each key pair
hostname = socket.gethostname()
localip = socket.gethostbyname(hostname)
broadcast = ipaddress.IPv4Network.broadcast.address
netmask = ipaddress.IPv4Network.netmask
gateway = netifaces.gateways()
wifissid = 
ipmask =
network = 
macaddress = 
netaddress =
iface = 
netParams.append()
linuxParams = [] # output of wifi parameters in either list of dict with name:output for each key pair
linux.iface = subproccess.call("ip -o -4 route show to default | awk '/dev/ {print $5}' | head -n1", shell=True)
linux.localip = subprocess.call("ip -o -4 route get 1 | awk '/src/ {print $7}'", shell=True)
linux.wifissid = subproccess.call(f"iw dev '{iface}' link " + "| awk '/SSID/ {print $NF}'", shell=True)
linux.gateway = subproccess.call("ip -o -4 route show to default | awk '/via/ {print $3}'", shell=True)
linux.broadcast = subproccess.call(f"ip -o -4 addr show dev '{iface}' " + "| awk '/brd/ {print $6}'", shell=True)
linux.ipmask = subprocess.call(f"ip -o -4 addr show dev '{interface}' " + "| awk '/inet/ {print $4}'", shell=True)
linux.netmask = subproccess.call(f"printf '%s\n' {ipmask} | cut -d '/' -f 2", shell=True)
linux.netaddress = subproccess.call(f"sipcalc '{ipmask}' " + "| awk '/Network address/ {print $NF}", shell=True)
linux.network = netaddress/netmask
linux.macaddress = subproccess.call(f"ip -0 addr show dev '{interface}' " + "| awk '/link/ && /ether/ {print $2}' | tr '[:upper;}' '[:lower:]'", shell=True)
linuxParams.append(iface, localip, wifissid, gateway, broadcast, ipmask, netmask, netaddress, network, macaddress)
    

def check_sudo():
    admin = 1
    # if the user is not root then exit 1
    if admin == 0:
        exit(1)


def create_temp():
    import sys
    tmp = ''
    with open(tmp, 'w+') as tmpfile:
        tmpfile.write('sometext\n')
        tmpfile.writelines(['a\n', 'b\n', 'c\n'])
        print('another line', file=tmp/tmpfile)
    pass


def clean_up():
    # remove tmp directory using tmp var
    # trap 0
    # exit


def calc_network():
    # if $netmask is < 24 then
    # calculate $network with sipcalc
    # split up $network into smaller chunks with
    # awk (/Network/ {print $3}) output from sipcalc > to temporary directory file networklist.$$.txt
    # else cut (-d "/" -f 1) $network > to "tmp" var to temporary directory file  networklist.$$.txt
    pass


def routermac():
    import nmap
    # encapsulate routermac var with router mac address
    # with output from nmap grep and tr
    # linux command : getroutermac="$(nmap -n -sn -PR -PS -PA -PU -T5 $gateway | grep -E -o '[A-Z0-9:]{17}' | tr A-Z a-z)"
    # windows comp :
    pass


def main():
    import sys
    textin, textout = sys.stdin.read(), sys.stdout.read()
    # first
    # while read networkfromlist
    # if $netmask is less than 24 then $network=$networkfromlist/24
    # else $network is $networkfromlist/$netmask
    # scan selected network for acitve hosts in $network
    # using nmap excluding $localip $gateway $network addresses
    # awk (/for/ {print $5} ; /Address/ {print $3}) nmap output
    # sed ($!N;s/\n/ - /) awk output to $tmp and file hostsalive.$$.txt
    # third
    # create newipset and newmacse with formatted output from $hostline
    # while read $hostline
    # create netipset var populate with command printf $hostline with /n
    # awk ({print $1}')) output of print $hostline
    # create netmacset var and populate with command printf $hostline with /n
    # awk ({print $3}')) output of print $hostline
    # tr ([:upper:] [:lower:]) awk output
    # fourth
    # set founded IP and MAC for wireless interface with ip commands
    # if $ routermac is not equal to $newmacset then
    # print trying to hijack newipset and newmacset
    # bring down $interfrace with ip link
    # set dev $interfrace address $newmacset using ip link
    # bing up $interface with ip link
    # ip addr flush dev $interface
    # ip addr add $newipset/$netmask broadcast $broadcast dev $interface
    # ip route add default via $gateway
    # let interface establish connection sleep 1 seconds
    # test new connection
    # check if google dns is pingable with new IP and MAC and route STDOUT to /dev/null
    # ping -c1 -w1 8.8.8.8 > /dev/null
    # if $? (command? or output?) is equal to 0 then
    # Success and exit 0
    # else skip $newipset and $newmacset
    # close while loop step 3 < $tmp/hostalive.$$.txt
    # remove file $tmp/hostalive.$$.txt
    # print current loop unsuccessful next loop
    # close while loop step 1 < $tmp/hostalive.$$.txt
    # remove file $tmp/hostalive.$$.txt
    # print main loop unsuccessful and restore original MAC and IP
    # ip link set $interface down
    # ip link set dev $interface address $macaddress
    # ip link set $interface up
    # ip addr flush dev $interface
    # ip add add $ipmask broadcast $broadcast dev $interface
    # ip route add default via $gateway
    pass

parser = argparse.ArgumentParser(description='Optional app description')
    # Required positional argument
parser.add_argument('pos_arg', type=int,
                         help='A required integer positional argument')
    # Optional positional argument
parser.add_argument('opt_pos_arg', type=int, nargs='?',
                        help='An optional integer positional argument')
    # Optional argument
parser.add_argument('--opt_arg', type=int,
                        help='An optional integer argument')
    # Switch
parser.add_argument('--switch', action='store_true',
                        help='A boolean switch')
# call functions
if __name__ = '__main__':
    args = parser.parse_args()
    if args.pos_arg > 10:
        parser.error("pos_arg cannot be larger than 10")
    clean_up()  # trap clean_up function with 0 1 2 3 15
    check_sudo()
    create_temp()
    calc_network()
    routermac()  # add routermac to calc_network()? used once in main()
    main()  # meat and potatoes the actual "hijacking"

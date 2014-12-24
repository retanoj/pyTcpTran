# coding = utf-8
#
# ######################################################
#
#   proxy.txt为代理地址列表
#   默认本地监听端口为 5551，默认5秒更换一次代理
#   burpsuite发HTTP包，要手动修改HTTP包的URL为全路径
#
# ######################################################

from subprocess import Popen
from time import sleep
import sys

def run(file,lport=5551, sleeptime=5):
    with open(file) as f:
        for line in f:
            rhost, rport = line.split(':')
            cmd = "ip_relay %s %s %s" % (lport, rhost, rport)
            p = Popen(cmd, shell=False)
            sleep(sleeptime)
            p.terminate()
            
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'eg. pyTcpTran.py proxy.txt 5551'
        sys.exit(1)
    file = sys.argv[1]
    port = sys.argv[2]
    run(file, port)
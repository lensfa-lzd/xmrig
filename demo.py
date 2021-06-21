# coding=utf-8
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--user", type=str, default='AWS0', help="name")
opt = parser.parse_args()


def replace(user):
    lines = open('config.json').readlines()
    f = open('config.json', 'w')
    for s in lines:
        f.write(s.replace('test', user))
    f.close()


'''os.system('echo "start setup script"')
os.system('echo "等待 15 秒将继续运行安装 (按 Ctrl+C 取消)"')
# os.system('sleep 15')
os.system('wget https://github.com/lensfa-lzd/xmrig/releases/download/v6.12.2/xmrig.tar.gz')
os.system('tar xf xmrig.tar.gz')
os.system('echo "start setup script"')
os.system('echo "start setup script"')'''

replace(opt.user)

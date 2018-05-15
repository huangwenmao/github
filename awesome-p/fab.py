
from fabric.api import *


env.user = 'root'
env.hosts = ['192.168.1.102']
env.password = '123456'

def build():
    lcd('/cygdrive/c/users/pc-asus/Downloads/awesome-p')
    local('tar -cvf awesome.tar ./*')

def deploy():
    put('c:/users/pc-asus/Downloads/awesome-p/awesome.tar','/srv/awesome.tar')
    with cd('/srv'):
        run('rm -rf awesome')
        run('mkdir awesome')
        run('chmod 777 awesome')
        run('tar -xvf awesome.tar -C /srv/awesome')

        
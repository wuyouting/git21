#_*_coding:utf-8_*_


'''
local 执行本地命令 如:local('uname -s')
lcd 切换本地目录 如:lcd('/home')
cd 切换远程目录 如:cd('/data/logs')
run 执行远程命令 如:run('free -m')
sudo sudo方式执行远程命令 如:sudo('/etc/init.d/httpd start')
put 上传本地文件到远程主机  如:put('/home/user.info','/data/user.info')
get 从远程主机下载文件到本地 如:get('/data/user.info','/home/root.info')
prompt 获得用户输入信息 如:prompt('please input user password:')


confirm 获得提示信息确认 如confirm("Tests failed, Continue[Y/N]")
reboot, 重启远程主机 如:reboot()

@task 函数修饰符，标识的函数为fab可调用，非标记对fab不可见，纯业务逻辑
@runs_once 函数修饰符，标识的函数只会执行一次，不受多台主机影响
'''


'''

使用fabric实现mysql源码批量安装部署

'''

from fabric.api import *


env.user = 'wuyoutin'
env.hosts = ['192.168.199.145']
env.password = 'wyt17507560752xmz'

def host_type():
    run('uname -s')
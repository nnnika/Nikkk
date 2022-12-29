# python多任务及网络编程

## 学习新的操作系统 
虚拟机软件 -> 虚拟机 -> 操作系统
虚拟机软件： Vmware，VirtualBox
虚拟机之间是相互独立的

## 常用的Linux发行版
Ubantu, CentOS, Redhat

## Linux主要目录
* /： 根目录
* /bin： 可执行二进制文件的目录
* /etc： 系统配置文件存放的目录
* /home： 用户家目录

## Linux命令
### 终端命令格式说明
命令名（ls）+ 选项（-r）+ 参数（touch文件名）
`command[-options][parameter]`  []可有可无

### 查看命令帮助的方式
* --help (command --help) 参数选项的列举说明
* man (man command) 一样，但阅读更方面，能翻页 （退出：q）

### 查看目录
* ls: 查看当前路径下的目录信息 
  命令选项：
    -l 以列表方式显示文件信息
    -h 智能显示文件大小 (-lh) 
    -a显示隐藏文件和目录 (创建文件时文件名前加.)
* tree: 以树状方式显示目录 (tree 文件名)
* pwd: 查看当前目录路径
* clear: 清除终端内容

### 切换目录
cd: 改变目录change directory
cd 目录: 切换到指定目录
cd ~ : 切换到当前用户的主目录
cd .. : 切换到上一级目录
cd . : 切换到当前目录（创建文件夹时使用）
cd - : 切换到上一次目录

### 路径
* 绝对路径：从根目录算起
* 相对路径：从当前目录算起
  (e.g. 桌面目录：/home/Desktop, 当前路径：/home/python, 相对路径切换回桌面：cd ../Desktop)
  (切换上一级再上一级目录：cd ../../)
  
### 创建、删除文件和目录
* touch 文件名：创建指定文件
* mkdir 目录名：创建目录（文件夹）
  命令选项：
    -p: 创建多层不存在目录 (mkdir aa/bb/cc -p)
* rm 文件名：删除指定文件
  命令选项：
    -i: 交互式提示（是否删除）
    -r: 递归删除
    -f: 强制删除（没有提示）
* rmdir 目录名：删除空目录
* 删除非空目录： rm 文件名/ -r (递归删除目录及其内容)

### 复制、移动文件和目录
* cp: 复制文件目录 
  (cp 文件名 新文件名) (cp 目录名 新目录名 -r) (cp 文件相对路径 另一目录相对路径)
  命令选项：
    -i: 交互式提示
    -r: 递归
    -v: 显示拷贝后的路径描述
* mv: 移动、重命名
  (mv 文件相对路径 要移动的相对路径) (mv 原名 新名)

### 重定向命令




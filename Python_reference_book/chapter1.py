import sys


# 文件输入和输出
f = open("xxxx.txt")
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()
f.close()
# 文件输出
principal = 1000
rate = 0.05
numyears = 15
year = 1
f = open('out', 'w')   # 打开文件w写入
while year <= numyears:
    principal = principal * (1 + rate)
    print("%3d %0.2f" % (year, principal), file=f)
    year += 1
f.close()


# 交互式地读取
sys.stdout.write("Enter your name :")
name = sys.stdin.readline()
# 简化： name = input("Enter your name :")


# 字符串： str()
# 索引切片: s[1:2]
# 连接: +
# 转换特定格式：format(x, '0.5f')

# 列表：list() 可以包含任意种类的python对象
# 连接: +，append, add, insert

# 读取在命令行上制定的一个文件中的数据列表，然后输入其中的最大值和最小值
if len(sys.argv) != 2:  # 检查命令行参数的数量, sys.argv： 一个从程序外部获取参数的桥梁, 0是这个脚本的名字，1，2…则为命令行下传递的参数.如：
    print("Please supply a filename")
    raise SystemExit(1)
f = open(sys.argv[1])   # 返回'--mode=client'
line = f.readline()
f.close()

# sys.path是对 Python 解释器的系统环境参数的操作，动态的改变 Python 解释器搜索路径（划重点）
#       sys.path会返回一个路径列表，sys.path[0]表示的是当前脚本运行目录
#       牢记知识点：python的两种加载py文件方式，sys.path[0]产生的值会有差异，注意返回列表的第一个值，在工作中注意脚本运行环境，这是个坑
#         方式一：直接运行代码
#         方式二：作为模块脚本来运行
#       假设一个第三方demo.py文件临时存放在E盘，sys.path.append("文件路径") 直接指向搜寻路径
# sys.stdin、sys.stdout、sys.stderr：这三个方法都是文件属性，对应的方法可以读、写、创建文件及编码操作
#      如果需要更好的控制输出，而print不能满足需求，sys.stdout，sys.stdin，sys.stderr就是你需要的


# 元组 tuple()
a = () = (name, ) = name,
# 创建元组后不能修改内容（替换、删除其中的元素），内存占用比列表list（）小
# 循环访问所有记录并展开到一组变量的方法：
portfolio = []
total = 0.0
for name, shares, price in portfolio:
    total += shares * price

# 集合 set()
# 集合是无序的，无法通过数字进行索引，集合中的元素不能重复， 操作：
s = set([3, 5, 9, 10])
t = set("Hello")
# 支持标准操作：
'''
并集： a = t | s
交集： b = t & s
差集： c = t - s
对称差集：d = t ^ s （d = ~b）
'''

# 字典 dict()



















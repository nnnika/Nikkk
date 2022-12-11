# numpy 和 pandas
* numpy是以矩阵为基础的数学计算模块，提供高性能的矩阵运算，数组结构为ndarray。
* pandas是基于numpy数组构建的，
  但二者最大的不同是pandas是专门为处理表格和混杂数据设计的,比较契合统计分析中的表结构，pandas数组结构有一维Series和二维DataFrame。 而numpy更适合处理统一的数值数组数据。
  
# Pandas

- 聚合函数
    `df.agg(func，axis = 0) `   e.g. `L_avg = df0.groupby('labels').agg({'L':np.mean})`

# numpy

- 在start和stop之间返回均匀间隔的数据
    `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)`
- 对array进行拼接的函数
    `numpy.concatenate((a1, a2, ...), axis=0, out=None)`




# 数据清理 
归一化处理，离散化处理，数据变换（log，0-1，exp，box-cox）：
1）0-1标准化：这是最简单也是最容易想到的方法，通过遍历feature vector里的每一个数据，将Max和Min的记录下来，并通过Max-Min作为基数（即Min=0，Max=1）进行数据的归一化处理。

    def MaxMinNormalization(x,Max,Min):
        x = (x - Min) / (Max - Min)
        return x

Z-score标准化：这种方法给予原始数据的均值（mean）和标准差（standard deviation）进行数据的标准化。经过处理的数据符合标准正态分布，即均值为0，标准差为1，这里的关键在于复合标准正态分布，个人认为在一定程度上改变了特征的分布。

    def Z_ScoreNormalization(x,mu,sigma):
        x = (x - mu) / sigma
        return x

# 数据分析过程

## 用户画像

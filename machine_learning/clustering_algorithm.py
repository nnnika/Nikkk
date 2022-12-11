# 聚类数据集
# 使用 make_classification ()函数创建一个测试二分类数据集。
from numpy import where
import sklearn
from matplotlib import pyplot

# -------------------------------------------------------------------------------- #

# 定义数据集
X, y = sklearn.datasets.make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4)

# 获取此类的示例的行索引
row_ix1 = where(y == 1)
row_ix2 = where(y != 1)
# 创建这些样本的散布
pyplot.scatter(X[row_ix1, 0], X[row_ix1, 1], marker='.', color='black', s=8)
pyplot.scatter(X[row_ix2, 0], X[row_ix2, 1], marker='.', color='red', s=8)
# 绘制散点图
pyplot.show()
pyplot.close()

# -------------------------------------------------------------------------------- #

# 亲和力传播聚类 AffinityPropagation
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import AffinityPropagation
from matplotlib import pyplot

# 定义数据集
X, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4)

# 定义模型
model = AffinityPropagation(damping=0.9)
# 匹配模型
model.fit(X)
# 为每个示例分配一个集群
yhat = model.predict(X)

# 检索唯一群集
clusters = unique(yhat)
# 为每个群集的样本创建散点图
for cluster in clusters:
    # 获取此群集的示例的行索引
    row_ix = where(yhat == cluster)
    # 创建这些样本的散布
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
# 绘制散点图
pyplot.show()
pyplot.close()

# -------------------------------------------------------------------------------- #

# K-Mean https://blog.csdn.net/qq_37634812/article/details/78678624
# 优点：原理简单,速度快,对大数据集有比较好的伸缩性
# 缺点：需要指定聚类(数量K), 对异常值敏感, 对初始值敏感

sklearn.cluster.KMeans(n_clusters=8,   # 簇的个数，即你想聚成几类，下面的都不太重要
                       init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0,
                       random_state=None, copy_x=True, n_jobs=1, algorithm='auto'
                       )


# 中心点的选择
# k-meams算法的能够保证收敛，但不能保证收敛于全局最优点，当初始中心点选取不好时，只能达到局部最优点，整个聚类的效果也会比较差。可以采用以下方法：k-means中心点
# 选择彼此距离尽可能远的那些点作为中心点；先采用层次进行初步聚类输出k个簇，以簇的中心点的作为k-means的中心点的输入。
# 多次随机选择中心点训练k-means，选择效果最好的聚类结果（聚类轮廓系数判断）。

# k值的选取 （n_clusters字段）
# k-means的误差函数有一个很大缺陷，就是随着簇的个数增加，误差函数趋近于0

# 当数据量很大的时候，Kmeans 显然还是很弱的，会比较耗费内存速度也会收到很大影响。
# scikit-learn 提供了MiniBatchKMeans算法，大致思想就是对数据进行抽样，每次不使用所有的数据来计算，这就会导致准确率的损失。




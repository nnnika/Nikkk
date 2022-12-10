# 聚类算法
https://blog.csdn.net/lsxxx2011/article/details/124995681
是无监督学习问题。通常被用于发现数据中的有趣模式，例如基于其行为的客户群。
将正常数据与异常值或异常分开可能会被认为是聚类问题； 根据自然行为将集群分开是一个集群问题，称为市场细分。
## scikit-learn
scikit-learn 库提供了一套不同的聚类算法供选择。下面列出了10种比较流行的算法：
1. 亲和力传播 AffinityPropagation
2. 聚合聚类
3. BIRCH
4. DBSCAN
5. K-均值
6. Mini-Batch K-均值
7. Mean Shift
8. OPTICS
9. 光谱聚类
10. 高斯混合

## 聚类轮廓系数
聚类评估算法-轮廓系数（Silhouette Coefficient ）
所有样本的s i 的均值称为聚类结果的轮廓系数，是该聚类是否合理、有效的度量。

        silhouette_score(res_std, clf.labels_))

$ s_i = \frac{b_i - a_i}{max(a_i, b_i)}$
* a_i(样本i的簇内不相似度) - 计算样本i到同簇其他样本的平均距离。ai 越小，说明样本i越应该被聚类到该簇。
* b_i(样本i的簇间不相似度) - 计算样本i到其他簇的所有样本的平均距离，。bi越大，说明样本i越不属于其他簇。

判断：
    si接近1，则说明样本i聚类合理；
    si接近-1，则说明样本i更应该分类到另外的簇；
    若si 近似为0，则说明样本i在两个簇的边界上。

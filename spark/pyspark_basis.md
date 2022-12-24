# Spark
大数据分析计算引擎，分布式计算框架，对任意类型的数据进行自定义计算
RDD 概念：弹性分布式数据集-在大规模集群中做内存运算并有一定的容错方式，计算结果在内存中，延迟小
hadoop生态圈不仅有计算（MR），也有存储（HDF5）和资源管理调度（YARN）
DAG有向无环图：多条链跟随主链，这些链之间大方向相同且不存在环路。

## 模块
SparkCore：核心功能模块，以RDD为数据抽象
SparkSQL：基于SparkCore之上，提供结构化数据的处理模块，支持SQL语言，针对离线计算场景，
升级模块（StructuredStreaming） - 以SparkSQL为基础，进行流式计算
SparkStreaming：有一定缺陷，推荐使用StructuredStreaming
MLlib：以SparkCore为基础，以分布式计算的模式进行机器学习计算
GraphX：图计算

## 运行模式
除了local都是生产环境
1. 本地模式Local 
    - 一个独立的进程（内部的多个线程来模拟），适用开发测试环境
    
2. Standalone模式（集群）
   - 各角色以独立进程的形式存在，组成spark集群环境
    
3. Hadoop Yarn环境（集群）
    - 各角色运行在Yarn的容器内部，组成spark集群环境 （Kubernetes模式也相似）
    
4. 云服务模式（运行在云平台上）

## 架构角色
* Yarn主要有四类角色，分2个层面
    资源管理层面：
        集群资源管理者（Master）：ResourceManager - 集群的资源管理
        单机资源管理者（Worker）：NodeManager - 所在服务器的资源管理
    任务计算层面：
        单任务管理者（Master）：ApplicationMaster - 当前计算任务的管家
        单任务执行者（Worker）：Task（容器内计算框架的工作角色）- 单个任务的执行者
  
* Spark运行角色
Master，Worker， Driver，Executor （一一对应上面的角色，只是叫法不同）
  






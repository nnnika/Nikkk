# 画图工具
import seaborn as sns
import matplotlib.pyplot as plt

## 画柱状图
### sns.barplot()
* 利用矩阵条的高度反映数值变量的集中趋势，以及使用errorbar功能（差棒图）来估计变量之间的差值统计。
    sns.barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None,\
                estimator=<function mean>,ci=95, n_boot=1000, units=None, orient=None,\
                color=None, palette=None, saturation=0.75,\
                errcolor='.26', errwidth=None, capsize=None, dodge=True, ax=None, **kwargs)
重要参数：
1）x,y：data中的变量名词或者向量；
hue:data中的变量名词或者向量,用于分类，类似分类标签；
2）orient:< “v” 或 “h” >
绘图的方向（垂直或水平）。这通常是从输入变量的数据类型推断出来的，但是可以用来指定“分类”变量是数字还是宽格式数据。
3）estimator：可回调函数，设置每个分类箱的统计函数；
4）errwidth：float类型，表示误差线的厚度；errcolor：表示置信区间的线条颜色； (errorbar功能（差棒图）)
5）estimator：设置对每类变量的计算函数，默认为平均值，可修改为max、median、max等；

### sns.countplot()
使用条形显示每个分箱器中的观察计数。
sns.countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, dodge=True, ax=None, **kwargs)

    ax = sns.countplot()
    # patches指每一个立柱，在每个立柱上增加对应的数字
    for p in ax.patches:  
        height = p.get_height()
        ax.text(x = p.get_x() + (p.get_width() / 2), y = height + 500, s = '{:.0f}'.format(height), ha = 'center')
        或
        # 在每个矩形上增添数值
        ax.annotate(f'\n{p.get_height()}', (p.get_x(), p.get_height()+50), color='black', size=15)


fig,ax = plt.subplots(figsize=(20,10), dpi=80)# 确定图的位置
ax.set_title("巡数分布") # 给图增加title
sns.countplot(x="totalsplist",data=tlj_data) #左图
#在直方图上显示具体数值
for p in ax.patches:
	# 在每个矩形上增添数值
    ax.annotate(f'\n{p.get_height()}', (p.get_x(), p.get_height()+50), color='black', size=15)

plt.show()




### sns.boxplot()
箱形图（Box-plot），又称为盒须图、盒式图或箱线图，是一种用作显示一组数据分散情况资料的统计图。它能显示出一组数据的最大值、最小值、中位数及上下四分位数。
seaborn.boxplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, width=0.8, dodge=True, fliersize=5, linewidth=None, whis=1.5, notch=False, ax=None, **kwargs)


## 饼图
直接用axs.pie(x(列表), explode=None, labels(分类)=None, colors=None, autopct比例=None('%.2f%%''), \
            pctdistance比例位置=0.6, shadow=False, labeldistance=1.1, startangle=0, \
            radius=1, counterclock=True, wedgeprops=None(中间挖洞{width: 0.4}), textprops=None, center=(0, 0), \ 
            frame=False, rotatelabels=False, *, normalize=None, data=None)

## 雷达图（聚类）
    1. 设置每个数据点的显示位置，在雷达图上用角度表示
        `angles=np.linspace(0, 2*np.pi,len(values), endpoint=False)`
    2. 拼接数据首尾，使图形中线条封闭
        `values=np.concatenate((values,[values[0]]))`
        `angles=np.concatenate((angles,[angles[0]]))`
    3. 绘图
        `fig=plt.figure()`
    4. 设置为极坐标格式
        `ax = fig.add_subplot(111, polar=True)`
    5. 绘制折线图
        `ax.plot(angles, values, 'o-', linewidth=2)`
    6. 设置为极坐标格式
        `ax = fig.add_subplot(111, polar=True)`
    7. 随机取不同的颜色
        `colors = np.random.choice(['r', 'g', 'b', 'y', 'k', 'orange'], replace = False, size = len(centers))`
    8. 填充颜色
        `ax.fill(angles, values, c=colors, alpha=0.25)`
    9. 设置图标上的角度划分刻度，为每个数据点处添加标签
        `ax.set_thetagrids(angles * 180/np.pi, feature)`
    10. 设置雷达图的范围
        `ax.set_ylim(0,5)`
    11. 添加标题
        `plt.title('活动前后员工状态表现')`
    12. 添加网格线
        `ax.grid(True)`
        `plt.show()`


## 其他操作
### 子图加标题
axs.set_title('')
### 增加一条垂直线
axes.axvline(self, x=0, ymin=0, ymax=1， **kwargs) 
### 保存图片
plt.savefig('./xxx.png')
# 利用 Pandas 进行分类数据编码的十种方式


## 连续型数据的转换
根据分数列的值，来新增一列标签，即如果分数大于90，则标记为A，分数在80-90标记为B，以此类推。

### 自定义函数 + 循环遍历
df1 = df.copy()
def myfun(x):
    if x>90:
        return 'A'
    elif x>=80 and x<90:
        return 'B'
    else:
        return 'E'
df1['Score_Label'] = None
for i in range(len(df1)):
    df1.iloc[i,3] = myfun(df1.iloc[i,2])

### 自定义函数 + map
df2 = df.copy()
def myfun(x):
    if x>90:
        return 'A'
    elif x>=80 and x<90:
        return 'B'
    else:
        return 'E'
df2['Score_Label'] = df2['Score'].map(mapfun)

### 自定义函数 + apply
df3 = df.copy()
df3['Score_Label'] = df3['Score'].apply(lambda x: 'A' if x > 90 else ('B' if 90 > x >= 80 else 'E'))))

###  pd.cut
df4 = df.copy()
bins = [0, 59, 70, 80, 100]
df4['Score_Label'] = pd.cut(df4['Score'], bins)
df4['Score_Label_new'] = pd.cut(df4['Score'], bins, labels=['low', 'middle', 'good', 'perfect'])

### sklearn 二值化
df5 = df.copy()
binerize = Binarizer(threshold = 60)  # 以60分为线，分为及格与不及格
trans = binerize.fit_transform(np.array(df1['Score']).reshape(-1,1))
df5['Score_Label'] = trans

## 文本性数据
打标签
### 使用 replace
df6 = df.copy()
df6['Sex_Label'] = df6['Sex'].replace(['Male','Female'],[0,1])

但要是类别很多，也可以使用pd.value_counts()来自动指定标签，例如对Course Name列分组

df6 = df.copy()
value = df6['Course Name'].value_counts()
value_map = dict((v, i) for i,v in enumerate(value.index))
df6['Course Name_Label'] = df6.replace({'Course Name':value_map})['Course Name']

### map
额外强调的是，新增一列，一定要能够想到map
df7 = df.copy()
Map = {elem:index for index,elem in enumerate(set(df["Course Name"]))}
df7['Course Name_Label'] = df7['Course Name'].map(Map)

### astype
df8 = df.copy()
value = df8['Course Name'].astype('category')
df8['Course Name_Label'] = value.cat.codes

### sklearn
from sklearn.preprocessing import LabelEncoder
df9 = df.copy()
le = LabelEncoder()
le.fit(df9['Sex'])
df9['Sex_Label'] = le.transform(df9['Sex'])
le.fit(df9['Course Name'])
df9['Course Name_Label'] = le.transform(df9['Course Name'])

一次性转换两列也是可以的:
df9 = df.copy()
le = OrdinalEncoder()
le.fit(df9[['Sex','Course Name']])
df9[['Sex_Label','Course Name_Label']] = le.transform(df9[['Sex','Course Name']])

### pd.factorize
df10 = df.copy()
df10['Course Name_Label'] = pd.factorize(df10['Course Name'])[0]

结合匿名函数，我们可以做到对多列进行有序编码转换

df10 = df.copy()
cat_columns = df10.select_dtypes(['object']).columns
df10[['Sex_Label', 'Course Name_Label']] = df10[cat_columns].apply(lambda x: pd.factorize(x)[0])




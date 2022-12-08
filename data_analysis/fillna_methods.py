import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# 随机森林填充

data = pd.DataFrame()
miss_list = data[:, 0]

for i in miss_list:
    '''
    特征矩阵和标签之前存在着某种关系，那么特征和标签是可以相互转化的
    e.g. 可以用地区，环境，附近学校数量预测房价
    '''
    # 依次将待填充特征称为新的标签，缺失越大的放在越后面
    new_label = data.iloc[:, i]
    # 根据缺失情况划分训练集和测试集
    y_train = new_label[new_label.notnull()]
    y_test = new_label[new_label.isnull()]
    x_train = data.iloc[y_train.index]
    x_test = data.iloc[y_test.index]
    # 其他特征的缺失部分仍要填充一个值，具体数值像上面所说，要考虑是否出现过
    x_train = x_train.fillna(0)
    x_test = x_test.fillna(0)
    # 训练RF回归模型，预测缺失特征的取值
    rfr = RandomForestRegressor(random_state=0, n_estimators=1000, n_jobs=-1)
    rfr = rfr.fit(x_train, y_train)
    Y_predict = rfr.predict(x_test)
    # 预测值回填到原始数据中
    data.iloc[y_test.index, i] = Y_predict

# SQL 函数

## 一、聚合函数

聚合函数:返回汇总值 （它对其应用的每个行集返回一个值）
AVG(表达式) 返回表达式中所有的平均值。仅用于数字列并自动忽略NULL值。
COUNT(表达式) 返回表达式中非NULL值的数量。可用于数字和字符列。
COUNT(*) 返回表中的行数(包括有NULL值的列)。
MAX(表达式) 返回表达式中的最大值,忽略NULL值。可用于数字、字符和日期时间列。
MIN(表达式) 返回表达式中的最小值,忽略NULL值。可用于数字、字符和日期时间列。
SUM(表达式) 返回表达式中所有的总和,忽略NULL值。仅用于数字列。

## 二、转换函数

CONVERT(data_type[(length)], expression [, style])
    `Select convert(varchar(10) ,stuno) as stuno,stuname from student`
CAST( expression AS data_type )
    `Select cast(stuno as varchar(10)) as stuno,stuname from student`
CAST 和 CONVERT 提供相似的功能，只是语法不同。在时间转化中一般用到convert,因为它比cast多加了一个style,可以转化成不同时间的格式。

## 三、日期函数

GETDATE() 当前的系统日期。
    `select GETDATE()`  --结果：2020-10-19 15:34:27.343
DATEADD(日期部分,number,date) 返回带有指定数字(number)的日期(date),该数字添加到指定的日期部分(datepart)
    `select DATEADD(dd, 5, getdate())`  --增加5天时间
DATEDIFF(日期部分,date1,date2) 返回两个日期中指定的日期部分之间的差值
    `select DATEDIFF(mm, '2010-1-1', '2010-3-1 00:00:00')`  --结果：2
DATENAME(日期部分,date) 返回日期中日期部分的字符串形式
    `select DATENAME(dw,GETDATE())` --结果：星期二
DATEPART(日期部分,date) 返回日期中指定的日期部分的整数形式
    `select DATEPART(dw,GETDATE())` --结果(返回今天是一周中的第几天)：3
YEAR(date) 返回指定日期的年份数值
    `select YEAR(GETDATE())` --结果：2020
MONTH(date)返回指定日期的月份数值
DAY(date)返回指定日期的天数值

注：
* DATENAME 和 DATEPART 的区别，返回的值类型不同，一个是VARCHAR一个是INT，另外就是星期会用本地语言来表示

* 当显示日期列的内容时如果只显示年月日部分,可以使用CONVERT转换函数对日期列进行转换
    CONVERT(VARCHAR(10),日期字段名,120) --120 为日期格式YYYY-MM-DD
    SELECT CONVERT(VARCHAR(10),盘点日期,120) AS 盘点日期 FROM 原材料盘点日期明细表

* SQL中日期的表示方法及有效范围,如下:

日期部分	缩写	值	日期部分	缩写	值
年	yy	1753-9999	周	wk	1-53
季度	qq	1-4	小时	hh	0-23
月	mm	1-12	分钟	mi	0-59
一年中的天	dy	1-366	秒	ss	0-59
一月中的天	dd	1-31	毫秒	ms	0-999
一周中的天	dw	1-7	

## 四、数学函数

CEILING(num_expr) 返回大于或等于数值表达式的最小整数。
FLOOR(num_expr) 返回小于或等于数值表达式的最大整数
FIRST() 返回在指定的域中第一个记录的值
LAST() 返回在指定的域中最后一个记录的值

ABS(num_expr) 返回数值表达式的绝对值。
SIGN(num_expr) 对正数执行+1操作,对负数和零执行-1操作。
ROUND(num_expr,length) 对数值表达式截取指定的整数长度,返回四舍五入后的值。
RAND([seed]) 随机返回的到之间的近似浮点值,可以对seed指定为整数表达式(可选)。

SQUARE(float_expr) 返回浮点表达式的平均值。
SQRT(float_expr) 返回指定的近似浮点表达式的平方根。
POWER(num_expr,y) 返回幂为y的数值表达式的值。
STDEV() 返回基于样本估计标准偏差
VAR() 返回基于样本估计方差

ACOS(float_expr) 返回角(以弧度表示),它的余弦值近似于指定的浮点表达式。
COS(float_expr) 返回以浮点表达式表示的近似于指定角度(以弧度表示)的余弦三角函数的值。
ASIN(float_expr) 返回角(以弧度表示),它的正弦值近似于指定的浮点表达式。
SIN(float_expr) 返回以浮点表达式表示的近似于指定角度(以弧度表示)的正弦三角函数的值。
ATAN(float_expr) 返回角(以弧度表示),它的正切值近似于指定的浮点表达式。
TAN(float_expr) 返回以浮点表达式表示的近似于指定角度(以弧度表示)的正切三角函数的值。
ATN2(float_expr1, float_expr2) 返回角(以弧度表示),它的正切值在两个近似的浮点表达式之间。
COT(float_expr) 返回以浮点表达式表示的近似于指定角度(以弧度表示)的余切三角函数的值。

DEGREES(num_expr)返回数值表达式表示的弧度值对应的度值。
RADIANS(num_expr) 返回数值表达式表示的度值对应的弧度值。

EXP(float_expr) 根据指定的近似浮点表达式,返回指数值。
LOG(float_expr) 根据指定的近似浮点表达式,返回自然对数值。
LOG10(float_expr) 根据指定的近似浮点表达式,返回以为底的对数。

PI() 返回常量值3.141592653589793


## 五、字符串函数

字符串函数:对字符串、二进制数据或表达式执行操作（可用于binary 和varbinary数据类型列,但主要用于char和varchar数据类型）

+ 返回两个表达式的组合形式的字符串。
STR(float_expr[,length[,decimal]]) 返回浮点表达式的字符串表示法。
LEN(char_expr) 返回字符表达式的长度。
REVERSE(char_expr) 反转字符表达式。
UPPER(char_expr) 将字符表达式全部转换为大写。
LOWER(char_expr) 将字符表达式全部转换为小写。

STUFF(char_expr1,start,length,char_expr2) 使用字符表达式替换字符表达式的一部分字符,从指定的位置开始替换指定的长度。
SUBSTRING(char_expr,start,length) 返回从字符表达式的指定位置开始,截取指定长度得到的字符集。
LEFT(char_expr,int_expr) 返回从字符表达式最左端起根据指定的字符个数得到的字符。
RIGHT(char_expr,int_expr) 返回从字符表达式最右端起根据指定的字符个数得到的字符。

SPACE(int_expr) 返回包含指定空格数的字符串。
LTRIM(char_expr) 返回删除掉前面空格的字符表达式。
RTRIM(char_expr) 返回删除掉其后空格的字符表达式。

CHARINDEX('pattern',char_expr) 返回字符表达式中指定模式的起始位置。
PATINDEX('%pattern%',expr) 返回表达式中模式第一次出现的起始位置。返回表示不存在模式形式。

SOUNDEX(char_expr) 评估两个字符串的相似度后得到的位代码。
REPLICATE(char_expr,int_expr) 返回重复指定次数的字符表达式产生的字符串。
DIFFERENCE(char_expr1,char_expr2) 根据比较两个字符表达式的相似度,返回到之间的值。表示匹配度最佳。

ASCII(char_expr) 返回表达式最左边字符的ASCⅡ代码值。
CHAR(int_expr) 返回到之间的整数表达式的ASCⅡ字符值。如果输入的值不在有效范围内,则返回NULL。


## 六、系统函数
从数据库返回在SQLSERVER中的值、对象或设置的特殊信息（用于返回元数据或配置设置）

DB_ID([‘database_name']) 返回数据库的标识号。
DB_NAME([database_id]) 返回数据库的名称。
GETANSINULL([‘database_name']) 返回数据库的默认空性(Nullability)。

COL_NAME(table_id,column_id) 返回指定的表中的列名。
COL_LENGTH('table_name','column_name') 返回列的长度。
COALESCE(expr1,expr2, xprN) 返回第一个非NULL表达式。

DATALENGTH('expr') 返回任何数据类型的实际长度。
INDEX_COL('table_name',index_id,key_id) 返回索引的列名。
STATS_DATE(table_id,index_id) 返回上次更新指定索引的统计的日期。
IDENT_INCR('table_or_view') 有新的记录添加入到表中时计数加。
IDENT_SEED('table_or_view') 返回标识列的起始编号。

ISNULL(expr,value) 使用指定的值替换的NULL表达式。
NULLIF(expr1,expr2) Expr1与Expr2相等时,返回Null。

OBJECT_ID('obj_name') 返回数据库对象标识号。
OBJECT_NAME('object_id') 返回数据库对象名。

HOST_ID() 返回工作站的标识号。
HOST_NAME() 返回工作站的名称。

SUSER_SID([‘login_name']) 返回用户的登录标识号。
SUSER_ID([‘login_name']) 返回用户的登录标识号。这个函数类似于SUSER_SID()函数,并且保留了向后的兼容性。
SUSER_SNAME([server_user_id]) 返回用户的登录标识号。
SUSER_NAME([server_user_id]) 返回用户的登录标识号。这个函数类似于SUSER_SNAME()函数,并且保留了向后的兼容性。

USER_ID('user_name') 返回用户的数据库标识号。
USER_NAME(['user_id']) 返回用户的数据库名称。


## 七、文本和图像函数
对文本和图像数据执行操作（通常返回有关文本和图像数据所需的信息。文本和图像数据是以二进制格式的形式进行存储的）

TEXTPTR(col_name) 返回varbinary格式的文本指针值。对文本指针进行检查以确保它指向第一个文本页。
TEXTVALID('table_name.col_name',text_ptr)检查给定的文本指针是否有效。返回表示有效,返回表示指针无效。

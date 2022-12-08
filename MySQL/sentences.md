# 1.DDL数据库操作（dataBase definition language(数据定义语言)

## 数据库
### 查看指定数据库创建时的sql指令
`show databases`
### 创建特定数据库或表的MySQL语句
`SHOW CREATE DATABASE XX
SHOW CREATE TABLE`
### 创建数据库
`CREATE DATABASE XX`
### 创建数据库 如果不存在
`CREAT DATABASE IF NOT EXISTS XX`
### 创建数据库 并设置编码
`CREAT DATABASE IF NOT EXISTS XX CHARACTER SET UTF8`
### 删除数据库
`DROP DATABASE IF EXISTS XX`

## 数据表
### 查看所有数据表
`SHOW TABLES`
### 查看表的详情
`DESC TXX`
### 删除表如果表存在
`DROP TABLES IF EXISTS TXX`
### 修改表名
`ALTER TABLES TXX RENAME XX`
### 修改表的字符集，默认和数据库一样
`ALTER TABLES XX CHARACTER SET UTF8`
### 添加字段  
char长度固定，verchar长度可变（节约空间）
`ALTER TABLES XX ADD COL VARCHAR(100)`
### 删除字段
`ALTER TABLES XX DROP COLOUMN COL`
### 修改字段的类型
`ALTER TABLES XX MODIFY COL VARCHAR(150)`
### 修改字段的列名和类型
`ALTER TABLES XX CHANGE XX CXX VARCHAR(5)`
### 删除表的主键约束
`ALTER TABLES XX DROP PRIMARY KEY`
### 删除表的外键约束 (删除需要带上外键名称) 
用来实现数据库的参照完整性的,外键约束可以使两张表紧密的结合起来,特别是针对修改或者删除的级联操作时,会保证数据的完整性。
外键是指表中某个字段的值依赖于另一张表中某个字段的值,而被依赖的字段必须具有主键约束或者唯一约束。
被依赖的表我们通常称之为父表或者主表,设置外键约束的表称为子表或者从表。
`ALTER TABLE XX DROP FOREIGN KEY COL`
### 添加表的主键约束
`ALTER TABLE MODIFY COL VARCHAR(30) PRIMARY KEY`
常见约束:
1.非空约束（not null)： 限制此列的值必须提供，不能为null
2.唯一约束（unique)： 在表中该列的值不能重复
3.主键约束（primary key）: 非空+唯一 能够唯一标识数据表中的一条数据
4.外键约束（foreign key）: 建立不同表之间的关联关系

# 2.DML数据库操作 （dataBase Manipulation language(数据操作语言)
## 插入语句
`INSERT INTO TABLE VALUES ('1', '张三')`
`INSERT INTO TABLE(ID) VALUES ('张三')`
## 删除语句
`DELECT FROM TABLE`
## 修改语句
`UPDATE TABLE SET ID='1', NAME='张三' WHERE ID='1'`


# 3.DQL数据库操作（dataBase query language(数据查询语言)）
## 多条件查询连接关键字
（and, or，not(取反)）
`SELECT * FROM TABLE WHERE COL NOT BETWEEN '1' AND '2'`
## 模糊查询
（%表示任意多个字符，_表示一个字符）
`SELECT * FROM TABLE WHERE COL LIKE '%12-01'`
## 查询去重复
`SELECT DISTINCT * FROM TABLE`
## 排序asc(升序)desc（降序）先按照id进行排序，如果id相同的再通过name排序
`SELECT * FROM TABLE ORDER BY ID DESC, NAME DESC`
## 日期函数
获得当前时间 用 now() 或者 sysdate()
向日期类型的列添加数据时，可以通过字符串类型赋值（字符串格式必须为yyyy-MM-dd hh:mm:ss）
## 字符串函数
UPPER(), LOWER()
`SELECT UPPER(NAME) FROM TABLE`
substring()截取字符串，concat(col,col)合并字符串
`SELECT SUBBSTRING(NAME, 1, 1) FROM TABLE`
`SELECT CONCAT(ID, '-', NAME) FROM TABLE`
## 分组查询（group by）
只有出现 group by 时才可以使用 having（对分组后的数据进行过滤）
`SELECT ID, COUNT(NUMBER), TYPE FROM TABLE WHERE ID >= 1 GROUP BY TYPE HAVING COUNT(NUMBER)>0`
## 分页查询（limit）
`SELECT * FROM TABLE LIMIT 100`

# 数据表的关联关系
1. 一对一关联
    主键关联--两张数据表中 主键相同的数据为相互对应的数据
    唯一外键--在任意一张表中添加一个字段添加外键约束与另一张表主键关联，并将外键添加唯一约束。
2. 一对多，多对一
    设置外键--在多的一方表中添加一个字段添加外键约束与另一张表主键关联。
3. 多对多
    新建关系表--在关系表中定义两个外键，分别与两个数据表的主键相关联。
## 外键的创建
1.在创建表的时候创建
    `create table class(
        class_id int primary key auto_incremment,
        class_name varchar(32) not null unique,
        class_remark varchar(200))`
    
    `create table student(
        stu_num varchar(32) primary key,
        stu_name varchar(32) not null unique,
        cla_id int,
        constraint PK_STUDENT_CLASS foreign key(cla_id) references class(class_id))`  
注意最后一段constraint，外键名为PK_STUDENT_CLASS

2.创建好表后在给其添加外键
`alter table student add constraint FK_STUDENT_CLASS foreign key(cla_id) references class(class_id)`

3.外键约束-级联操作 在创建外键时 添加 级联操作
on update cascade（级联修改）
on delete cascade (级联删除)
`alter table student add 
    constraint FK_STUDENT_CLASS foreign key(cla_id) references class(class_id) on update cascade on delete cascade`

## 连接查询
笛卡尔积（A表&B表）：使A表中的每条记录和B表中的每条记录关联，笛卡尔积的总数 = A表记录的数量*B表记录的数量
### 内连接查询（inner join）
- 如果直接执行连接查询会生成两张表的笛卡尔积(即用student表中的每条记录去和class表中的每条记录相匹配)
`SELECT * FROM STUDENT INNER JOIN CLASS`

连接条件
1.where：是在两张表产生笛卡尔积后，在通过条件来对生成的笛卡尔积进行筛选的（效率不高）
select * from student inner join class where student.cls_id = class.class_id
2.on : 通过on设置两张表进行连接查询的匹配条件（效率高）
select * from student inner join class on student.cls_id = class.class_id 
 结果：只获取两张表中匹配条件成立的数据，任意一张表在另一张表，如果没有找到对应的匹配则不会出现在查询结果中

### 左连接 (left join) 右连接（right join）
结果：显示左边表中的所有数据，如果在右表中有对应的匹配关系，则进行匹配，如果右表中不存在匹配数据，则显示为null
select * from student left join class on student.cla_id = class.class_id

## 子查询/嵌套查询
### 单列多行（作为查询条件）
//查询所有在Java班级的同学(两张表)
select * from student where cla_id in (select class_id from class where class_name like 'java%')
### 多行多列（作为虚拟表）
//查询所有在java班并且性别是男的同学
select * from (select * from student where cla_id in (select class_id from class where class_name like 'java%')) as t where t.stu_sex = '男'









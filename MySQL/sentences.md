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
`DELETE FROM TABLE` \
删除重复的邮件 \
`delete p1
 from Person p1, Person p2
 where p1.email = p2.email and p1.id > p2.id`
## 修改语句
`UPDATE TABLE SET ID='1', NAME='张三' WHERE ID='1'` \
男女性别互换 \
`update Salary set sex = 
     case
     when sex = 'f' then 'm'
     else 'f'
     end`


# 3.DQL数据库操作（dataBase query language(数据查询语言)）
## 多条件查询连接关键字
（and, or，not(取反)） \
`SELECT * FROM TABLE WHERE COL NOT BETWEEN '1' AND '2'`
## 模糊查询
（%表示任意多个字符，_表示一个字符） \
`SELECT * FROM TABLE WHERE COL LIKE '%12-01'`
## 查询去重复
`SELECT DISTINCT * FROM TABLE`
## 排序asc(升序)desc（降序）先按照id进行排序，如果id相同的再通过name排序
`SELECT * FROM TABLE ORDER BY ID DESC, NAME DESC`
## 日期函数
获得当前时间 用 now() 或者 sysdate()
向日期类型的列添加数据时，可以通过字符串类型赋值（字符串格式必须为yyyy-MM-dd hh:mm:ss）
## 判断归类（打标签）
`if(T1.grade >= 8, T2.name, null) as name`  如果成绩小于8，用null替换名字 \
或者     `case when T1.grade>=8 then T2.name else 'NULL' end as name`
`T1 inner join T2 on T2.marks between T1.min_mark and T2.max_mark` 表关联并打标签
## 字符串函数
- UPPER(), LOWER() \
`SELECT UPPER(NAME) FROM TABLE` 
- substring()截取字符串，concat(col,col)合并字符串 \
e.g. `select distinct(city) from station where substring(city, 1, 1) in ('a', 'e', 'i', 'o', 'u'); ` \
或者： `SELECT left(NAME, 1) FROM TABLE` 从左边数起第一个 \
`SELECT CONCAT(ID, '-', NAME) FROM TABLE`
修复名字，只有第一个字符是大写的，其余都是小写的
`select
     user_id,
     concat(upper(left(name, 1)), lower(substring(name, 2, length(name)))) as name
 from Users`
- Group_concat() 将一列的数据转成一行列表 [a,b,c]
group_concat( [distinct] 要连接的字段 [order by 排序字段 asc/desc ] [separator '分隔符'] )
  e.g. `group_concat(distinct product order by product asc separator ',') as products`
# 判断字符串是否包含某个字符串
`SELECT * FROM ‘表名’ WHERE LOCATE(‘包含的字符串’,‘字段’) > 0`
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
`select * from student inner join class where student.cls_id = class.class_id`
2.on : 通过on设置两张表进行连接查询的匹配条件（效率高）
`select * from student inner join class on student.cls_id = class.class_id` 
 结果：只获取两张表中匹配条件成立的数据，任意一张表在另一张表，如果没有找到对应的匹配则不会出现在查询结果中

### 左连接 (left join) 右连接（right join）
结果：显示左边表中的所有数据，如果在右表中有对应的匹配关系，则进行匹配，如果右表中不存在匹配数据，则显示为null
`select * from student left join class on student.cla_id = class.class_id`

## 子查询/嵌套查询
### 单列多行（作为查询条件）
//查询所有在Java班级的同学(两张表)
select * from student where cla_id in (select class_id from class where class_name like 'java%')
### 多行多列（作为虚拟表）
//查询所有在java班并且性别是男的同学
select * from (select * from student where cla_id in (select class_id from class where class_name like 'java%')) as t where t.stu_sex = '男'



## JOIN和UNION区别
- join 是两张表做交连后里面条件相同的部分记录产生一个记录集。 （横向延伸）
- union是产生的两个记录集(字段要一样的)并在一起，成为一个新的记录集 。 （纵向延伸）
### JOIN
join [等同于 inner join] 取两个表的交集
full join [等同于 full outer join] 取两个表的并集，对于没有匹配的记录默认为 NULL （mysql用不了？）
left(right) join [等同于 left outer join] 产生表A的完全集，而B表中匹配的则有值，没有匹配的则以null值取代。
cross join 笛卡尔积，N*M的一个结果集
### UNION
union 与 union all
        UNION 操作符用于合并两个或多个 SELECT 语句的结果集。
        请注意，UNION 内部的 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每条 SELECT 语句中的列的顺序必须相同。
        UNION和UNION ALL的区别：
            union 检查重复
            union all 不做检查

JOIN的基本语法：
`Select table1.* FROM table1 JOIN table2 ON table1.id=table2.id`
UNION的基本语法：
`SELECT * FROM TABLE_A UNION SELECT * FROM TABLE_B`


## group by & having 
`SELECT *|字段列表 FROM 表名 [WHERE 子句] [GROUP BY 子句][HAVING 子句][ORDER BY 子句][LIMIT 子句]`
使用了having必须使用group by，但是使用group by 不一定使用having。
* having是在分好组后找出特定的分组，通常是以筛选聚合函数的结果，如sum(a) > 100等 
* 分组函数常用到的聚合函数：
    1. MIN 最小值 
    2. MAX 最大值 
    3. SUM 求和
    4. AVG 求平均
    5. COUNT 计数
* 不允许使用双重聚合函数，所以在对分组进行筛选的时候，可以用order by 排序，然后用limit也可以找到极值。

## 行转列，列转行：改变表格结构
https://blog.csdn.net/m0_68850571/article/details/124300784 \
行转列用case...when或if分类讨论, group by进行分组 。 sum/max为聚合作用

    select 
        date, 
        sum(if(新列表名='旧列表名1', 1, 0)) '旧列表名1',
        sum(if(新列表名='旧列表名2', 1, 0)) '旧列表名2'
    from table
    group by date;

    select  name,
            max(case when subject='语文' then score else 0  end) as 语文,
            max(case when subject='数学' then  score else 0 end) as 数学, 
            max(case when subject='英语' then score else 0  end) as 英语 
    from test 
    group by name;
列转行用union或union all将多列的字段整合到一行。

    select product_id, 'store1' as store, store1 as price from Products where store1 is not null
    union all
    select product_id, 'store2' as store, store2 as price from Products where store2 is not null
    union all
    select product_id, 'store3' as store, store3 as price from Products where store3 is not null

## 取第二大的值
方法一： 排除掉最大值，那就是第二大

    select
        max(salary) as SecondHighestSalary
    from Employee
    where salary < (select max(salary) from Employee) 
    order by salary desc
    limit 2

方法二: 采用limit offset(跳过)来处理

    select (
        select distinct salary
        from employee
        order by salary DESC
        limit 1 offset 1
    ) as secondhighestsalary;




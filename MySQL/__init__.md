# sql语句形式
    (8) SELECT (9)DISTINCT<select_list>
    (1) FROM <left_table>
    (3) <join_type> JOIN <right_table>
    (2)         ON <join_condition>
    (4) WHERE <where_condition>
    (5) GROUP BY <group_by_list>
    (6) WITH {CUBE|ROLLUP}
    (7) HAVING <having_condition>
    (10) ORDER BY <order_by_list>
    (11) LIMIT <limit_number>

执行顺序：
(1) FROM:对FROM子句中的左表<left_table>和右表<right_table>执行笛卡儿积，产生虚拟表VT1;
(2) ON: 对虚拟表VT1进行ON筛选，只有那些符合<join_condition>的行才被插入虚拟表VT2;
(3) JOIN: 如果指定了OUTER JOIN(如LEFT OUTER JOIN、RIGHT OUTER JOIN)，那么保留表中未匹配的行作为外部行添加到虚拟表VT2，产生虚拟表VT3。如果FROM子句包含两个以上的表，则对上一个连接生成的结果表VT3和下一个表重复执行步骤1~步骤3，直到处理完所有的表;
(4) WHERE: 对虚拟表VT3应用WHERE过滤条件，只有符合<where_condition>的记录才会被插入虚拟表VT4;
(5) GROUP By: 根据GROUP BY子句中的列，对VT4中的记录进行分组操作，产生VT5;
(6) CUBE|ROllUP: 对VT5进行CUBE或ROLLUP操作，产生表VT6;
(7) HAVING: 对虚拟表VT6应用HAVING过滤器，只有符合<having_condition>的记录才会被插入到VT7;
(8) SELECT: 第二次执行SELECT操作，选择指定的列，插入到虚拟表VT8中;
(9) DISTINCT: 去除重复，产生虚拟表VT9;
(10) ORDER BY: 将虚拟表VT9中的记录按照<order_by_list>进行排序操作，产生虚拟表VT10;
(11) LIMIT: 取出指定街行的记录，产生虚拟表VT11，并返回给查询用户


# sql 存储过程：
存储过程是在大型数据库系统中 , 一组为了完成特定功能的 SQL 语句集 , 存储在数据库中;
经过第一次编译后再次调用不需要再次编译 , 用户通过指定存储过程的名字并给出参数来执行它存储过程是数据库中的一个重要对象 ; 
存储过程中可以包含 逻辑控制语句 和 数据操纵语句 , 它可以接受参数 , 输出参数 , 返回单个或多个结果集以及返回值 ;
## 简单创建一个存储过程
    create procedure GetUsers()
    begin 
        select * from user; 
    end;
### 调用存储过程
    call GetUsers();
### 删除存储过程
    deop procedure if exists GetUsers;
## 带参数的存储过程
MySql 支持 IN (传递给存储过程) , OUT (从存储过程传出) 和 INOUT (对存储过程传入和传出) 类型的参数
通过指定INTO关键字保存到相应的变量 

    create procedure GetScores(
        out minScore decimal(8,2),
        out avgScore decimal(8,2),
        out maxScore decimal(8,2)
    )
    begin
        select min(score) into minScore from user;
        select avg(score) into avgScore from user;
        select max(score) into maxScore from user;
    end;

### 调用此存储过程 , 必须指定3个变量名(所有 MySql 变量都以 @ 开始)
    call GetScores(@minScore, @avgScore, @maxScore);
    select @minScore, @avgScore, @maxScore;
### 使用 IN 参数 , 输入一个用户 id , 返回该用户的名字 :
    create procedure GetNameByID(
        in userID int,
        out userName varchar(200)
    )
    begin
        select name from user
        where id = userID
        into userName;
    end;

    call GetNameByID(1, @userName);
    select @userName;



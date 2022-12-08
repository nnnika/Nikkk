# 存储过程
https://blog.csdn.net/m0_51516106/article/details/125291443

## 存储过程优点：
 1.SQL指令无需客户端编写，通过网络传送，可以节省网络开销，同时避免SQL指令在网络传输过程中被恶意篡改保证安全性；
 2.存储过程经过编译创建并保存在数据库中，执行过程无需重复进行编译，对SQL执行过程进行了性能优化。
3.存储过程中多个SQL指令之间存在逻辑关系，支持流程控制语句，可以实现复杂的业务。
## 存储过程的缺点
1.存储过程是根据不同的数据库进行编译，创建并存储在数据库中的，当我们需要更换数据库时，需要从新编写存储过程。
2.存储过程受限于数据库产品，如果需要高性能的优化会成为一个问题。
3.如果需要对数据库高并发访问，使用存储过程会增加数据库的连接执行时间（因为存储过程是把复杂的业务交给了数据库处理）

### 创建一个加法的存储过程：
    create procedure add_num (in a int,in b int,out c int)
    begin
    set c = a + b;
    end 
### 调用存储过程
    set @m = 0 ; -- 定义用户变量（全局变量） @m
    call add_num(3,2,@m) -- 调用存储过程获得结果赋值给@m
    select @m from dual; -- 参看变量值
 
局部变量：定义在存储过程中的变量，只能在存储过程内部使用。（必须定义在存储过程开始）
用户变量：相当于全局变量，存放在mysql数据库的数据字典中（dual），使用set关键字直接定义，变量名要以@开头
存储过程参数：in(入参)，out（出参），inout(即可当入参，又可当出参)

## 存储过程中流程控制
### 1.分支语句 if-then-else
 
#### 单分支语句
    create procedure proce_test ( in a int ) begin
        if
            a = 1 then
                insert into student    values    ( '202203', '王二', '5', '男' ) ;
            end if;
        end
    call proce_test(1)
 
#### 双分支语句
    create procedure proce_test2 ( in a int ) begin
        if
            a = 1 then
                insert into student    values ( '202204', '小红', '5', '女' );
            else insert into class values ( '2', 'mysql2022', '很棒' );
        end if;
        end
 
### 2.多分支 case when
    create procedure proce_test2 (in a int) begin
        case a
            when 1 then
                insert into student    values ( '202204', '小红', '5', '女' );
            when 2 then
                insert into class values ( '2', 'mysql2022', '很棒' );
            else --如果不符合上面的条件就执行else中的
                insert into class values ( '2', 'mysql2022', '很棒' );
        end case;
    end;
 
## 循环语句
# while循环 向class表中循环添加数据
create procedure add_class(in num int)
    begin
    declare x int default 0;
    while 
        x < num do 
        insert into class(class_name,class_remark) values (concat('java',x),x);
    set x = x + 1;
    end while;
    end 
 
# repeat循环 向class表中循环添加数据
create procedure repeat_addClass(in num int)
    begin
    declare x int default 0;
    repeat 
        insert into class(class_name,class_remark) values (concat('c++',x),x);
        set x = x + 1;
    until i >= num     end repeat;
    end
 
# loop循环 向class表中循环添加数据
create procedure loop_addClass(in num int)
    begin
        declare x int default 0;
        myloop:loop
            insert into class(class_name,class_remark) values(concat('html',x),x);
            set x = x + 1;
            if x >= num then
                leave myloop;
            end if;
        end loop;
    end




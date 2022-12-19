# SQL递归查询
* 优点：效率高，大量数据集下，速度比程序的查询快

递归CTE最少包含两个查询(也被称为成员)。第一个查询为定点成员，定点成员只是一个返回有效表的查询，用于递归的基础或定位点。
第二个查询被称为递归成员，使该查询称为递归成员的是对CTE名称的递归引用是触发。在逻辑上可以将CTE名称的内部应用理解为前一个查询的结果集。

递归查询没有显式的递归终止条件，只有当第二个递归查询返回空结果集或是超出了递归次数的最大限制时才停止递归。是指递归次数上限的方法是使用MAXRECURION。

## 常见形式

    WITH CTE AS (
        SELECT cols FROM table WHERE conditions
        UNION ALL
        SELECT cols FROM table
        INNER JOIN CTE ON conditions
    ）


    # e.g.    
    WITH CTE AS (
        SELECT userID, ManagerID, Name, Name AS ManagerName
        FROM dbo.table 
        WHERE ManagerID = -1   # 根节点，递归查询起始点
        UNION ALL  # 迭代公式（把每次查询结果集并在一起）
        SELECT c.userID, c.ManagerID, c.Name, p.Name AS ManagerName  # 查询语句中调用CTE，调用上次查询的结果集
        FROM CTE p
        INNER JOIN dbo.table ON p.UserID=c.ManagerID
    ）
    SELECT userID, ManagerID, Name, ManagerName FROM CTE;



    # 通过层次结构查询子节点到父节点的路径
    WITH CTE AS(
        SELECT userID, ManagerID, Name, CAST(NAME as NVARCHAR(MAX)) as LPath  # 将Name的长度设置为最大防止字段过长
        FROM dbo.table 
        WHERE ManagerID = -1  
        UNION ALL 
        SELECT c.userID, c.ManagerID, c.Name, p.LPath+'->'+c.Name AS LPath
        FROM CTE p
        INNER JOIN dbo.table ON p.UserID=c.ManagerID
    ）
    SELECT userID, ManagerID, Name, ManagerName FROM CTE;
    ## 返回：Boss->employee1->employee6 (层级关系）


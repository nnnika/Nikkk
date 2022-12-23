# 数据埋点

## 类型
1. 全埋点 - 部署对应sdk，页面及控件数据全采集，使用时解析
2. 前端埋点 - 前段定义的事件发生时,上传对应的数据
3. 服务端埋点 - 服务端di定义的时间发生时,上传对应的数据

* 根据埋点技术还可分为Web埋点/JavaScript埋点、App埋点、接口埋点。
## 事件的基本思维（4W1H）
1. Who：对行为的发起者进行标识，一般使用账号及设备号进行标识。账号是常用的方式，通过身份证号、手机号、账号 ID 等信息区分用户；设备号多用于不需要登录的产品，通过设备的编码来区分用户。
2. When：记录行为的发生时间，一般使用服务器时间，即 Unix 时间戳记录行为发生时间；它是全球统一时间，不受地区的干扰。
3. Where：记录行为发生的地点，一般通过 GPS 进行定位，或者通过设备 IP 判断用户位置。
4. What：指用户行为的具体内容是什么，比如用户阅读一本书，那么购买的书名是什么？价格是多少？哪个出版社出版等信息。
5. How：行为是怎么发生的，一般包含在行为名称中，如提交某订单，也有若干行为是可以通过多种方式完成，如解锁 iPhone，可以输入密码解锁，也可以刷脸解锁，无论使用哪种方式都是一种可以记录的信息。

## 事件分类
1. 核心事件。产品的核心流程及用户核心行为的分支事件，根据具体业务需求进行专门处理和参数设置。
2. 通用事件。对于通用的、泛化性的、活动等次要流程事件，可以进行抽象化处理。 比如，在日常工作中，经常遇到市场或活动运营同事提出某次活动的埋点需求，如果每次活动都单独处理成一个事件，随着时间的推移将会导致同类事件越积越多，不利于管理，因此对于这类相关的事件，需要进行抽象化的通用事件处理。
3. 边缘事件。所谓边缘事件，指的是零散的只查看点击或浏览行为的事件，比如 APP 端诸如设置、客服入口等功能按钮。 
   处理此类事件，有两种常见方法： 一种是做一个最基本的自定义事件容器，然后把相关按钮名称、所在页面及其他零散东西抽象化后放进去。 另一种是手动纠正一些全埋点进行上报。之所以要手动纠正，是因为前后端的技术架构不同，没有办法 100% 地适应全埋点，当全埋点数据出现未知或无法采集时，需要手动调 SDK，纠正所要采集的页面。

## 具体行为埋点
Who:用户ID，设备ID
When：浏览时间（时间戳）
How：浏览时长，前向页面
What：浏览事件（点击事件）
Where：功能板块，页面ID
公共指标：平台，端口号，应用版本，操作系统，操作系统版本号，设备制造商，设备型号，屏幕高度，屏幕宽度，网络环境，运营商ID，地址，IP...

## 数据字段
埋点位置：{APP，Web，小程序，功能板块}
事件定义：{事件ID，触发步骤，中文名称}
回传参数定义：{中文名称，英文名称，参数值类型，参数示例说明}
其他：{埋点形式，埋点版本，备注}


UV（Unique visitor） 浏览网页的自然人
IP（Internet Protocol）指访问过某站点的IP总数，以用户的IP地址作为统计依据
PV（Page View）即页面浏览量或点击量
VV（Visit View）统计所有访客1天内访问网站的次数

    @route("/detail")
    def detail(env):
        # 获取前端传递数据
        data = env['requests']['query_str']
        header = env['requests']['header']
        # 创建链接
        conn = connect(host='localhost', port=3306, database='booksite', user='root', password='mysql', charset='utf8')
        # 创建游标
        cursor = conn.cursor()
        # 执行sql语句 按照指定条件查询
        sql = "select *  from bookinfo where %s;"%data
        cursor.execute(sql)
     
        # 获取数据 元组  ((),())
        stock_data = cursor.fetchone()
        data_dict = {
                "id":stock_data[0],
                "name":stock_data[1],
                "auth":stock_data[2],
                "img_url":stock_data[3],
                "read":stock_data[5],
                "comment":stock_data[6],
                "score":stock_data[8],
                "content":stock_data[7],
                "synopsis":stock_data[9]
            }
     
        # 将阅读量更新后写入数据库
        read = stock_data[5] + 1
        sql = 'update bookinfo set bread=%d where id=%d;'%(read,stock_data[0])
        cursor.execute(sql)
        conn.commit()
     
        # 将埋点数据写入日志
        logger.info({
            'bookClick':{ # 事件名称
            "identification":header['User-Agent'].split(' ')[-1], # 获取设备号
            "ip":header['client_addr'], # 用户设备ip
            "equipment":header['User-Agent'],#用户系统信息
            "entrance":header['Referer'], # 用户跳转路径
            "bookname":stock_data[1], # 书名
            "read":read, # 阅读量
        }
        })
     
        json_str = json.dumps(data_dict, ensure_ascii=False)
     
        return json_str


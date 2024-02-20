# 基于深度卷积神经网络的餐饮管理系统

## 功能设计

#### 餐厅消费者

> 1.通过系统的yolov5算法，将选择的菜品放到机器下通过摄像头识别自动算出菜品的价格，价格透明计算无误
>
> 2.用户在机器计算出菜品的价格后，扫机器显示的二维码即可支付菜品的花费，方便快捷



#### 餐厅服务者

>1.当机器计算出餐厅消费者选择的菜品的价格后，会将菜品的价格显示给餐厅服务员确认价格，方便快捷
>
>2.机器打开计算餐厅服务者的当班时间，据服务者当班的时间内交易的次数，工钱奖惩计算准确无误
>
>3.机器统计出菜品中的畅销款，给予餐厅服务者购买畅销的菜品的原材料建议



#### 餐厅老板

>1.系统推出盈利日报，季报，年报，老板可以查看各个餐厅的盈利情况
>2.播报餐厅服务者的当班签到盈利情况，老板可以更清楚的知道每个服务者的动向，给予奖惩



## 数据库设计

### t_menu(菜单表)

>#id，盘子颜色，菜品名称，菜品存量，菜品销量，菜品盈利，is_state，创建时间，创建人id，更新时间，更新人id，租户id
>
>| 表单 | id     | plateColor | dish_name | dish_stock | dish_used | dish_profit | is_state | create_time | create_id | update_time | update_id | tenant_id |
>| ---- | ------ | ---------- | --------- | ---------- | --------- | ----------- | -------- | ----------- | --------- | ----------- | --------- | --------- |
>| 参数 | bigint | Int        | Varchar30 | Int        | Int       | double      | Int      | Date        | Bigint    | Date        | Bigint    | Bigint    |



### t_price(价格表)

>#id，盘子颜色，盘子价格，is_state，创建时间，创建人id，更新时间，更新人id，租户id
>
>| 表单 | id     | plate_color | plate_price | is_state | create_time | create_id | update_time | update_id | tenant_id |
>| ---- | ------ | ----------- | ----------- | -------- | ----------- | --------- | ----------- | --------- | --------- |
>| 参数 | Bigint | Int         | Double      | Int      | Date        | Bigint    | Date        | Bigint    | Bigint    |



### t_attendancesheet(签到表)

>#id，用户id，签到时间，签到类型（0:上班，1:下班）,is_state，创建时间，创建人id，更新时间，更新人id，租户id
>
>| 表单 | id     | user_id | attendance_time | attendance_type | is_state | create_time | create_id | update_time | update_id | tenant_id |
>| ---- | ------ | ------- | --------------- | --------------- | -------- | ----------- | --------- | ----------- | --------- | --------- |
>| 参数 | Bigint | Bigint  | Date            | int             | Int      | Date        | Bigint    | Date        | Bigint    | Bigint    |



### t_salestable(销售表)

>#id，菜品名称，时间，菜品id，菜品盈利，价格id，is_state，创建时间，创建人id，更新时间，更新人id，租户id
>
>| 表单 | id     | dish_name | date_time | dish_id | dish_profit | price_id | is_state | create_time | create_id | update_time | update_id | tenant_id |
>| ---- | ------ | --------- | --------- | ------- | ----------- | -------- | -------- | ----------- | --------- | ----------- | --------- | --------- |
>| 参数 | Bigint | Varchar30 | date      | bigint  | Double      | Bigint   | Int      | Date        | Bigint    | Date        | Bigint    | Bigint    |



### t_payroll(工资表)

>#id，用户id，时间，工资，is_state，创建时间，创建人id，更新时间，更新人id，租户id
>
>| 表单 | id     | user_id | date_time | payroll | is_state | create_time | create_id | update_time | update_id | tenant_id |
>| ---- | ------ | ------- | --------- | ------- | -------- | ----------- | --------- | ----------- | --------- | --------- |
>| 参数 | bigint | Bigint  | date      | double  | Int      | Date        | Bigint    | Date        | Bigint    | Bigint    |



## 深度学习部分

>深度学习部分使用yolov5开源项目，以yolov5项目为基础，添加了flask模块负责与外网通讯。


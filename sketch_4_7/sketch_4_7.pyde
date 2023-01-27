# 催眠的同心圆
'''
4.1绘制圆弧
4.2圆弧的旋转
4.3利用全局变量实现圆弧变长
4.4if语句实现圆弧长度重复变化
4.5逻辑运算符
4.6圆弧同时旋转与长度变化
4.7多层圆弧效果
4.8小结
'''
# 最终代码
def setup():  # 初始化函数，仅运行一次
    global spanAngle,spanAngleSpeed  # 全局变量
    size(600,600)  # 设定画面宽度、高度
    noFill()  # 不填充
    strokeWeight(3)  # 设置线条粗细
    spanAngle = 0  # 圆弧跨越的角度，初始为0
    spanAngleSpeed = 0.5  # 圆弧跨越角度变化速度
    
def draw():  # 绘制函数，每帧重复运行
    global spanAngle,spanAngleSpeed  # 全局变量
    background(255)  # 设置白色背景，并覆盖整个画面
    # 圆弧终点角度，随着帧率循环变大
    endAngle = 2*radians(frameCount % 360)
    spanAngle = spanAngle + radians(spanAngleSpeed)  # 圆弧跨越角度变化
    startAngle = endAngle - spanAngle  # 求出圆弧起点角度
    
    if spanAngle > 2*PI or spanAngle < 0:  # 当跨越角度达到2PI或0时
        spanAngleSpeed = -spanAngleSpeed  # 更改跨越角度变化速度的方向
        
    for diam in range(50,width,50):  # 圆弧直径从50开始遍历到width
        angleShift = radians(360*diam/width)  # 不同直径圆弧有个偏移量
        arc(width/2,height/2,diam,diam,  # 绘制对应的各个圆弧
            startAngle + angleShift,endAngle+angleShift)

'''
if语句（选择判断语句）

if spanAngle > 2*PI:  # 当跨越角度达到2PI或0时
    spanAngleSpeed = -spanAngleSpeed  # 更改跨越角度变化速度的方向

python共有6种运算符判断两个数字的大小关系
-----------------------------------------
|    表达式    |         含义           |
-----------------------------------------
|    x > y     |       x是否大于y       |
-----------------------------------------
|    x < y     |       x是否小于y       |
-----------------------------------------
|    x == y    |       x是否等于y       |
-----------------------------------------
|    x != y    |      x 是否不等于 y    |
-----------------------------------------
|    x >= y    |    x 是否大于或等于y   |
-----------------------------------------
|    x <= y    |    x 是否小于或等于y   |
-----------------------------------------

'''
# if语句格式：
# x = 3
# y = 5
# if x > y:
#     print("x > y")
# if x == y:
#     print("x == y")
# if x < y:
#     print("x < y")

#练习4-3：
number = 11*13*15*17
if number > 30000:
    print('11*13*15*17 > 30000')
if number < 30000:
    print('11*13*15*17 < 30000')
if number == 30000:
    print('11*13*15*17 == 30000')

'''
4.4if 语句实现圆弧长度重复变化
'''
# def setup():  # 初始化函数，仅运行一次
#     global spanAngle,spanAngleSpeed  # 全局变量
#     size(600,600)  # 设定画面宽度、高度
#     noFill()  # 不填充
#     strokeWeight(3)  # 设置线条粗细
#     spanAngle = 0  # 圆弧跨越的角度，初始为0
#     spanAngleSpeed = 0.5  # 圆弧跨越角度变化速度
    
# def draw():  # 绘制函数，每帧重复运行
#     global spanAngle,spanAngleSpeed  # 全局变量
#     background(255)  # 设置白色背景，并覆盖整个画面
#     # 圆弧终点角度，随着帧率循环变大
#     endAngle = 2*radians(frameCount % 360)
#     spanAngle = spanAngle + radians(spanAngleSpeed)  # 圆弧跨越角度变化
#     startAngle = endAngle - spanAngle  # 求出圆弧起点角度
    
#     if spanAngle > 2*PI:  # 当跨越角度达到2PI时
#         spanAngleSpeed =-spanAngleSpeed  # 更改跨越角度变化速度的方向
#     if spanAngle < 0:  # 当跨越角度小于0时
#         spanAngleSpeed =-spanAngleSpeed  # 更改跨越角度变化速度的方向

'''
1.if spanAngle > 2*PI:  # 当跨越角度达到2PI时
    spanAngleSpeed =-spanAngleSpeed  # 更改跨越角度变化速度的方向
    
2.if spanAngle < 0:  # 当跨越角度小于0时
    spanAngleSpeed =-spanAngleSpeed  # 更改跨越角度变化速度的方向
1.当spanAngle大于2*PI时，将圆弧跨越角度变化速度反向，圆弧长度开始变小。2.当spanAngle小于0时，再让变化速度反向，又让圆弧长度开始增加。
'''
'''
逻辑运算符
'''
# print(3 > 2)  # True(真) 
# print(4 > 5)  # False(假)

# print(not(3 > 2))  # False(假)
# print(not(4 > 5))  # True(真)

# print((3 > 2) or(4 > 5))  # True(真)
# print((3 > 2) or(4 > 5))  # False(假)
'''
Python有三个逻辑运算符，方便进行多个判断条件的组合：
not(非)、and(与)、or(或)
'''
'''
练习4-4：利用if语句实现圆半径重复变大，变小的效果。
'''
# def setup():
#     global diameter,diamSpeed
#     size(600,600)
#     fill(200)
#     diameter = 1
#     diamSpeed = 2
    
# def draw():
#     global diameter,diamSpeed
#     background(255)
#     diameter = diameter + diamSpeed
#     if diameter > width or diameter < 1:
#         diamSpeed = -diamSpeed
#     circle(300,300,diameter)
'''
4.6圆弧同时旋转与长度变化
'''
# def setup():  # 初始化函数，仅运行一次
#     global spanAngle,spanAngleSpeed  # 全局变量
#     size(600,600)  # 设定画面宽度、高度
#     noFill()  # 不填充
#     strokeWeight(3)  # 设置线条粗细
#     spanAngle = 0  # 圆弧跨越的角度，初始为0
#     spanAngleSpeed = 0.5  # 圆弧跨越角度变化速度
    
# def draw():  # 绘制函数，每帧重复运行
#     global spanAngle,spanAngleSpeed  # 全局变量
#     background(255)  # 设置白色背景，并覆盖整个画面
#     # 圆弧终点角度，随着帧率循环变大
#     endAngle = 2*radians(frameCount % 360)
#     spanAngle = spanAngle + radians(spanAngleSpeed)  # 圆弧跨越角度变化
#     startAngle = endAngle - spanAngle  # 求出圆弧起点角度
#     if spanAngle > 2*PI or spanAngle < 0:  # 当跨越角度达到2PI或0时
#         spanAngleSpeed = -spanAngleSpeed  # 更改跨越角度变化速度的方向
#         arc(width/2,height/2,300,300,startAngle,endAngle)  # 绘制圆弧

'''
4.7多层圆弧效果
'''
# def setup():  # 初始化函数，仅运行一次
#     global spanAngle,spanAngleSpeed  # 全局变量
#     size(600,600)  # 设定画面宽度、高度
#     noFill()  # 不填充
#     strokeWeight(3)  # 设置线条粗细
#     spanAngle = 0  # 圆弧跨越的角度，初始为0
#     spanAngleSpeed = 0.5  # 圆弧跨越角度变化速度
    
# def draw():  # 绘制函数，每帧重复运行
#     global spanAngle,spanAngleSpeed  # 全局变量
#     background(255)  # 设置白色背景，并覆盖整个画面
#     # 圆弧终点角度，随着帧率循环变大
#     endAngle = 2*radians(frameCount % 360)
#     spanAngle = spanAngle + radians(spanAngleSpeed)  # 圆弧跨越角度变化
#     startAngle = endAngle - spanAngle  # 求出圆弧起点角度
    
#     if spanAngle > 2*PI or spanAngle < 0:  # 当跨越角度达到2PI或0时
#         spanAngleSpeed = -spanAngleSpeed  # 更改跨越角度变化速度的方向
        
#     for diam in range(50,width,50):  # 圆弧直径从50开始遍历到width
#         arc(width/2,height/2,diam,diam,startAngle,endAngle)  # 绘制圆弧
        
'''
for循环中变量diam从50逐渐增加到width，绘制多层圆弧效果。
'''
'''
多层圆弧效果
'''
def setup():  # 初始化函数，仅运行一次
    global spanAngle,spanAngleSpeed  # 全局变量
    size(600,600)  # 设定画面宽度、高度
    noFill()  # 不填充
    strokeWeight(3)  # 设置线条粗细
    spanAngle = 0  # 圆弧跨越的角度，初始为0
    spanAngleSpeed = 0.5  # 圆弧跨越角度变化速度
    
def draw():  # 绘制函数，每帧重复运行
    global spanAngle,spanAngleSpeed  # 全局变量
    background(255)  # 设置白色背景，并覆盖整个画面
    # 圆弧终点角度，随着帧率循环变大
    endAngle = 2*radians(frameCount % 360)
    spanAngle = spanAngle + radians(spanAngleSpeed)  # 圆弧跨越角度变化
    startAngle = endAngle - spanAngle  # 求出圆弧起点角度
    
    if spanAngle > 2*PI or spanAngle < 0:  # 当跨越角度达到2PI或0时
        spanAngleSpeed = -spanAngleSpeed  # 更改跨越角度变化速度的方向
        
    for diam in range(50,width,50):  # 圆弧直径从50开始遍历到width
        angleShift = radians(360*diam/width)  # 不同直径圆弧有个偏移量
        arc(width/2,height/2,diam,diam,  # 绘制对应的各个圆弧
            startAngle + angleShift,endAngle+angleShift)     
'''
4.8本章小结
1.学习了全局变量、if选择判断、比较大小运算符、逻辑运算符等语法知识。
2.学习了圆弧的绘制。
3.学校实现理发店标志转灯等效果。    

'''
第5章 简易毛笔字
·5.1鼠标画圆
·5.2鼠标画线
·5.3改变画线粗细
·5.4粗细平滑过渡
·5.5一条线段上粗细插值
·5.6绘制分叉线
·5.7小结
'''
# 最终代码
# def setup():  # 初始化函数，仅运行一次
#     global maxThickness,offset # 全局变量
#     size(1920,1080)  # 设定画面宽度、高度
#     strokeWeight(10) # 设置线条粗细
#     background(255)  # 设置白色背景
#     maxThickness = 25 # 最粗笔触
#     offset = 2 # 用于画偏移分叉线
    
# def draw():  # 绘制函数，每帧重复运行
#     return # 函数直接返回

# def mousePressed(): # 当鼠标按键时
#     global lastX,lastY,vx,vy,lastThickness # 全局变量
#     lastX = mouseX  # 当鼠标按下时，表示这一笔的起点坐标
#     lastY = mouseY
#     vx = 0 # 移动的速度初始化为0
#     vy = 0
#     lastThickness = 1 # 鼠标刚按下时，笔触粗细为1
    
# def mouseDragged(): # 当鼠标按键后拖动时
#     global lastX,lastY,vx,vy,lastThickness # 全局变量
#     vx = 0.7*vx + 0.3*(mouseX-lastX) # 获得当前移动速度，保持连续插值
#     vy = 0.7*vy + 0.3*(mouseY-lastY)
#     v = sqrt(vx*vx+vy*vy) # 当前移动速度的模
    
#     # 速度越快，笔触越细
#     nextThickness = maxThickness - v
#     if nextThickness < 0:  # 防止粗细小于0
#         nextThickness = 0 
#     # 笔触的粗细也需要连续，防止变化太剧烈
#     nextThickness = 0.5*nextThickness + 0.5*lastThickness
    
#     n = 10 + int(v/2) # 速度越快，分段数越高
#     for i in range(1,n+1): # 将鼠标前后两个点间分成n段绘制
#         x1 = map(i-1,0,n,lastX,mouseX) # 对应的前后两个顶点坐标
#         y1 = map(i-1,0,n,lastY,mouseY)
#         x2 = map(i,0,n,lastX,mouseX)
#         y2 = map(i,0,n,lastY,mouseY)
#         # 对应的这一小段的粗细
#         thickness = map(i-1,0,n,lastThickness,nextThickness)
#         strokeWeight(thickness+offset) # 主线粗细加一个偏移量
#         line(x1,y1,x2,y2)  # 画主线
#         strokeWeight(thickness) # 以下画出偏移，模拟毛笔分叉绘制的效果
#         line(x1+offset*2,y1+offset*2,x2+offset*2,y2+offset*2)
#         line(x1-offset,y1-offset,x2-offset,y2-offset)
        
#     lastX = mouseX # 更新前一个点的坐标
#     lastY = mouseY
#     lastThickness = nextThickness # 更新前一个笔触的粗细
    
# def keyPressed(): # 当按下任意键盘按键时
#     background(255) # 重新用白色填充屏幕

'''
5.1鼠标画圆
'''
# def setup():  # 初始化函数，仅运行一次
#     size(800,600)  # 设定画面宽度、高度
#     noStroke()  # 不绘制线条
#     fill(0)  # 填充黑色
#     background(255)  # 设置白色背景
    
# def draw():  # 绘制函数，每帧重复运行
#     circle(mouseX,mouseY,10)  # 在鼠标位置处画一个圆

# def setup():  # 初始化函数，仅运行一次
#     size(800,600)  # 设定画面宽度、高度
#     noStroke()  # 不绘制线条
#     fill(0)  # 填充黑色
#     background(255)  # 设置白色背景
    
# def draw():  # 绘制函数，每帧重复运行  
#     return  # 函数直接返回

# def mouseDragged():  #当鼠标按键时
#     circle(mouseX,mouseY,10)  # 在鼠标位置处画一个圆
    
# def mouseDragged():  # 当鼠标按键后拖动时
#     circle(mouseX,mouseY,10)  # 在鼠标位置处画一个圆
'''
mousePressed()当按下鼠标按键时执行，mouseDragged()当鼠标按键且移动时执行鼠标按键后才画圆更逼近实际落笔写字的过程。
缺：不连续的笔画。
'''
'''
5.2鼠标画线
line(x1,y1,x2,y2),在顶点(x1,y1)、(x2,y2)之间绘制一条线段
记录鼠标上一帧的位置(lastX,lastY)，与鼠标当前位置(mouseX,mouseY)绘制连线
'''    
# def setup():  # 初始化函数，仅运行一次
#     size(800,600)  # 设定画面宽度、高度
#     strokeWeight(10)  # 设置线条粗细
#     background(255)  # 设置白色背景
    
# def draw():  # 绘制函数，每帧重复运行
#     return  # 函数直接返回

# def mousePressed():  # 当鼠标按键时
#     global lastX,lastY  # 全局变量
#     lastX = mouseX  # 当鼠标按下时，表示这一笔的起点坐标
#     lastY = mouseY
    
# def mouseDragged():  # 当鼠标按键后拖动时
#     global lastX,lastY  # 全局变量
#     line(lastX,lastY,mouseX,mouseY)  # 画线
#     lastX = mouseX  # 更新前一个点的坐标
#     lastY = mouseY
'''
改变画线粗细
模拟真实毛笔效果：鼠标移动速度越快，线条越细；移动速度越慢，线条越粗
mousePressed()中，设定x，y方向速度vx=0，vy=0，笔触粗细thickness初始化为1
mouseDragged()函数，利用鼠标当前位置和之前位置，计算鼠标移动速度vx,vy
             vx = mouseX-lastX
             vy = mouseY-lastY
计算当前移动速度的大小（模）v，sqrt()为求平方根函数
             v = sqrt(vx*vx+vy*vy)
设定当前画笔粗细，v越大thickness越小
             thickness = maxThickness - v
             strokeWeight(thickness)  #设置线粗细
'''
'''
5.3改变画线粗细
'''
# def setup():  # 初始化函数，仅运行一次
#     global maxThickness,offset # 全局变量
#     size(800,600)  # 设定画面宽度、高度
#     strokeWeight(10) # 设置线条粗细
#     background(255)  # 设置白色背景
#     maxThickness = 25 # 最粗笔触
    
# def draw():  # 绘制函数，每帧重复运行
#     return # 函数直接返回

# def mousePressed(): # 当鼠标按键时
#     global lastX,lastY,vx,vy,thickness # 全局变量
#     lastX = mouseX  # 当鼠标按下时，表示这一笔的起点坐标
#     lastY = mouseY
#     vx = 0 # 移动的速度初始化为0
#     vy = 0
#     thickness = 1 #当鼠标刚按下时，笔触粗细为1
    
# def mouseDragged(): # 当鼠标按键后拖动时
#     global lastX,lastY,vx,vy,thickness # 全局变量
#     vx = mouseX-lastX # 获得当前移动速度，保持连续插值
#     vy = mouseY-lastY
#     v = sqrt(vx*vx+vy*vy) # 当前移动速度的模
    
#     # 速度越快，笔触越细
#     thickness = maxThickness - v
#     if thickness < 0:  # 防止粗细小于0
#         thickness = 0 
#     strokeWeight(thickness)  # 设置线宽度
        
#     line(lastX,lastY,mouseX,mouseY)  # 画线
#     lastX = mouseX # 更新前一个点的坐标
#     lastY = mouseY
    
# def keyPressed(): # 当按下任意键盘按键时
#     background(255) # 重新用白色填充屏幕
'''
5.4粗细平滑过渡
当鼠标移动速度变化较大时，笔触粗细变化过于剧烈
新的鼠标速度vx由旧的速度vx、当前新速度(mouseX-lastX)加权平均获得
'''
# vx = 0.7*vx + 0.3*(mouseX-lastX)  # 获得当前移动速度，保持连续插值
# vy = 0.7*vy + 0.3*(mouseY-lastY)

'''
lastThickness记录之前笔触粗细，nextThickness记录之后笔触粗细，应用加权平均的方法防止笔触粗细变化过于剧烈：
'''
# # 笔触的粗细也需要连续，防止变化太剧烈
# nextThickness = 0.5*nextThickness + 0.5*lastThickness
# strokeWeight(lastThickness)  # 设置线粗细

'''
5.4粗细平滑过渡
'''
# def setup():  # 初始化函数，仅运行一次
#     global maxThickness,offset # 全局变量
#     size(1920,1080)  # 设定画面宽度、高度
#     strokeWeight(10) # 设置线条粗细
#     background(255)  # 设置白色背景
#     maxThickness = 25 # 最粗笔触
    
# def draw():  # 绘制函数，每帧重复运行
#     return # 函数直接返回

# def mousePressed(): # 当鼠标按键时
#     global lastX,lastY,vx,vy,lastThickness # 全局变量
#     lastX = mouseX  # 当鼠标按下时，表示这一笔的起点坐标
#     lastY = mouseY
#     vx = 0 # 移动的速度初始化为0
#     vy = 0
#     lastThickness = 1 # 鼠标刚按下时，笔触粗细为1
    
# def mouseDragged(): # 当鼠标按键后拖动时
#     global lastX,lastY,vx,vy,lastThickness # 全局变量
#     vx = 0.7*vx + 0.3*(mouseX-lastX) # 获得当前移动速度，保持连续插值
#     vy = 0.7*vy + 0.3*(mouseY-lastY)
#     v = sqrt(vx*vx+vy*vy) # 当前移动速度的模
    
#     # 速度越快，笔触越细
#     nextThickness = maxThickness - v
#     if nextThickness < 0:  # 防止粗细小于0
#         nextThickness = 0 
#     # 笔触的粗细也需要连续，防止变化太剧烈
#     nextThickness = 0.5*nextThickness + 0.5*lastThickness
#     strokeWeight(lastThickness)  # 设置线粗细
    
#     line(lastX,lastY,mouseX,mouseY)  # 画线
#     lastX = mouseX  # 更新前一个点的坐标
#     lastY = mouseY
#     lastThickness = nextThickness # 更新前一个笔触的粗细

'''
一条线段上粗细插值
当鼠标移动速度过快时，仍会出现笔触粗细变化不连续的情况
将line(lastX,lastY,mouseX,mouseY)分成n段分别绘制
鼠标移动速度越快，n越大int()把小数转换为整数。
'''
#     n = 10 + int(v/2) # 速度越快，分段数越高
#     for i in range(1,n+1): # 将鼠标前后两个点间分成n段绘制
#         x1 = map(i-1,0,n,lastX,mouseX) # 对应的前后两个顶点坐标
#         y1 = map(i-1,0,n,lastY,mouseY)
#         x2 = map(i,0,n,lastX,mouseX)
#         y2 = map(i,0,n,lastY,mouseY)
#         # 对应的这一小段的粗细
#         thickness = map(i-1,0,n,lastThickness,nextThickness)
#         strokeWeight(thickness+offset) # 主线粗细加一个偏移量
#         line(x1,y1,x2,y2)  # 画线

'''
                             ---------------------
                             |   类型转换函数    |
———————————|———|————————— |————————————————
|         格式        |                功能                 |     结果输出       |
----------------------|-------------------------------------|----------------------
|    print(int(3.5))  |# 把浮点数转换为整数                 |         3          |
----------------------|-------------------------------------|----------------------
|    print(int("31")) |# 把字符串转换为整数                 |         31         |
----------------------|-------------------------------------|----------------------
|     print(float(3)) |# 把整数转换为浮点数                 |        3.0         |
----------------------|-------------------------------------|----------------------
| print(float("3.14"))|# 把字符串转换为浮点数               |        3.14        | 
----------------------|-------------------------------------|----------------------
|    print(str(12345))|# 把整数转换为字符串                 |        12345       |
----------------------|-------------------------------------|----------------------
|   print(str(5.4321))|# 把浮点数转换为字符串               |       5.4321       |
—————————————————————————————————————————
'''
'''
5.6绘制分叉线
定义偏移量offset = 2，以thickness+offset的粗细绘制主要的笔触线条line(x1,y1,x2,y2)
设定笔触粗细为thickness，在主线条的右下方绘制线条line(x1+offset*2,y1+offset*2,y2+offset*2),在主线条的左上方绘制线条line(x1-offset,y1-offset,x2-offset,y2-offset)
'''
#         strokeWeight(thickness+offset) # 主线粗细加一个偏移量
#         line(x1,y1,x2,y2)  # 画主线
#         strokeWeight(thickness) # 以下画出偏移，模拟毛笔分叉绘制的效果
#         line(x1+offset*2,y1+offset*2,x2+offset*2,y2+offset*2)
#         line(x1-offset,y1-offset,x2-offset,y2-offset)

'''
5.7小结
·学习了类型转换等语法知识
·学习了直线的绘制、鼠标键盘的互动
·尝试实现水彩笔、蜡笔、粉笔等等其他画笔的绘制效果
'''

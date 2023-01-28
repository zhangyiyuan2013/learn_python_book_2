# 第7章 随机扭动的曲线
'''
·7.1圆圈上的点
·7.2random随机函数
·7.3noise随机函数
·7.4连续变化的随机点
·7.5将点连接成曲线
·7.6处理首尾不连接的问题
·7.7彩色曲线效果
·7.8清屏与保存图片
·7.9小结
'''
# 最终代码
# def setup():
#     size(800, 800)   # 设定画布大小
#     noFill()   # 不要填充颜色
#     background(255)   # 纯白背景
#     frameRate(30)   # 设置帧数
    
# def draw():
#     if frameCount%800 ==0:    # 每过若干帧
#         saveFrame("RandomLines-######.png")   # 保存一张图片
#         background(255)   # 用白色重新填充背景
        
#     translate(width/2,height/2)   # 移动坐标系原点到画面中心
#     r = map(sin(frameCount/200.0),-1,1,100,255)   # 随机红色分量
#     g = map(sin(frameCount/300.0),-1,1,0,255)     # 随机绿色分量
#     b = map(sin(frameCount/400.0),-1,1,100,255)   #随机蓝色分量
#     stroke(r,g,b,15)  # 设置线条颜色、透明度
#     beginShape()   # 开始绘制曲线
#     for angle in range(0,360,2):   # 对一圈角度遍历
#         radAngle = radians(angle)   # 转换为弧度值
#         # 利用三角函数生成周期性的数据，避免曲线首尾不连续的问题
#         noiseID = sin(radAngle)-cos(radAngle) \
#                   + 2*sin(radAngle)*sin(radAngle)
#         # 利用二维噪音声函数生成随机半径
#         radius = map(noise(noiseID*0.3,frameCount*0.01) \
#                      ,0,1,200,400)
#         x = radius*cos(radAngle)  # 这一角度对应的x坐标
#         y = radius*sin(radAngle)  # 这一角度对应的y坐标
#         curveVertex(x,y)  # 添加对应的顶点
#     endShape(CLOSE)   # 结束封闭曲线的绘制
    
# def mousePressed():  # 当鼠标按键时
#     saveFrame("RandomLines-######.png")  # 保存一张图片
#     background(255)   # 用白色重新填充背景

'''
·7.1圆圈上的点
translate(width/2,height/2)将坐标系原点
移动到画面中心

角度angle从0到360度遍历，radAngle为对
应弧度值，radius为大圆圈半径，
(radius*cos(radAngle),radius*sin(radAngle))
为对应角度在圆周上的点
'''
# def setup():
# size(500, 500)  # 设定画布大小
# noFill()  # 不要填充颜色
# strokeWeight(2)  # 制定边框线条粗细为2
# stroke(0)  # 设定线条颜色为淡灰色，0为纯黑、255为纯白

# ** def draw():
#     background(255)  # 纯白背景
#     radius = 200  # 大圆圈的半径
# translate(width/2,height/2)  # 移动坐标系原点到画面中心
# for angle in range(0, 360 ,10):  # 对一圈角度遍历
#     radAngle = radians(angle)  #转换为弧度值
#     x = radius*cos(radAngle)  # 这一角度对应的x坐标
#     y = radius*sin(radAngle)   # 这一角度对应的y坐标
#     circle(x,y,3) **  # 对应位置绘制一个圆圈

'''
·7.2random随机函数
random(5)生成[0, 5]间的随机小数，每次输出结果可能不同
可以设定最大、最小范围，random(-5, 10)生成[-5,10)之间的随机小数
利用类型转换函数，可以生成[10,20)之间的随机整数
1:                   2:
'''
# for i in range(10):     for i in range(5):
#     r = random(5)           r = int(random(10,20))
#     print(r)                print(r)
'''
1的结果输出：        2的结果输出：
2.5930621624         14
0.771473348141       11
3.37304258347        13
1.82577157021        19
0.37273263976414     10
2.37273263931
3.27095413208
0.48580467701
'''
'''
·7.2随机变化的圆圈
'''
# def setup():
# size(500, 500)  # 设定画布大小
# noFill()  # 不要填充颜色
# strokeWeight(2)  # 制定边框线条粗细为2
# stroke(0)  # 设定线条颜色为淡灰色，0为纯黑、255为纯白

# ** def draw():
#     background(255)  # 纯白背景
#     radius = 200  # 大圆圈的半径
# translate(width/2,height/2)  # 移动坐标系原点到画面中心
# for angle in range(0, 360 ,10):  # 对一圈角度遍历
#     radAngle = radians(angle)  #转换为弧度值
#     x = radius*cos(radAngle) + random(-10,10)  # 这一角度对应的x坐标
#     y = radius*sin(radAngle) + random(-10,10)   # 这一角度对应的y坐标
#     circle(x,y,3) **  # 对应位置绘制一个圆圈

'''
·7.3noise随机函数
random()随机绘制的图形，前后帧没有连续性，是不连续随机
为了模拟自然界中云朵、火焰、风、水流等有一定连续性的随机效
果，利用基于柏林噪音(Perlin noise)的noise()函数
1:                       2:
'''
# for i in range(5):        for i in range(5):
#     r = noise(i)              r = noise(0)
#     print(r)                  print(r)
'''
1输出的结果：            2输出的结果：
0.218373671174           0.188436686993
0.539799153805           0.188436686993
0.510047018528           0.188436686993
0.274670958519           0.188436686993
0.64270234108            0.188436686993
1：noice()生成[0,1]之间的随机数
2：noice(0)生成同样的值
'''
'''
·7.3noise随机函数
鼠标左右移动，控制noise()参数取值的间隔
for循环中，x1从0、1、2一直增加width-1，x2=x1+1。
y1 = noise(x1*magn)*height、y2 = noise(x2*magn)*height,并画出连接(x1,y1)、(x2,y2)的直线。

map()函数将鼠标水平位置从[0,width]映射到[0,1]，并赋
值给magn变量。

y1和y2对应noise()函数的参数正好相差magn。magn值越
小，绘制出的曲线越连续；magn值越大，绘制出的曲线越不连续。
'''
# def setup():
#     size(600,300)
    
# def draw():
#     background(255)
#     magn = map(mouseX,0,width,0,1)
#     for x1 in range(width):
#         y1 = noise(x1*magn)*height
#         x2 = x1+1
#         y2 = noise(x2*magn)*height
#         line(x1,y1,x2,y2)

'''
·7.4半径连续随机变化
将noise(frameCount*0.01)应用于圆圈半径，即可以实现随着帧数增加，半径连续随机变化的效果
'''
# def setup():
# size(500, 500)  # 设定画布大小
# noFill()  # 不要填充颜色
# strokeWeight(2)  # 制定边框线条粗细为2
# stroke(0)  # 设定线条颜色为淡灰色，0为纯黑、255为纯白

# ** def draw():
#     background(255)  # 纯白背景
#     radius = 200  # 大圆圈的半径
# translate(width/2,height/2)  # 移动坐标系原点到画面中心
# for angle in range(0, 360 ,10):  # 对一圈角度遍历
#     radAngle = radians(angle)  #转换为弧度值
#     radius = map(noise(frameCount*0.01.),0,1,100,300)   # 随机半径
#     x = radius*cos(radAngle)  # 这一角度对应的x坐标
#     y = radius*sin(radAngle)   # 这一角度对应的y坐标
#     circle(x,y,3) **  # 对应位置绘制一个圆圈

'''
·7.4连续变化的随机点noise(radAngle*0.1,frameCount*0.01)
同时受角度radAngle、帧数frameCount影响

在产生随机的同时保证相近角度、
相邻帧的半径较接近，实现了空间、时间一定连续性的随机

代码过长时，可分成多行，加一个反斜杠符号“\”,系统自动把多行代码连起来运行
'''
# def setup():
# size(500, 500)  # 设定画布大小
# noFill()  # 不要填充颜色
# strokeWeight(2)  # 制定边框线条粗细为2
# stroke(0)  # 设定线条颜色为淡灰色，0为纯黑、255为纯白

# ** def draw():
#     background(255)  # 纯白背景
#     radius = 200  # 大圆圈的半径
# translate(width/2,height/2)  # 移动坐标系原点到画面中心
# for angle in range(0, 360 ,10):  # 对一圈角度遍历
#     radAngle = radians(angle)  #转换为弧度值
      # 利用二维噪音声函数生成随机半径
#     radius = map(noise(noiseID*0.3,frameCount*0.01) \
#                      ,0,1,200,400)
#     x = radius*cos(radAngle)  # 这一角度对应的x坐标
#     y = radius*sin(radAngle)   # 这一角度对应的y坐标
#     circle(x,y,3) **  # 对应位置绘制一个圆圈

'''
·7.5将点连接成曲线
将圆圈上的采样点连接成曲线：beginShape()表示开始绘制曲线，for循环中通过
curveVertex(x,y)添加多个顶点，endShape(CLOSE)表示结束封闭曲线的绘制
'''
# beginShape()  # 开始绘制曲线  **其他代码同sketch_7_4_2.pyde
# for angle in range(0, 360 ,10):  # 对一圈角度遍历
#     radAngle = radians(angle)  #转换为弧度值
      # 利用二维噪音声函数生成随机半径
#     radius = map(noise(noiseID*0.3,frameCount*0.01) \
#                      ,0,1,200,400)
#     x = radius*cos(radAngle)  # 这一角度对应的x坐标
#     y = radius*sin(radAngle)   # 这一角度对应的y坐标
#     curveVertex(x,y)  # 添加对应顶点   **其他代码同sketch_7_4_2.pyde
# endShape(CLOSE)  # 结束封闭曲线的绘制  **其他代码同sketch_7_4_2.pyde

'''
·7.5半透明累加绘制效果
stroke(gray,alpha)设定线条的亮度与透
明度。gray=0表示黑色，gray=255表示
白色；alpha=0表示完全透明，
alpha=255表示完全不透明

stroke(0,15)设定为黑色半透明线条

将background(255)移到setup()中，可
以实现多根线条的累加绘制效果

0度和350度差别大，noise()的值区别
大，对应的radius差异大，曲线出现首
尾不连续现象
'''
# def setup():
#     size(800, 800)   # 设定画布大小
#     noFill()   # 不要填充颜色
#     stroke(0,15)  # 设定线条颜色为黑色，半透明
#     background(255)   # 纯白背景
#     frameRate(30)   # 设置帧数
    
# def draw():
#     translate(width/2,height/2)   # 移动坐标系原点到画面中心
#     beginShape()   # 开始绘制曲线
#     for angle in range(0,360,2):   # 对一圈角度遍历
#         radAngle = radians(angle)   # 转换为弧度值
#         # 利用二维噪音声函数生成随机半径
#         radius = map(noise(noiseID*0.3,frameCount*0.01) \
#                      ,0,1,200,400)
#         x = radius*cos(radAngle)  # 这一角度对应的x坐标
#         y = radius*sin(radAngle)  # 这一角度对应的y坐标
#         curveVertex(x,y)  # 添加对应的顶点
#     endShape(CLOSE)   # 结束封闭曲线的绘制

'''
·7.6处理首尾不连续问题
利用正弦、余弦等三角函数的周期性

sin(0)=sin(2*PI)、cos(0)=cos(2*PI)，因
此由sin()、cos()组合而成的函数会避
免首尾不连续的问题
'''
# def setup():
#     size(800, 800)   # 设定画布大小
#     noFill()   # 不要填充颜色
#     stroke(0,15)  # 设定线条颜色为黑色，半透明
#     background(255)   # 纯白背景
#     frameRate(30)   # 设置帧数
    
# def draw():
#     translate(width/2,height/2)   # 移动坐标系原点到画面中心
#     beginShape()   # 开始绘制曲线
#     for angle in range(0,360,2):   # 对一圈角度遍历
#         radAngle = radians(angle)   # 转换为弧度值
#         # 利用三角函数生成周期性的数据，避免曲线首尾不连续的问题  # **其他代码同sketch_7_5_2.pyde
#         noiseID = sin(radAngle)-cos(radAngle) \
#                   + 2*sin(radAngle)*sin(radAngle)
#         # 利用二维噪音声函数生成随机半径
#         radius = map(noise(noiseID*0.3,frameCount*0.01) \     # **其他代码同sketch_7_5_2.pyde
#                      ,0,1,200,400)
#         x = radius*cos(radAngle)  # 这一角度对应的x坐标
#         y = radius*sin(radAngle)  # 这一角度对应的y坐标
#         curveVertex(x,y)  # 添加对应的顶点
#     endShape(CLOSE)   # 结束封闭曲线的绘制

'''
·7.7三原色原理
三原色原理：任何色彩可由红(Red)、
绿(Green)、蓝(Blue)三种基本颜色
混合而成,如下：
'''
# size(400,300)
# background(255,0,0)
'''                                                 ·7.7三原色原理
 _________________________________________________·-------------------
|对于(r,g,b)中的任意颜色分量，规定0为最暗，255最亮|  
+=================================================+
|background(0,0,0)             # 黑色背景         |
+-------------------------------------------------+
|background(255,255,255)       # 白色背景         |
+-------------------------------------------------+
|background(150,150,150)       # 灰色背景         |
+-------------------------------------------------+ 
|background(255,0,0)           # 红色背景         |
+-------------------------------------------------+
|background(120,0,0)           # 暗红色背景       |
+-------------------------------------------------+
|background(0,255,0)           # 绿色背景         |
+-------------------------------------------------+
|background(0,0,255)           # 蓝色背景         |
+-------------------------------------------------+
|background(255,255,0)         # 黄色背景         |
+-------------------------------------------------+
'''
'''
·7.7彩色绘制效果
background(r,g,b)设置背景颜色，fill(r,g,b)设置填充颜色、stroke(r,g,b)设置线条颜色
'''
# size(500,500)
# background(255)
# noStroke()
# for diameter in range(width,0,-1):
#     r = map(diameter,0,width,255,0)
#     fill(r,0,0)
#     circle(width/2,height/2,diameter)
    
'''
·7.7彩色绘制效果
'''
# size(500,500)
# background(255)
# noStroke()
# for diameter in range(width,0,-1):
#     r = random(0,255)
#     g = random(0,255)
#     b = random(0,255)
#     fill(r,g,b)
#     circle(width/2,height/2,diameter)

'''
·7.7彩色曲线效果
stroke(r,g,b,alpha)设定绘制线条的颜色和透明度
利用正弦函数的周期性，可以实现颜色随着帧数增加的周期性变化
添加了：
'''
#     translate(width/2,height/2)   # 移动坐标系原点到画面中心
#     r = map(sin(frameCount/200.0),-1,1,100,255)   # 随机红色分量
#     g = map(sin(frameCount/300.0),-1,1,0,255)     # 随机绿色分量
#     b = map(sin(frameCount/400.0),-1,1,100,255)   #随机蓝色分量
#     stroke(r,g,b,15)  # 设置线条颜色、透明度

'''
·7.8清屏与保存图片
1.每过800帧，自动保存图片、清空画面
2.当键盘按键时，用白色背景清空画布
'''
# def draw():
#     if frameCount%800 == 0:   # 每过若干帧
#         saveFrame("RandomLines-#####.png")   # 保存一张图片
#         background(255)   # 用白色重新填充背景

# def mousePressed():  # 当鼠标按键时
#     saveFrame("RandomLines-######.png")  # 保存一张图片
#     background(255)   # 用白色重新填充背景

'''
saveFrame("RandomLines-######.png")保存当前画面，如果是第1234帧时保
存，保存图片文件名为：RandomLines-001234.png
'''
'''
·7.9小结
·学习了随机函数、RGB颜色模型
·学习了曲线的绘制
·应用随机和颜色，尝试绘制其他绚丽
  多彩的图形
'''

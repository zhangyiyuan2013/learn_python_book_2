'''
旋转的方块
·6.1绘制方块
·6.2方块旋转
·6.3方块缩放
·6.4绘制一行方块
·6.5绘制方块阵列
·6.6方块阵列旋转缩放
·6.7文字表情包
·6.8小结
'''
# 最终代码
# def setup(): 
#     size(500, 500) # 设定画布大小
#     fill(50)   # 设置填充颜色
#     myFont=createFont("simsun.ttc",10) # 导入字体文件，字体大小为10
#     textFont(myFont) # 设置文字字体
    
# def draw():
#     background(255)   # 纯白背景
#     for x in range(100,401,30):   # 对x遍历
#         for y in range(100,401,30):   # 对y遍历
#             pushMatrix()   # 保存之前的坐标系
#             translate(x,y)   # 将坐标系原点移动到画面中心位置
#             rotate(radians(frameCount)) # 绕着坐标系原点旋转
#             # 当前缩放比例
#             currentScale = map(sin((frameCount+(x-y))/30.0),-1,1,0,4)
#             scale(currentScale)   # 自动缩放
#             textAlign(CENTER) # 坐标设为字符串中心 
#             text(u"元",0,0) # 在坐标系原点显示文字
#             popMatrix()   # 恢复到之前保存的坐标系
'''
square(x,y,w)在(x,y)处绘制边长为w的正方形。
square(x，y，w)默认设置矩形左上角的坐标为(x,y)。
'''
'''
·6.1绘制方块
'''
# def setup():
#     size(500,500)  # 设定画布大小
#     noFill()  # 不要填充颜色
#     strokeWeight(2)  # 制定边框线条粗细为2像素
#     stroke(50)  # 设定线条颜色为淡灰色，0为纯黑、255为纯白
# def draw():
#     background(255)  # 纯白背景
#     square(width/2,height/2,100)  # 在画面正中心画一个矩形

'''
·6.1居中模式
'''
# def setup():
#     size(500,500)  # 设定画布大小
#     noFill()  # 不要填充颜色
#     strokeWeight(2)  # 制定边框线条粗细为2像素
#     stroke(50)  # 设定线条颜色为淡灰色，0为纯黑、255为纯白
# def draw():
#     background(255)  # 纯白背景
#     rectMode(CENTER)  # 在矩形模式中心定位
#     square(width/2,height/2,100)  # 在画面正中心画一个矩形
    
'''
square(x,y,w)在(x,y)处绘制边长为w的正方形
rectMode(CENTER)将矩形中心坐标设为(x,y)
'''
'''
·6.1平移坐标系
'''
# def setup():
#     size(500,500)   # 设定画布大小
#     noFill()   # 不要填充颜色
#     strokeWeight(2)   # 制定边框线条粗细为2像素
#     stroke(50)   # 设定线条颜色为淡灰色，0为纯黑、255为纯白
    
# def draw():
#     background(255)   # 纯白背景
#     rectMode(CENTER)   # 矩形模式中心定位
#     translate(width/2,height/2)  # 将坐标系原点移动到画面中心坐标位置
#     square(0,0,100)   # 在局部坐标系原点画一个矩形
'''
square(x,y,w)在(x,y)处绘制边长为w的正方形。
translate(x,y)，把坐标系的原点在水平方向移动x、在垂直方向移动y。
'''

# square(width/2,height/2,100)   

# rectMode(CENTER)   # 矩形模式中心定位
# translate(width/2,height/2)  # 将坐标系原点移动到画面中心坐标位置
# square(0,0,100)   # 在局部坐标系原点画一个矩形
# 正中心 = (width/2,height/2)
'''
·6.2方块旋转
'''
'''
rotate(angle)让绘制的图形绕坐标系原点旋转angle角度
'''
# rectMode(CENTER)   # 矩形模式中心定位
# translate(width/2,height/2)  # 将坐标系原点移动到画面中心坐标位置
# rotate(radians(30))  # 绕着坐标系原点旋转30度    ***其他代码同·6.1.3
# square(0,0,100)   # 在局部坐标系原点画一个矩形
'''
radians(30)为30度对应的弧度值，角度为正时顺时针方向旋转
利用frameCount让小方块持续旋转
'''
# rotate(radians(30))  # 绕着坐标系原点旋转30度    ***代码同·6.2.1
'''
·6.3方块缩放
scale(s)可以绘制的图形缩放5倍
scale(2)变为原来大小的2倍，scale(0.1)变为原来大小的10%
'''
# scale(0.01*frameCount)  # 自动放大
'''
·6.3方块重复缩放
正弦函数sin(x)值在[-1,1]之间周期性变化。
map(sin(frameCount/30.0),-1,1,0.5,2)产生重复变化的[0.5,2]之间的缩放比例。
scale(currentScale)实现方块的循环放大、缩小。
'''
# # 当前缩放比例：利用正弦函数产生重复变化的数值
# currentScale = map(sin(frameCount/30.0),-1,1,0.5,2)
# scale(currentScale)   # 自动缩放

'''
·6.4绘制一行方块
通过设定方块的x坐标，利用for语句绘制一行代码
'''
# def setup():
#     size(500,500)   # 设定画布大小
#     noFill()    # 不要填充颜色
#     strokeWeight(2)   # 制定边框线条粗细为2像素
#     stroke(50)   # 设定线条颜色为淡灰色，0为纯黑、255为纯白
    
# def draw():
#     background(255)   # 纯白背景
#     for x in range(100,401,30):    # 对x遍历
#         rectMode(CENTER)    # 矩形模式中心定位
#         square(x,height/2,10)   # 画一个矩形

'''
·6.4绘制一行方块
通过平移坐标系，利用for语句绘制一行方块
'''
# def setup():
#     size(500,500)  # 设定画布大小
#     noFill()   # 不要填充颜色
#     strokeWeight(2)   # 制定边框线条粗细为2像素
#     stroke(50)   # 设定线条颜色为淡灰色，0为纯黑、255为纯白
    
# def draw():
#     background(255)   # 纯白背景
#     for x in range(100,401,30):   # 对x遍历
#         rectMode(CENTER)   # 矩形模式中心定位
#         translate(x,height/2)   # 将坐标系原点移动到画面中心位置
#         square(0,0,10)   # 在坐标系原点画一个矩形

'''
·6.4绘制一行方块
for循环语句执行前，坐标系原点为(0,0)
首先x=100，执行translate(x,height/2)，坐标系原点变成(100,height/2),调用
square(0,0,10)绘制一个方块。
x=130，执行translate(x，height/2)，坐标系原点继续平移，变成(230,height)，调用
squarel(0,0,10)绘制一个方块。
x=160，执行translate(x,height/2)，坐标系原点继续平移，变成(390,1.5*height),
超出窗口范围，之后绘制的方块不可见
'''
# for x in range(100,401,30):   # 对x遍历
#     rectMode(CENTER)   # 矩形模式中心定位
#     translate(x,height/2)   # 将坐标系原点移动到画面中心位置
#     square(0,0,10)   # 在坐标系原点画一个矩形
'''
·6.4绘制一行方块
x=100，pushMatrix()保存之前坐标系，即坐标系原点为(0,0)的坐标系执行translate(x，height/2)，坐标系原点变成(100,height/2)，绘制一个方块
popMatrix()恢复到之前保存的坐标系，即坐标系原点为(0,0)的坐标系，x=130，pushMatrix()保存之前坐标系，即坐标系原点为(0,0)的坐标系执行
translate(x，height/2)，坐标系原点变成(130,height/2)，绘制一个方块popMatrix()恢复到之前保存的坐标系，即坐标系原点为(0,0)的坐标系。
'''
# for x in range(100,401,30):   # 对x遍历
#     rectMode(CENTER)   # 矩形模式中心定位
#     pushMatrix()    # 保存之前的坐标系     ***其他代码同·6.4.2
#     translate(x,height/2)   # 将坐标系原点移动到画面中心位置
#     square(0,0,10)   # 在坐标系原点画一个矩形
#     popMatrix()   # 恢复到之前保存的坐标系
'''
·6.5循环嵌套
i取值范围0、1、2。print(i，j)在一行同时输出i、j的值
对外层循环，i初始0，内层循环j取值从0到2，首先输出三行
内层循环j遍历结束，回到外层i循环。i取值1，j从0到3，继续输出三行
内层循环j遍历结束，回到外层i循环，i也遍历结束，整个循环结束。
     代码如下：              输出结果如下：
'''                       
# for i in range(2):            (0, 0) (1, 0)
#     for j in range(3):        (0, 1) (1, 1)
#         print(i,j)            (0, 2) (1, 2)

'''
练习6-1：修改sketch_6_5_1.pyde,实现三层循环的嵌套。
'''
# for i in range(2):
#     for j in range(3):
#         for x in range(2):
#             print(i,j,x)

'''
·6.5绘制方块阵列
利用循环嵌套，通过设置方块的中心坐标，绘制出方块阵列
'''
# for x in range(100,401,30):   # 对x遍历
#     for y in range(100,401,30):   # 对y遍历
#         rectMode(CENTER)   # 矩形模式中心定位   ***其他代码同sketch_6_4_1.pyde
#         square(x,y,10)   # 画一个矩形
'''
·6.5绘制方块阵列
利用循环嵌套，通过变换坐标系的方法，绘制出方块阵列
'''
# for x in range(100,401,30):   # 对x遍历
#     for y in range(100,401,30):   # 对y遍历
#         rectMode(CENTER)   # 矩形模式中心定位   ***其他代码同sketch_6_4_1.pyde
#         pushMatrix()   # 保存之前的坐标系
#         translate(x,y)   # 移动坐标系原点
#         square(0,0,10)   # 在坐标系原点画一个矩形
#         popMatrix()       # 恢复到之前保存的坐标系
'''
·6.6方块阵列旋转缩放
'''
# def setup(): 
#     size(500, 500) # 设定画布大小
#     noFill()   # 不要填充颜色
#     strokeWeight(0.5)   # 制定边框线条粗细
#     stroke(50)   # 设定线条颜色为淡灰色，0为纯黑、255为纯白
# def draw():
#     background(255)   # 纯白背景
#     for x in range(100,401,30):   # 对x遍历
#         for y in range(100,401,30):   # 对y遍历
#             pushMatrix()   # 保存之前的坐标系
#             translate(x,y)   # 将坐标系原点移动到画面中心位置
#             rotate(radians(frameCount)) # 绕着坐标系原点旋转
#             # 当前缩放比例
#             currentScale = map(sin((frameCount+(x-y))/30.0),-1,1,0,4)
#             scale(currentScale)   # 缩放
#             square(0,0,10) # 在坐标系原点画一个矩形
#             popMatrix()   # 恢复到之前保存的坐标系
'''
·6.6方块阵列旋转缩放
当x=y时，sin((frameCount+(x-y))/60.0)的取值一样，因此可以
实现波浪斜向传播的效果
'''
# def setup(): 
#     size(500, 500) # 设定画布大小
#     noFill()   # 不要填充颜色
#     strokeWeight(0.5)   # 制定边框线条粗细
#     stroke(50)   # 设定线条颜色为淡灰色，0为纯黑、255为纯白
# def draw():
#     background(255)   # 纯白背景
#     for x in range(100,401,30):   # 对x遍历
#         for y in range(100,401,30):   # 对y遍历
#             pushMatrix()   # 保存之前的坐标系
#             translate(x,y)   # 将坐标系原点移动到画面中心位置
#             rotate(radians(frameCount)) # 绕着坐标系原点旋转
#             # 当前缩放比例
#             currentScale = map(sin((frameCount+(x-y))/60.0),-1,1,0,4)
#             scale(currentScale)   # 缩放
#             square(0,0,10) # 在坐标系原点画一个矩形
#             popMatrix()   # 恢复到之前保存的坐标系
'''
·6.6方块阵列旋转缩放
scale()会影响方块线条粗细，直接修改方块边长可实现不同大小方块同样粗细线条
'''
# def setup(): 
#     size(500, 500) # 设定画布大小
#     noFill()   # 不要填充颜色
#     strokeWeight(0.5)   # 制定边框线条粗细
#     stroke(50)   # 设定线条颜色为淡灰色，0为纯黑、255为纯白
# def draw():
#     background(255)   # 纯白背景
#     speed = radians(frameCount)
#     for x in range(100,401,30):   # 对x遍历
#         for y in range(100,401,30):   # 对y遍历
#             pushMatrix()   # 保存之前的坐标系
#             translate(x,y)   # 将坐标系原点移动到画面中心位置
#             rotate(radians(frameCount)) # 绕着坐标系原点旋转
#             # 当前缩放比例
#             currentScale = map(sin(speed-x*49-y*2),-1,1,35,35)
#             scale(currentScale)   # 缩放
#             square(0,0,10*currentScale) # 在坐标系原点画一个矩形
#             popMatrix()   # 恢复到之前保存的坐标系
'''
·6.7文字表情包
'''
# 1.print("haha 哈哈")
# 2.print(u"haha 哈哈")
'''
1.print()正常输出英文字符串，但是中文字符串为乱码  输出为：haha （由于键盘原因，请自行尝试！）
2.“u”为unicode编码的缩写，不仅适用英文和中文，而且支持全球所有文字的统一编码。  输出为：haha 哈哈
'''
'''
·6.8小结
·学习了循环嵌套的语法知识
·学习了方块的绘制、坐标系的变换、
  中文字符串的处理
·尝试用圆、圆弧、直线等元素或元素
  组合，修改宽度、高度、位置、旋转、
  明暗等参数，实现更多有趣的效果
'''

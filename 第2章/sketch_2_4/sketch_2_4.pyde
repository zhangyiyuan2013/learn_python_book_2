# def setup():
#     size(600,600)
# def draw():
#     circle(300,300,100)
# def setup():
#     size(600,600)
# def draw():
#     background(200)
#     circle(mouseX,mouseY,100)

# def setup():
#     size(600, 600)
    
# def draw():
#     background(255)
#     fill(180)
#     circle(300,300,300)
#     fill(235)
#     x1 = map(mouseX,0,width,260,340)
#     y1 = map(mouseY,0,height,260,340)
#     circle(x1,y1,200)
#     fill(0)
#     x2 = map(mouseX,0,width,220,380)
#     y2 = map(mouseY,0,height,220,380)
#     circle(x2,y2,100)

def setup():   # 初始化函数，仅运行一次
    size(800,600)  # 设定画面宽度、高度
    
def draw():  # 绘制函数，每帧重复运行
    background(255)  # 设置白色背景，并覆盖整个画面
    fill(255)  # 设置填充色为白色（默认黑色线条）
    circle(400,300,500)  # 绘制圆脸
    circle(305,180,180)  # 绘制左眼边框
    circle(495,180,180)  # 绘制右眼边框
    circle(400,300,40)   # 绘制鼻子
    circle(400,420,140)  # 绘制嘴巴
    fill(0)  # 设置填充色为黑色（用于绘制眼珠）
    # 将鼠标位置映射为左眼珠坐标
    x1 = map(mouseX,0,width,280,330)  
    y1 = map(mouseY,0,height,155,195)
    circle(x1,y1,110)  # 绘制左眼珠
    # 将鼠标位置映射为右眼珠坐标
    x2 = map(mouseX,0,width,470,520)
    y2 = map(mouseY,0,height,155,195)
    circle(x2,y2,110)  # 绘制右眼珠

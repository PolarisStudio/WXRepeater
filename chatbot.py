from wxpy import *
bot = Bot(cache_path=True)
group1 = bot.groups(update=False).search('北极星工作室')[0]
friend = bot.friends().search('friendname')[0]

group1.send('测试')
friend.send('测试')

# 信息 box
msgList = []

# 添加信息
def addMsg(msg):
    msgList.append(msg)

# 消息发送
def sendMsg():
    print('发送消息')
    friend.send(msgList.pop())

    # # 发送图片
    # my_friend.send_image('my_picture.png')
    # # 发送视频
    # my_friend.send_video('my_video.mov')
    # # 发送文件
    # my_friend.send_file('my_file.zip')
    # # 以动态的方式发送图片
    # my_friend.send('@img@my_picture.png')

# 监听
@bot.register(group1)
def message(msg):
    print('接收到：',msg) 
    ret = "收到你的消息："+msg
    return ret

# 线程阻塞，防止结束停止监听
embed()
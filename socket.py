import django
import socket
import time
def yimi(url):
    # with open("yimi.html", "rb") as f:
    with open("yimi.html", "r", encoding = 'utf-8') as f:
        ret = f.read()
    ret = ret.replace("@@xx@@", str(time.time()))
    return bytes(ret, encoding = 'utf-8')  # 只能发送字节

def xiaohei(url):
    ret = 'hello {}'.format(url)
    return bytes(ret, encoding = 'utf-8')

def f404(url):
    ret = "你访问的这个{}找不到".format(url)
    return bytes(ret, encoding="utf-8")

url_func = [("/yimi/", yimi), ("/xiaohei/", xiaohei)]

#生成socket实例对象
sk = socket.socket()
#绑定IP和端口
sk.bind(("127.0.0.1", 8001))
#监听
sk.listen()
#写一个死循环，一直等待客服端来连接
while True:
    #获取与客户端的连接
    conn, _ = sk.accept()
    #接收客户端发来消息
    data = conn.recv(8096)
    #print(data) # 字节类型
    #转换成字符串类型
    data_str = str(data, encoding="utf-8")  # bytes("str", encoding="utf-8)
    print("data_str", data_str)
    #用\r\n去切割上面的字符串
    l1 = data_str.split("\r\n")
    #print("l1[0]", l1[0])
    l2 =l1[0].split()
    print("l2", l2)
    url = l2[1]
    print("url", url)
    if url == '/favicon.ico':
        continue
    #给客户端回复消息
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n') #发送字节
    #想让浏览器在页面上显示出来的内容都是相应正文
    #根据不同的url返回不同的结果
    # if url == "/yimi/":
    #     response_str = yimi()
    # elif url == "/xiaohei/":
    #     response_str = b'<h1>hello xiaohei</h1>'
    # else:
    #     response_str = b'<h1>404! not found</h1>'
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
        else:
            func = f404
    response_str = func(url)
    conn.send(response_str)
    #关闭
    conn.close()
sk.close()
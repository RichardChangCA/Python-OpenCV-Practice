import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# matrix1 = tf.constant([[3, 3]])
# matrix2 = tf.constant([[2],
#                        [2]])
# product = tf.matmul(matrix1, matrix2)  #matrix multiply np.dot(m1, m2)
#
# # #method 1
# # sess = tf.Session()
# # result = sess.run(product)
# # print(result)
# # sess.close()
#
# #method 2
# with tf.Session() as sess:  #with后不用close
#     result2 = sess.run(product)
#     print(result2)


"""
每run一次，tensorflow跑一次
Ctrl + / 注释所选
有变量就要初始变量
tf.global_variables_initializer() 替代 tf.initialize_all_variables()
"""


# state = tf.Variable(0, name='counter')
# print(state.name)
# one = tf.constant(1)
#
# new_value = tf.add(state, one)
# update = tf.assign(state, new_value)
#
# init = tf.global_variables_initializer()  #must have if define variable
#
# with tf.Session() as sess:
#     sess.run(init)
#     for _ in range(3):
#         sess.run(update)
#         print(sess.run(state))  #注意要run才能显示

# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)   #placehold可以每次放进去不同的值
#
# output = tf.multiply(input1, input2)  #将mul换成multiply
#
# with tf.Session() as sess:
#     print(sess.run(output, feed_dict={input1: [7.], input2: [2.]}))


# 构建神经层
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)  # biases建议初始值不为0
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


x_data = np.linspace(-1, 1, 300)[:, np.newaxis]   # -1到1区间，300个单位（例子），加一个维度
noise = np.random.normal(0, 0.05, x_data.shape)  # mean = 0, standard deveiation = 0.05
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32, [None, 1])  # None代表可以加入任何参数，1维
ys = tf.placeholder(tf.float32, [None, 1])

l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)  # 输入1个神经元，输出10个神经元，relu激活函数
prediction = add_layer(l1, 10, 1, activation_function=None)  # 假设隐藏层有10个神经元

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))  # reduction_indices参数处理的维度
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

fig = plt.figure()  # 图片框
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
plt.ion()  # 持续plot
plt.show()

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        try:  # 第一次没抹除
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        lines = ax.plot(x_data, prediction_value, 'r', lw=5)  # 线的宽度为5，red色
        plt.pause(0.1)  # 暂停0.1s



# x = np.linspace(-1, 1, 10)
# y = x ** 2
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# lines = ax.plot(x, y, 'r',)
# plt.show()

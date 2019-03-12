import numpy as np
import tensorflow as tf

#create data
x_data = np.random.rand(100).astype(np.float32)  #tensorflow常处理的数据type为float32
y_data = x_data*0.1 + 0.3

#create tensorflow structure start
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  #一维，生成范围-1~1
biases = tf.Variable(tf.Variable(tf.zeros([1])))

y = Weights*x_data + biases  #预测值

loss = tf.reduce_mean(tf.square(y-y_data)) #损失函数
optimizer = tf.train.GradientDescentOptimizer(0.5)  #0.5学习效率，小于1的数
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
#create tensorflow structure end

sess = tf.Session()
sess.run(init)    #激活init   Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

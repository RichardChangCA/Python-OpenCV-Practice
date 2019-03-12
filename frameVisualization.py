import tensorflow as tf

def add_layer(inputs, in_size, out_size, activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')  # biases建议初始值不为0
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs


#define placeholder for inputs to network
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')  # None代表可以加入任何参数，1维
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

#add hidden layer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)  # 输入1个神经元，输出10个神经元，relu激活函数
#add output layer
prediction = add_layer(l1, 10, 1, activation_function=None)  # 假设隐藏层有10个神经元

#the error between prediction and real data
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))  # reduction_indices参数处理的维度
with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

sess = tf.Session()
writer = tf.summary.FileWriter("log/", sess.graph)
#important step
sess.run(tf.global_variables_initializer())


"""
activate tensorflow
进入目录
tensorboard --logdir=log
"""
import tensorflow as tf

tensor1 = tf.ones([1, 2, 3])

with tf.Session() as sess:
    tensor1.eval()
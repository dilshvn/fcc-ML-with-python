import tensorflow as tf

t1 = tf.zeros([5, 5, 5, 5])
t2 = tf.reshape(t1, [625])
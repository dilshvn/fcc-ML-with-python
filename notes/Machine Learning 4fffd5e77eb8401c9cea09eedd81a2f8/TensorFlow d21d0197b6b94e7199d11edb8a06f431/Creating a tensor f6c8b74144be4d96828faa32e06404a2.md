# Creating a tensor

## Creating a rank 0 tensor

```jsx
import tensorflow as tf

string = tf.Variable('this is a string', tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)
```

Here, first argument is the object and 2nd argument is the data type. These 3 tensors one dimensional. They are also called scalars (rank 0 tensors)

Rank is the number of dimensions involved in the tensor

## Creating high rank tensor

```jsx
rank1_tensor = tf.Variable([‘Test’], tf.string)
rank2_tensor = tf.Variable([[‘Test’, ‘ok’], [‘Test’, ‘Yes’]], tf.string)
```

Here, rank2_tensor has a list inside a list (nested list). This tensor is a matrix
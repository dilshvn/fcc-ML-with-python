# Changing shape of a tensor

```jsx
tensor1 = tf.ones([1,2,3])
tensor2 = tf.reshape(tensor1, [2,3,1])
```

tf.ones() creates a shape [1,2,3] tensor full of ones

[1,2,3] means 1 list has 2 lists and those 2 lists have 3 lists each
# Changing shape of a tensor (Reshaping)

```jsx
tensor1 = tf.ones([1, 2, 3])
tensor2 = tf.reshape(tensor1, [2, 3, 1])
tensor3 = tf.reshape(tensor2, [3, -1])
```

tf.ones() creates a shape [1, 2, 3] tensor full of ones

[1, 2, 3] means 1 list has 2 lists and those 2 lists have 3 lists each

Both former and reshaped tensors should have same number of elements

In the last line, -1 is used to let tensor calculate the size of that place which will result in (3, 2) because 3*2 is 6
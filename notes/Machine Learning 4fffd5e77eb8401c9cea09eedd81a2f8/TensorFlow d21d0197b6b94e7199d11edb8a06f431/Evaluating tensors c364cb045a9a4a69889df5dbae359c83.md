# Evaluating tensors

Evaluating tensor means getting its value. Sometimes, we have to run a ‘session’ to evaluate a tensor. 

This is how it’s done

```jsx
with tf.Session() as sess:
    tensor1.eval()
```

.Session() creates a session using default graph 

Here, we evaulate tensor1 variable that’s stored in default graph which holds all operations not specified to any other graph
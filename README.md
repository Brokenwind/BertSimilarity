# BertSimilarit
基于Google的BERT模型来进行语句相似性比较  
工程的入口文件为 similarity.py
## 训练阶段，在main函数中执行如下代码
```
    sim = BertSim()
    sim.set_mode(tf.estimator.ModeKeys.TRAIN)
    sim.train()
```

## 使用阶段，在main函数中执行如下代码
```
    sim = BertSim()
    sim.set_mode(tf.estimator.ModeKeys.PREDICT)
    while True:
        sentence1 = input('sentence1: ')
        sentence2 = input('sentence2: ')
        predict = sim.predict(sentence1, sentence2)
        print(f'similarity：{predict[0][1]}')

```

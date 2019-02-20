# BertSimilarit
基于Google的BERT模型来进行语句相似性比较
## 如何使用
工程中提供下载google bert模型的预训练模型chinese_L-12_H-768_A-12.zip，以及根据蚂蚁金服数据进行fine tune 之后的模型数据tmp.tgz。 下载脚本为 download.py。   
- 如果要自己根据数据体验训练，请下载google的预训练模型chinese_L-12_H-768_A-12,下载方式：    
在download.py的main函数中执行：
```
down.download(pre_train_url, 'chinese_L-12_H-768_A-12.zip')
```
- 如果想要要最终的训练结果，请下载tmp.tgz，下载方式：  
在download.py的main函数中执行：
```
down.download(final_train_model, 'tmp.tgz')
```
工程的入口文件为 similarity.py
### 训练阶段，在main函数中执行如下代码
```
    sim = BertSim()
    sim.set_mode(tf.estimator.ModeKeys.TRAIN)
    sim.train()
```

### 使用阶段，在main函数中执行如下代码
```
    sim = BertSim()
    sim.set_mode(tf.estimator.ModeKeys.PREDICT)
    while True:
        sentence1 = input('sentence1: ')
        sentence2 = input('sentence2: ')
        predict = sim.predict(sentence1, sentence2)
        print(f'similarity：{predict[0][1]}')

```

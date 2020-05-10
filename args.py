import os
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

PROJECT_ROOT_PATH = os.path.dirname(__file__)

data_path = os.path.join(PROJECT_ROOT_PATH, 'data')
dataset_path = os.path.join(data_path, 'dataset')
model_dir = os.path.join(data_path, 'pretrained_model/chinese_L-12_H-768_A-12/')
output_dir = os.path.join(data_path, 'model_ouput')

config_name = os.path.join(model_dir, 'bert_config.json')
ckpt_name = os.path.join(model_dir, 'bert_model.ckpt')
vocab_file = os.path.join(model_dir, 'vocab.txt')

num_train_epochs = 10
batch_size = 128
learning_rate = 0.00005

# gpu使用率
gpu_memory_fraction = 0.8

# 默认取倒数第二层的输出值作为句向量
layer_indexes = [-2]

# 序列的最大程度，单文本建议把该值调小
max_seq_len = 32

import os

read_file = "cnews.test.txt"
write_file = "data_test.txt"
fw = open(write_file, 'w', encoding='UTF-8')
with open(read_file, 'r', encoding='UTF-8') as p:
    for line in p.readlines():
        name = line.split('\t')[0]
        if name in ('体育','科技','教育','娱乐','财经'):
            fw.write(line.split('\t')[0] + '\t' + line.split('\t')[1])
print('test done!')


read_file = "cnews.train.txt"
write_file = "data_train.txt"
fw = open(write_file, 'w', encoding='UTF-8')
with open(read_file, 'r', encoding='UTF-8') as p:
    for line in p.readlines():
        name = line.split('\t')[0]
        if name in ('体育','科技','教育','娱乐','财经'):
            fw.write(line.split('\t')[0] + '\t' + line.split('\t')[1])
print('train done!')

read_file = "cnews.val.txt"
write_file = "data_val.txt"
fw = open(write_file, 'w', encoding='UTF-8')
with open(read_file, 'r', encoding='UTF-8') as p:
    for line in p.readlines():
        name = line.split('\t')[0]
        if name in ('体育','科技','教育','娱乐','财经'):
            fw.write(line.split('\t')[0] + '\t' + line.split('\t')[1])
print('val done!')

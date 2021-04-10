import matplotlib.pyplot as plt
import numpy as np

# save loss txt所在的路径
loss_save = '/home/fullo/公共的/fullo-Pixel2MeshPlusPlus-master/Pixel2MeshPlusPlus/results5/coarse_mvp2m/logs/train_loss_record.txt'
loss_save2 = '/home/fullo/公共的/fullo-Pixel2MeshPlusPlus-master/Pixel2MeshPlusPlus/results5/coarse_mvp2m/logs/vaild_loss_record.txt'

epp = []
epoch1 = []
Meanloss = []

with open(loss_save, 'r') as file:  # 打开文件
    num = 0
    for line in file.readlines():  # 文件内容分析成一个行的列表
        num = num+1
        if num!=1:
            line = line.strip().split(" ")  # 按照空格进行切分
            # print(line)
            s , ep , _ ,mloss = line[0], line[1] ,line[2] ,line[3]  # 一行拆分为三行
            ep = int(ep.split(',')[0])  # 保留itera参数
            epoch1.append(ep)  # 保存在数组中
            Meanloss.append(float(mloss))

epp2 = []
epoch2 = []
Meanloss2 = []


with open(loss_save2, 'r') as file:  # 打开文件
    num2 = 0
    for line in file.readlines():  # 文件内容分析成一个行的列表
        num2 = num2+1
        if num2!=1:
            line = line.strip().split(" ")  # 按照空格进行切分
            # print(line)
            s2 , ep2 , _, mloss2 = line[0], line[1] ,line[2] ,line[3]  # 一行拆分为三行
            mloss2 = float(mloss2)*10
            ep2 = int(ep2.split(',')[0])  # 保留itera参数
            epoch2.append(ep2)  # 保存在数组中
            Meanloss2.append(mloss2)

# 画图
plt.title('Loss')  # 标题
# plt.plot(x,y)
# 常见线的属性有：color,label,linewidth,linestyle,marker等
plt.plot(epoch1, Meanloss, color='cyan', label='train-loss')
plt.plot(epoch2, Meanloss2, 'b', label='vaild-loss')  # 'b'指：color='blue'
# plt.plot(iteration3, Loss3, 'r', label='loss_train100w_0.01')  # 'r'指：color='red'

plt.legend()  # 显示上面的labelprint('finish')
plt.xlabel('epoch')
plt.ylabel('loss')


# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
print('finish')
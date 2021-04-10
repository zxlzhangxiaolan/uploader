import matplotlib.pyplot as plt
import numpy as np

# save loss txt所在的路径
#loss_save = '/home/fullo/公共的/fullo-Pixel2MeshPlusPlus-master/Pixel2MeshPlusPlus/loss/loss.txt'
loss_save2 = '/home/fullo/公共的/fullo-Pixel2MeshPlusPlus-master/Pixel2MeshPlusPlus/results5/loss/vaildloss-p2mpp.txt'

epp = []
epoch1 = []
iteration1 = []
Meanloss = []
Iterloss = []
Imeanloss = []
z=1

# with open(loss_save, 'r') as file:  # 打开文件
#     for line in file.readlines():  # 文件内容分析成一个行的列表
#         line = line.strip().split(" ")  # 按照空格进行切分
#         # print(line)
#         ep, itera, mloss, iloss = line[0], line[1] ,line[2] ,line[3] # 一行拆分为三行
#         ep = int(ep.split(':')[1])  # 保留itera参数
#         epoch1.append(ep)  # 保存在数组中
#         if ep!=z:
#             epp.append(z)
#             mean = np.mean(Iterloss)
#             Imeanloss.append(mean)
#             Iterloss = []
#         itera = int(itera.split(':')[1])  # 保留itera参数
#         iteration1.append(itera)  # 保存在数组中
#         mloss = float(mloss.split(':')[1])
#         Meanloss.append(mloss)
#         iloss = float(iloss.split(':')[1])
#         Iterloss.append(iloss)
#         z=ep
#
# epp.append(z)
# mean = np.mean(Iterloss)
# Imeanloss.append(mean)

epp2 = []
epoch2 = []
iteration2 = []
Meanloss2 = []
Iterloss2 = []
Imeanloss2 = []
num=30

with open(loss_save2, 'r') as file:  # 打开文件
    for line in file.readlines():  # 文件内容分析成一个行的列表
        line = line.strip().split(" ")  # 按照空格进行切分
        # print(line)
        ep2, itera2,cdloss2 = line[0], line[1] ,line[2] # 一行拆分为三行
        ep2 = int(ep2.split(':')[1])  # 保留itera参数
        epoch2.append(ep2)  # 保存在数组中
        itera2 = int(itera2.split(':')[1])  # 保留itera参数
        iteration2.append(itera2)  # 保存在数组中
        cdloss2 = float(cdloss2.split(':')[1])
        if ep2==32:
            Iterloss2.append(cdloss2)


epp2.append(z)
mean2 = np.mean(Iterloss2)
Imeanloss2.append(mean2)
print('finish')
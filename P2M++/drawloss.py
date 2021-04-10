import matplotlib.pyplot as plt
import numpy as np

# save loss txt所在的路径
loss_save = '/home/fullo/公共的/fullo-Pixel2MeshPlusPlus-master/Pixel2MeshPlusPlus/loss/loss.txt'
loss_save2 = '/home/fullo/公共的/fullo-Pixel2MeshPlusPlus-master/Pixel2MeshPlusPlus/loss/vaildloss.txt'

epp = []
epoch1 = []
iteration1 = []
Meanloss = []
Iterloss = []
Imeanloss = []
z=1

with open(loss_save, 'r') as file:  # 打开文件
    for line in file.readlines():  # 文件内容分析成一个行的列表
        line = line.strip().split(" ")  # 按照空格进行切分
        # print(line)
        ep, itera, mloss, iloss = line[0], line[1] ,line[2] ,line[3] # 一行拆分为三行
        ep = int(ep.split(':')[1])  # 保留itera参数
        epoch1.append(ep)  # 保存在数组中
        if ep!=z:
            epp.append(z)
            mean = np.mean(Iterloss)
            Imeanloss.append(mean)
            Iterloss = []
        itera = int(itera.split(':')[1])  # 保留itera参数
        iteration1.append(itera)  # 保存在数组中
        mloss = float(mloss.split(':')[1])
        Meanloss.append(mloss)
        iloss = float(iloss.split(':')[1])
        Iterloss.append(iloss)
        z=ep

epp.append(z)
mean = np.mean(Iterloss)
Imeanloss.append(mean)

epp2 = []
epoch2 = []
iteration2 = []
Meanloss2 = []
Iterloss2 = []
Imeanloss2 = []
z2=1

with open(loss_save2, 'r') as file:  # 打开文件
    for line in file.readlines():  # 文件内容分析成一个行的列表
        line = line.strip().split(" ")  # 按照空格进行切分
        # print(line)
        ep2, itera2, mloss2, iloss2 = line[0], line[1] ,line[2] ,line[3] # 一行拆分为三行
        ep2 = int(ep2.split(':')[1])  # 保留itera参数
        epoch2.append(ep2)  # 保存在数组中
        if ep2!=z2:
            epp2.append(z2)
            mean2 = np.mean(Iterloss2)
            Imeanloss2.append(mean2)
            Iterloss2 = []
        itera2 = int(itera2.split(':')[1])  # 保留itera参数
        iteration2.append(itera2)  # 保存在数组中
        mloss2 = float(mloss2.split(':')[1])
        Meanloss2.append(mloss2)
        iloss2 = float(iloss2.split(':')[1])
        Iterloss2.append(iloss2)
        z2=ep2

epp2.append(z)
mean2 = np.mean(Iterloss2)
Imeanloss2.append(mean2)
# 画图
plt.title('Loss')  # 标题
# plt.plot(x,y)
# 常见线的属性有：color,label,linewidth,linestyle,marker等
plt.plot(epp, Imeanloss, color='cyan', label='train-loss')
plt.plot(epp2, Imeanloss2, 'b', label='vaild-loss')  # 'b'指：color='blue'
# plt.plot(iteration3, Loss3, 'r', label='loss_train100w_0.01')  # 'r'指：color='red'

plt.legend()  # 显示上面的labelprint('finish')
plt.xlabel('Iteration')
plt.ylabel('Loss')


# plt.ylim(-1,1)#仅设置y轴坐标范围
plt.show()
print('finish')
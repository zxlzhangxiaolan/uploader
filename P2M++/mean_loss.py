import glob
import os

path = '/home/fullo/公共的/fullo-Pixel2MeshPlusPlus-master/Pixel2MeshPlusPlus/results5/loss/vaildloss-p2mpp.txt'

f = open(path, 'r')
data = {}
lines = f.readlines()
for i in range(30, 35):
    data[i] = 0
for line in lines:
    data[int(line.split(':')[1].split()[0])] += float(line.split(':')[3])
print()
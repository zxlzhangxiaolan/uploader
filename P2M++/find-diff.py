# -*- coding: UTF-8 -*-

import re                                                 #使用正则库

# 打开文件
fo = open("/home/fullo/公共的/fullo-Pixel2MeshPlusPlus-master/Pixel2MeshPlusPlus/data/test_list_bak.txt", "r");
co = open("/home/fullo/公共的/fullo-Pixel2MeshPlusPlus-master/Pixel2MeshPlusPlus/data/vaild_list.txt", "r");

colines = co.readlines();                       #读取所有world文件中的行

for line in fo.readlines():                        #依次读取每行
    line = line.strip();                              #去掉每行头尾空白
    matchObj = re.search( line, "%s" %  colines, re.M | re.I);
   #正则匹配开始，使用search可以将全部符合条件的字符集都找出来
    if not matchObj:
        print(line);

# 关闭文件
fo.close();
co.close();
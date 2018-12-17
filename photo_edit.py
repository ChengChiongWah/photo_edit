# -*- coding: utf-8 -*-
#通过对2018级学生信息的数据整理后建议改成以学号作为文件名来导入，因为在整理的过程中学生提供的身份证号码有漏位和空格
#建议一个一个班导入，在按照名字匹配时需要检查名字重名的问题。

import os
import sys
import shutil
import re
import win32com.client

# 需要处理的图片的文件路径,每一个班级不同文件夹故每处理完要更改一次
# source_dir = r'C:\Users\wah\Desktop\18级大头照 - 副本\18级大头照\18高职中药学1班大头照\18高职中药学1班大头照'

#在所在文件路径新建一个文件夹
# target_dir = os.path.join(source_dir, "Result")
# os.makedirs(target_dir)

# 第一类：提供的图片名含有身份证号码的，则直接提取身份证号码作为新的图片文件名。
# for root, dirs, files in os.walk(source_dir):
#     print("-----")
#     print(root)  # os.walk()所在的目录
#     print(dirs)  #os.walk()所在目录的所有目录名
#     print(files)
#     if dirs:    #判断目录是否有文件
#         for f in files:  #所在目录的所有非目录文件名
#             print(f)
#             # name_target = f.rsplit(".", 1)[0].rsplit("-")[-1]      #获取身份证号码
#             # name_target = f.rsplit(".", 1)[0][-18:]                #获取身份证号码（采用取后18位的方法）
#             name_target = f[5:].split(" ", 1)[1][:18]        #获取身份证号码（格式3）
#             name_extension = f.rsplit(".", 1)[1]    #获取扩展名
#             print(name_target + "." + name_extension )
#             shutil.copy(os.path.join(source_dir, f), os.path.join(target_dir, name_target+"."+name_extension))


#第二类：提供的图片名只含有姓名和学号后三位的,把学生科提供的数据导入到access然后分析后的图片姓名对比。
# for root, dirs, files in os.walk(source_dir):
#     print("-----")
#     print(root)  # os.walk()所在的目录
#     print(dirs)  #os.walk()所在目录的所有目录名
#     print(files)
#     if dirs:    #判断目录是否有文件
#         for f in files:  #所在目录的所有非目录文件名
#             # print(f)
#             # name_target = f.rsplit(".", 1)[0].rsplit("-")[-1]      #获取身份证号码
#             # name_target = f.rsplit(".", 1)[0][-18:]                #获取身份证号码（采用取后18位的方法）
#             name_target = f.split(".", 2)[1]        #获取学生姓名（格式3）
#             # number_student = f.split(" ", 2)[2]     # 获取学号
#             # print(number_student)
#             name_extension = f.rsplit(".", 1)[1]    #获取扩展名
#             # print(name_target + "." + name_extension )
#
#             with open(r"C:\Users\wah\Desktop\18级大头照 - 副本\18级大头照\18高职中药学1班大头照\身份证学号姓名明细.txt", "r", encoding="utf-8") as files:
#                 counter_check_name = 0    #添加一个计数器检测是否有重名的
#                 for line in files.readlines():
#                     if name_target in line:
#                         counter_check_name = counter_check_name + 1
#                         print(name_target, line.split("	", 2)[2][1:19], counter_check_name)  #运行一次后人工查看counter_check_name > 1的，有的话出现重名
#                     # print(line.split("	", 2)[0], line.split("	", 2)[1], line.split("	", 2)[2])
#                         shutil.copy(os.path.join(source_dir, f), os.path.join(target_dir, line.split("	", 2)[2][1:19]+"."+name_extension))

# 　对处理后的数据进行检测
source_dir = r'C:\Users\wah\Desktop\18药物制剂1班\18药物制剂1班-王莎（79人）'
for root, dirs, files in os.walk(source_dir):
    for f in files:
        if " " in f:      # 检测是否有空格
            print(f, "有空格")
        if len(f.rsplit(".",1)[0]) != 18:  #从右边第一个.符号起切片，看左边的字符是否18位。
            print(f, len(f.split(".",1)[0]))
    for f in files:
        print(f.rsplit(".", 1)[0], len(f.rsplit(".", 1)[0]))

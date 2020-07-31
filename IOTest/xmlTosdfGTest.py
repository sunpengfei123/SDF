from SDFIO import xmlTosdfG
from analysis import HSDF_CP as Hcp
import networkx as nx
import matplotlib.pyplot as plt
import os

# 测试图的文件夹目录
filedir = 'E:\\TestCase\\HSDFGs'

# files = os.listdir(filedir)  # 得到文件夹下的所有文件名称
#
# for file in files: # 遍历文件夹
#     print(os.path.isdir(filedir+'\\'+file))
#     if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
#         print(file)
#         file = os.path.splitext(file)
#         filename, type = file
#         if type == '.xml':
#             test_path = filedir+"\\"+file
#             print(test_path)

test_path = []

def getfile(path):
    filedir = path
    files = os.listdir(filedir)  # 得到文件夹下的所有文件名称

    for file in files:  # 遍历文件夹
        if not os.path.isdir(filedir+'\\'+file):  # 判断是否是文件夹，不是文件夹才打开
            file_mess = os.path.splitext(file)
            filename, type = file_mess
            if type == '.xml':
                test_path.append(filedir + '\\' + file)
        else:
            getfile(filedir+'\\'+file)

getfile(filedir)
print(test_path)

for path in test_path:
    t = xmlTosdfG.xmlTosdfG(path)

    g = t.get_sdfG()

    # nx.draw_networkx(g.getsdfG())
    # plt.show()

    Hsdf_Cp = Hcp.HSDF_CP(g)
    p = Hsdf_Cp.clockPeriod()
    print(path)
    print(p)

# path = 'E:\\TestCase\\HSDFGs\\ha1k\\ha1k-000.xml'
# t = xmlTosdfG.xmlTosdfG(path)
#
# g = t.get_sdfG()
#
# # nx.draw_networkx(g.getsdfG())
# # plt.show()
#
# Hsdf_Cp = Hcp.HSDF_CP(g)
# p = Hsdf_Cp.clockPeriod()
# print(p)


import pandas as pd
import networkx as nx
import numpy as np

class code_translate():
    """本类主要
    实现将matlab代码实现为py代码"""
    def __init__(self):
        self.num_industry = 45
        self.num_province = 31
        self.name = pd.read_csv("data/nmInd.csv",header=None)[0].tolist()
        pass
    def drawCountryNet(self,pi):
        """根据参数
        绘制指定省份的内部产业网络。
        :param pi:大陆省份代号，取值从0-31"""
        # 创建一个digraph
        inoutput2017  = pd.read_csv('data/inoutput2017.csv', header=None, names=["col_{}".format(i) for i in range(1395)])
        for i in range(inoutput2017.shape[0]):
            inoutput2017.iloc[i,i]=0
        start = pi * self.num_industry
        end = (1+pi) * self.num_industry
        data_index = list(range(start, end))
        tnet = inoutput2017.iloc[data_index,data_index]
        tg = nx.DiGraph()
        tg.add_nodes_from(self.name)
        for i in range(45):
            for j in range(45):
                    start_node = self.name[i]
                    end_node = self.name[j]
                    weight = tnet.iloc[i,j]
                    tg.add_edge(start_node, end_node,weight=weight)
        
        tP = self.drawNetworkG(tg,8,8,{},{},'b')
    
    
    def drawNetworkG(self,G,vn,en,nl,el,ctype):
        """复杂网络的可视化函数
        :param G:图对象
        :param vn:节点分组,如果已经分好了组,那么vn为一个列向量,组别是从1开始的自然数
        :param en:是否按照边权绘图
        :param nl:节点标签，为空则不绘制标签
        :param el:
        :param ctype:绘图颜色
        :return p:图形对象
        """
        n = len(list(G.nodes))  # 节点的数量
        e = len(list(G.edges))  # 边的数量
        es = np.ones((e,1))  # 边的组别（粗细与颜色深浅)
        vs = np.zeros((n,3))  # 节点组别（大小）和坐标
        nx_max = 10  # 最大分许
        lv = len(vn)
        if lv == 1:
            vn = max(min(vn,nx),1)  # 节点分组范围[1,8]
        else:
            tvn = max(vn) - vn + 1
            vn = max(vn)
            
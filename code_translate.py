import pandas as pd

class code_translate():
    """本类主要
    实现将matlab代码实现为py代码"""
    def __init__(self):
        self.num_industry = 45
        self.num_province = 31
        pass
    def drawCountryNet(self,pi):
        """根据参数
        绘制指定省份的内部产业网络。
        :param pi:大陆省份代号，取值从0-31"""
        inoutput2017  = pd.read_csv('data/inoutput2017.csv', header=None, names=["col_{}".format(i) for i in range(1395)])
        for i in range(inoutput2017.shape[0]):
            inoutput2017.iloc[i,i]=0
        start = pi * self.num_industry
        
        
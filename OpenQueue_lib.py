import numpy as np
from numpy.linalg import solve 

class OpenQueue_lib:

    def __init__(self, p):
        self.p = p

    #開放型ネットワークのノード到着率αを求める
    def getOpenTraffic(self, lmd): 
        e = np.eye(len(self.p)) #Pと同じ大きさの単位行列
        pe = self.p.T - e # P転置と単位行列の差(対角要素の引き算)
        slv = solve(pe, lmd * (-1))
        return slv

    #開放型ネットワークで人数分布が与えられたときの定常分布(積形式解)
    def getOpenStationary(self, n, lmd, mu):
        rho = lmd / mu
        st = 1 #積になるので初期値は1
        for i in range(len(n)):
            st *= (1 - rho[i]) * (rho[i] ** n[i])
        return st

    #M/M/1平均系内人数
    def getMM1Length(self, lmd, mu):
        rho = lmd / mu
        l = rho / (1 - rho)
        return l


    #閉鎖型ネットワークのノード到着率αを求める
    #https://mizunolab.sist.ac.jp/2019/09/bcmp-network1.html
    def getCloseTraffic(self):
        e = np.eye(len(self.p)-1) #次元を1つ小さくする
        pe = self.p[1:len(self.p), 1:len(self.p)].T - e #行と列を指定して次元を小さくする
        lmd = self.p[0, 1:len(self.p)] #0行1列からの値を右辺に用いる
        slv = solve(pe, lmd * (-1))
        return slv
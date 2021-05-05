import OpenQueue_lib as mdl
import numpy as np

p = np.array([[0, 0, 1], [0, 0, 0.6], [0.5, 0, 0]])#開放型の例(ORの基礎P153)
mu = np.array([5.0, 4.0, 6.0])

#p = np.array([[0, 0.5, 0.5], [0, 0, 1.0], [1.0, 0, 0]]) #閉鎖型の例
qlib = mdl.OpenQueue_lib(p)

#開放型の場合
lmd = np.array([2, 1, 0])#開放型外部到着率
alpha = qlib.getOpenTraffic(lmd)
print('各ノードへの到着率 : {0}'.format(alpha))

l = qlib.getMM1Length(alpha, mu)
print('平均系内人数 : {0}'.format(l))

st = qlib.getOpenStationary(l, alpha, mu)
print('人数分布{0}のときの定常分布 : {1}'.format(l, st))

#閉鎖型の場合
#alpha = qlib.getCloseTraffic() #α1 = 1とする
#print('各ノードへの到着率 : {0}'.format(alpha))

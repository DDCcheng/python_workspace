import matplotlib.pyplot as plt
import  numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'   # 使图形中的中文正常编码显示
plt.rcParams['axes.unicode_minus'] = False

x=np.arange(-10,10,0.4)
y=x*x+2*x+1

plt.plot(x,y,'ro-.')

plt.xlabel("tick")
plt.ylabel("voltage")
plt.title("抛物线示意图")

plt.savefig("test",dpi=300)
plt.show()





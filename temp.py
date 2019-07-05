import numpy as np
import matplotlib.pyplot as plt



# 直方图

a = np.random.randint(0,20,10000)
b = np.arange(1,10001)
y = a[0::3]
y1 = a[1::3]
y2 = a[2::3]

x = b[0::3]
x1 = b[1::3]
x2 = b[2::3]

rate = (len(y) - list(y).count(0))/len(y)
rate1 = (len(y1) - list(y1).count(0))/len(y1)
rate2 = (len(y2) - list(y2).count(0))/len(y2)

plt.bar(x, y, color='yellow', label="x   rate:{0:.2f}".format(rate),width=1)
plt.bar(x1, y1, color="red",label="x1 rate:{0:.2f}".format(rate1), width=1)
plt.bar(x2, y2, color="green", label='x2 rate:{0:.2f}'.format(rate2), width=1)

plt.legend() # 添 加 图 例
plt.ylim(0,30) # 设 置 y 轴 的 最 大 高 度

plt.ylabel("random")
plt.xlabel("x")
plt.title("random.randint")
plt.show()

# 饼状图
"""
def pie(
        x, explode=None, labels=None, colors=None, autopct=None,
        pctdistance=0.6, shadow=False, labeldistance=1.1,
        startangle=None, radius=None, counterclock=True,
        wedgeprops=None, textprops=None, center=(0, 0), frame=False,
        rotatelabels=False, *, data=None):
    return gca().pie(
        x, explode=explode, labels=labels, colors=colors,
        autopct=autopct, pctdistance=pctdistance, shadow=shadow,
        labeldistance=labeldistance, startangle=startangle,
        radius=radius, counterclock=counterclock,
        wedgeprops=wedgeprops, textprops=textprops, center=center,
        frame=frame, rotatelabels=rotatelabels, **({"data": data} if
        data is not None else {}))
"""



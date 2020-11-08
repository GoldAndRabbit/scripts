import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

CHINESE_FONT_PATH = '/home/psdz/anaconda3/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/NotoSansCJK-Regular.ttc'
font = font_manager.FontProperties(fname=CHINESE_FONT_PATH)

x  = np.arange(1, 20, 1)
y1 = x * x
y2 = np.log(x)

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)

# 合并双轴图例
ln1 = ax1.plot(x, y1, label="$y1 = x * x$", color="r")
ax2 = plt.twinx()
ln2 = ax2.plot(x, y2, label="$y2 = log(x)$")
lns = ln1 + ln2
labs = [l.get_label() for l in lns]

ax1.legend(lns, labs, loc='best')
ax1.set_xticks(range(1, 20, 1))
ax1.set_xlabel("Compare y1 and y2")
ax1.set_ylabel("y1")
ax1.grid()
ax1.set_title('双y轴趋势图', fontproperties=font)
ax2.set_ylabel("y2")


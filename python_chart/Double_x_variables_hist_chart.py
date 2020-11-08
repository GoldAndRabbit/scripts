import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

CHINESE_FONT_PATH = '/home/psdz/anaconda3/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/NotoSansCJK-Regular.ttc'
font = font_manager.FontProperties(fname=CHINESE_FONT_PATH)

x_labels = ['G1','G2','G3','G4','G5']
y1       = [20,34,30,35,27]
y2       = [25,32,34,20,25]

x = np.arange(len(x_labels))    # the label locations
width = 0.35                    # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, y1, width, label='y1')
rects2 = ax.bar(x + width / 2, y2, width, label='y2')

ax.set_ylabel('y')
ax.set_title('双变量柱状图', fontproperties=font)
ax.set_xticks(x)
ax.set_ylim(0, 40)
ax.set_xticklabels(x_labels)
ax.grid()
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center',
            va='bottom'
        )

autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()
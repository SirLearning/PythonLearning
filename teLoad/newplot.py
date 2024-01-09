import matplotlib.pyplot as plt

# 提供数据
categories = ['DHH', 'DTA', 'DTC', 'DTH', 'DTM', 'DTT', 'DTX', 'DXX', 'RIX', 'RLC', 'RLG', 'RLX', 'XXX']
counts = [735, 1194, 1095976, 48828, 95785, 184898, 108199, 12509, 109873, 596077, 1586131, 147763, 285813]

# 计算百分比
total_counts = sum(counts)
percentages = [count / total_counts * 100 for count in counts]

# 创建水平条形图
fig, ax = plt.subplots()

# 绘制条形图
bars = ax.barh(categories, counts, color='#6780B6')

# 添加标签，显示百分比
for bar, count, percent in zip(bars, counts, percentages):
    ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{percent:.1f}%', ha='left', va='center')

# 添加标题和标签
ax.set_title('Category Percentages')
ax.set_xlabel('Counts')
ax.set_ylabel('Categories')

# 显示图表
plt.show()

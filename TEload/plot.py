import matplotlib.pyplot as plt

# 提供数据
categories = ['DHH', 'DTA', 'DTC', 'DTH', 'DTM', 'DTT', 'DTX', 'DXX', 'RIX', 'RLC', 'RLG', 'RLX', 'XXX']
counts = [735, 1194, 1095976, 48828, 95785, 184898, 108199, 12509, 109873, 596077, 1586131, 147763, 285813]

# 创建条形图
plt.bar(categories, counts, color='blue')

# 添加标题和标签
plt.title('Category Counts')
plt.xlabel('Categories')
plt.ylabel('Counts')

# 显示图表
plt.show()

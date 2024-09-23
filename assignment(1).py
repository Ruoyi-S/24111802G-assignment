import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

# 新的CSV文件的URL
url = "https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_1min_temperature.csv"

# 从URL下载CSV文件
response = requests.get(url)
response.raise_for_status()  # 确保请求成功

# 将下载的内容转换为一个可读的CSV格式
csv_data = StringIO(response.text)

# 使用pandas读取CSV数据
data = pd.read_csv(csv_data)

# 查看数据的前几行和列名，确保数据结构正确
print(data.head())
print(data.columns)

# 假设CSV文件有'Automatic Weather Station', 'Air Temperature(degree Celsius)'等列
# 重命名列名以匹配正确的含义
data.columns = ['DateTime', 'Automatic Weather Station', 'Air Temperature(degree Celsius)']

# 将温度列转换为浮点数类型
data['Air Temperature(degree Celsius)'] = data['Air Temperature(degree Celsius)'].astype(float)

# 设置图表大小
plt.figure(figsize=(12, 6))

# 绘制折线图，并在每个数据点上添加气泡标记
plt.plot(data['Automatic Weather Station'], data['Air Temperature(degree Celsius)'], color='pink', linestyle='-', linewidth=2, marker='o', markersize=8, markerfacecolor='white', markeredgewidth=2, markeredgecolor='pink')

# 设置图表的标题和坐标轴名称
plt.title('Air Temperature by Automatic Weather Station', fontsize=16)
plt.xlabel('Automatic Weather Station', fontsize=12)
plt.ylabel('Air Temperature (°C)', fontsize=12)

# 旋转x轴标签以便更好地显示站点名称
plt.xticks(rotation=90)

# 调整布局以防止标签被截断
plt.tight_layout()

# 显示图表
plt.show()
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import StrMethodFormatter
chipotle_data = []
with open('chipotle.tsv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        chipotle_data.append(row)
'''
1. 가장 많이 팔린 메뉴와, 가장 매출이 큰 메뉴 조사
2. 추가 메뉴의 빈도 조사 → 얼만큼 많은 재료를 미리 발주해야 하나
3. 최대 주문 금액 달성한 사람의 결제 금액 구하기, 평균과 비교
4. 매장의 순이익 구하기
    - Salsa: 3.5%
    - Izze: 5%
    - Nectar: 7%
    - Bowl: 10 %
    - Chips: 9.5%
    - Burrito: 6.8 %
    - Tacos: 8.5%
    - Guacamole: 10%
    - Soda: 15%
    - Water: 20%
'''

print("1---------------------------------------------------------------------------------------------------------------------------------------------------------")

chipotle_items_data = {}
for i in range(1, len(chipotle_data)):
    if chipotle_data[i][2] in chipotle_items_data:
        chipotle_items_data[chipotle_data[i][2]] += int(chipotle_data[i][1])
    else:
        chipotle_items_data[chipotle_data[i][2]] = int(chipotle_data[i][1])
chipotle_item_data = sorted(
    chipotle_items_data.items(), key=lambda x: x[1], reverse=False)
print(chipotle_item_data)

chipotle_item_data = np.array(chipotle_item_data)
x = chipotle_item_data[:, 0]
y = np.array(chipotle_item_data[:, 1], dtype="float32")

plt.xlabel('Kinds')
plt.ylabel('Quantity')
plt.bar(x, y, width=0.7, color='green')
plt.xticks(rotation=90, fontsize=8)
plt.subplots_adjust(bottom=0.3)
plt.show()

chipotle_sold_data = {}
for i in range(1, len(chipotle_data)):
    if chipotle_data[i][2] in chipotle_sold_data:
        chipotle_sold_data[chipotle_data[i][2]
                           ] += float(chipotle_data[i][4][1:])
    else:
        chipotle_sold_data[chipotle_data[i][2]
                           ] = float(chipotle_data[i][4][1:])
chipotle_sold_data = sorted(
    chipotle_sold_data.items(), key=lambda x: x[1], reverse=False)

print(chipotle_sold_data)

chipotle_sold_data = np.array(chipotle_sold_data)
x = chipotle_sold_data[:, 0]
y = np.array(chipotle_sold_data[:, 1], dtype="float32")

plt.xlabel('Kinds')
plt.ylabel('Sales($)')
plt.bar(x, y, width=0.7, color='blue')
plt.xticks(rotation=90, fontsize=8)
plt.subplots_adjust(bottom=0.25)
# plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
plt.show()


print("2---------------------------------------------------------------------------------------------------------------------------------------------------------")
chipotle_element_data = {}
for i in range(1, len(chipotle_data)):
    if ', [' in chipotle_data[i][3]:
        for j in chipotle_data[i][3].split(', [')[1][:-2].split(', '):
            if j in chipotle_element_data:
                chipotle_element_data[j] += 1
            else:
                chipotle_element_data[j] = 1

chipotle_element_data = sorted(
    chipotle_element_data.items(), key=lambda x: x[1], reverse=False)

print(chipotle_element_data)

chipotle_element_data = np.array(chipotle_element_data)
x = chipotle_element_data[:, 0]
y = np.array(chipotle_element_data[:, 1], dtype="int32")

plt.xlabel('Kinds')
plt.ylabel('Quantity')
plt.bar(x, y, width=0.7, color='violet')
plt.xticks(rotation=90, fontsize=8)
plt.subplots_adjust(bottom=0.25)
plt.show()

print("3---------------------------------------------------------------------------------------------------------------------------------------------------------")

chipotle_deep_pocketers_data = {}
for i in range(1, len(chipotle_data)):
    if chipotle_data[i][0] in chipotle_deep_pocketers_data:
        chipotle_deep_pocketers_data[chipotle_data[i]
                                     [0]] += float(chipotle_data[i][4][1:])
    else:
        chipotle_deep_pocketers_data[chipotle_data[i][0]] = float(
            chipotle_data[i][4][1:])
chipotle_deep_pocketers_data = sorted(
    chipotle_deep_pocketers_data.items(), key=lambda x: x[1], reverse=False)

print(chipotle_deep_pocketers_data)

chipotle_deep_pocketers_data = np.array(chipotle_deep_pocketers_data)
x = chipotle_deep_pocketers_data[:, 0]
y = np.array(chipotle_deep_pocketers_data[:, 1], dtype="float32")
print(np.mean(y))
'''
plt.xlabel('Order_ID')
plt.ylabel('Sales($)')
plt.bar(x, y, width=0.7, color='pink')
plt.xticks(rotation=90, fontsize=3)
plt.show()
'''
print("4---------------------------------------------------------------------------------------------------------------------------------------------------------")

chipotle_net_profit_data = {'Salsa': 0, 'Izze': 0, 'Nectar': 0, 'Bowl': 0,
                            'Chips': 0, 'Burrito': 0, 'Tacos': 0, 'Guacamole': 0, 'Soda': 0, 'Water': 0}

chipotle_net_profit_percent_data = {'Salsa': 0.035, 'Izze': 0.05, 'Nectar': 0.07, 'Bowl': 0.1,
                                    'Chips': 0.095, 'Burrito': 0.068, 'Tacos': 0.085, 'Guacamole': 0.1, 'Soda': 0.15, 'Water': 0.2}

for i in range(1, len(chipotle_data)):
    for key, value in chipotle_net_profit_percent_data.items():
        if key in chipotle_data[i][2]:
            chipotle_net_profit_data[key] += float(
                chipotle_data[i][4][1:])*value

chipotle_net_profit_data = sorted(
    chipotle_net_profit_data.items(), key=lambda x: x[1], reverse=False)

print(chipotle_net_profit_data)

chipotle_net_profit_data = np.array(chipotle_net_profit_data)
x = chipotle_net_profit_data[:, 0]
y = np.array(chipotle_net_profit_data[:, 1], dtype="float32")

plt.xlabel('Kinds')
plt.ylabel('Net_profit($)')
plt.bar(x, y, width=0.7, color='orange')
plt.xticks(rotation=90, fontsize=8)
plt.subplots_adjust(bottom=0.25)
plt.show()

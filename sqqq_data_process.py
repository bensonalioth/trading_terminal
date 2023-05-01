import re
import numpy as np

with open(r"D:\trade_big_data\SQQQ_subjects.txt", "r") as file:
    lines = file.readlines()



pattern = r'(BOUGHT|SOLD) (\d+) (\w+) @ (\d+\.\d{0,4}\b) \((\w+)\)'

results = []
profits = []  # 增加一个profits数组

for line in lines:
    match = re.search(pattern, line)
    if match:
        # 將匹配結果存儲到一個列表中
        result = [match.group(1), match.group(2), match.group(3), match.group(4), match.group(5)]
        # 將列表加入到結果列表中
        results.append(result)

# 遍歷結果列表，打印每個存儲的字串
for result in results:
    print(f'{result[0]} {result[1]} {result[2]} @{result[3]} ({result[4]})')
        
        

        
def calculate_earning(results):
    total_amount = 0
    total_cost = 0.0
    

    for result in results:
        action = result[0]
        amount = int(result[1])
        price = float(result[3])

        if action == 'BOUGHT':
            total_amount += amount
            total_cost += amount * price
            average_price = total_cost / total_amount
        elif action == 'SOLD':
            # 如果售出的數量大於持有的數量，就報錯
            if amount > total_amount:
                raise ValueError('SOLD amount is greater than holdings')

            profit = amount * (price - average_price)
            profit_sqqq=round(profit,3)
            profits.append(profit_sqqq)
            total_cost -= amount * average_price
            total_amount -= amount
        
        else:
            raise ValueError(f'Invalid action: {action}')
            

        if total_amount == 0:
            average_price=0
            continue
            
        print(f'Holdings: {total_amount}, Average Price: {average_price}')

    # 如果遍歷完成後還有持有的股票，就打印出持有的數量和加權平均持有價格
    if total_amount > 0:
        average_price = total_cost / total_amount
        print(f'Unsold Holdings: {total_amount}, Average Price: {average_price}')

    # 打印profits数组中存储的利润信息
    if profits:
        print(f'Profits: {profits}')

        

weighted_avg = calculate_earning(results)




SQQQ_profits = np.array(profits)

np.set_printoptions(sign=' ', # 使用空格作為正負號的分隔符
                    precision=2, # 只保留小數點後兩位
                    suppress=True, # 禁止科學記號
                    floatmode='fixed', # 禁止科學記號
                    formatter={'float_kind':lambda x: f"{x:+.2f}"} # 每個數字的格式
                   )

print(SQQQ_profits)

with open('SQQQ_profits.txt','a') as file:
    np.savetxt(file, SQQQ_profits.reshape(1,-1), delimiter=',', fmt='%.2f')
    
    
with open('TandS_profits.txt','a') as file:
     np.savetxt(file, SQQQ_profits.reshape(1,-1), delimiter=',', fmt='%.2f')








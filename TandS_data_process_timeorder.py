import re
import numpy as np

filename = 'D:\\trading_terminal\\trading_terminal\\TandS_profits_timeorder.txt'
with open(filename, 'w') as file:
    # 使用 truncate() 函數將檔案內容清空
    file.truncate()

with open(r"D:\\trading_terminal\\trade_big_data\\email_subjects.txt", "r") as file:
    lines = file.readlines()


TandS_profits_thirty= [] 

pattern = r'(BOUGHT|SOLD) (\d+) (TQQQ|SQQQ) @ (\d+\.\d{0,4}\b) \((\w+)\)'

results = []

for line in lines:
    match = re.search(pattern, line)
    if match:
        
        result = [match.group(1), match.group(2), match.group(3), match.group(4), match.group(5)]
        
        results.append(result)

for result in results:
    print(f'{result[0]} {result[1]} {result[2]} @{result[3]} ({result[4]})')
        
        

 
def calculate_earning(results):
    tqqq_pre_amount = 0
    tqqq_average_price=0
    
    tqqq_profit=0.0
    
    sqqq_pre_amount = 0
    sqqq_average_price=0
    
    sqqq_profit=0.0
    

    for result in results:
        action = result[0]
        stock =result[2]
        amount = int(result[1])
        price = float(result[3])
        if stock=='TQQQ':
            if action == 'BOUGHT':
                tqqq_average_price = ((amount*price)+(tqqq_pre_amount*tqqq_average_price))/(tqqq_pre_amount+amount)
                tqqq_pre_amount+=amount
            elif action == 'SOLD':
                if amount > tqqq_pre_amount:
                    raise ValueError('SOLD amount is greater than holdings')

                tqqq_profit = amount * (price - tqqq_average_price)
                tqqq_profit=round(tqqq_profit,3)
                TandS_profits_thirty.append(tqqq_profit)
                
                tqqq_pre_amount -= amount
                with open('D:\\trading_terminal\\trading_terminal\\TandS_profits_timeorder.txt', 'a') as f:
                    f.write('%.2f\n'%tqqq_profit)
            else:
                raise ValueError(f'Invalid action: {action}')
            if tqqq_pre_amount == 0:
                tqqq_average_price=0
                continue
            
            print(f'Holdings: {tqqq_pre_amount}, Average Price: {tqqq_average_price}')

            
            if tqqq_pre_amount > 0:
                
                print(f'Unsold Holdings: {tqqq_pre_amount}, Average Price: {tqqq_average_price}')
        if stock=='SQQQ':
            if action == 'BOUGHT':
                sqqq_average_price = ((amount*price)+(sqqq_pre_amount*sqqq_average_price))/(sqqq_pre_amount+amount)
                sqqq_pre_amount+=amount
            elif action == 'SOLD':
                if amount > sqqq_pre_amount:
                    raise ValueError('SOLD amount is greater than holdings')

                sqqq_profit = amount * (price - sqqq_average_price)
                sqqq_profit=round(sqqq_profit,3)
                TandS_profits_thirty.append(sqqq_profit)
                
                sqqq_pre_amount -= amount
                with open('D:\\trading_terminal\\trading_terminal\\TandS_profits_timeorder.txt', 'a') as f:
                    f.write('%.2f\n'%sqqq_profit)
            else:
                raise ValueError(f'Invalid action: {action}')
            if sqqq_pre_amount == 0:
                sqqq_average_price=0
                continue
            
            print(f'Holdings: {sqqq_pre_amount}, Average Price: {sqqq_average_price}')

            
            if sqqq_pre_amount > 0:
                
                print(f'Unsold Holdings: {sqqq_pre_amount}, Average Price: {sqqq_average_price}')
                

weighted_avg = calculate_earning(results)


# 開啟A文件，讀取內容
with open('D:\\trading_terminal\\trading_terminal\\TandS_pre_profits_timeorder.txt', 'r') as file:
    a_content = file.read()

# 開啟B文件，讀取內容
with open('D:\\trading_terminal\\trading_terminal\\TandS_profits_timeorder.txt', 'r') as file:
    b_content = file.read()

# 將B文件的內容串接於A文件之後
a_content += b_content

# 開啟real文件，將串接後的內容寫入
with open('D:\\trading_terminal\\trading_terminal\\TandS_real_profits_timeorder.txt', 'w') as file:
    file.write(a_content)



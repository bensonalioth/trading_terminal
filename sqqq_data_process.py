import re
import numpy as np

with open(r"D:\\trading_terminal\\trade_big_data\\SQQQ_subjects.txt", "r") as file:
    lines = file.readlines()



pattern = r'(BOUGHT|SOLD) (\d+) (\w+) @ (\d+\.\d{0,4}\b) \((\w+)\)'

results = []
profits = []  # 增加一个profits数组

for line in lines:
    match = re.search(pattern, line)
    if match:
        
        result = [match.group(1), match.group(2), match.group(3), match.group(4), match.group(5)]
       
        results.append(result)

for result in results:
    print(f'{result[0]} {result[1]} {result[2]} @{result[3]} ({result[4]})')
        
        

        
def calculate_earning(results):

    pre_amount = 0
    average_price=0

    for result in results:
        action = result[0]
        amount = int(result[1])
        price = float(result[3])

        if action == 'BOUGHT':
            average_price = ((amount*price)+(pre_amount*average_price))/(pre_amount+amount)
            pre_amount+=amount
        elif action == 'SOLD':
            
            if amount > pre_amount:
                raise ValueError('SOLD amount is greater than holdings')

            profit = amount * (price - average_price)
            profit_sqqq=round(profit,3)
            profits.append(profit_sqqq)
            pre_amount -= amount
            
        
        else:
            raise ValueError(f'Invalid action: {action}')
            

        if pre_amount == 0:
    
            average_price=0
            continue
            
        print(f'Holdings: {pre_amount}, Average Price: {average_price}')

    
    if pre_amount > 0:
    
        print(f'Unsold Holdings: {pre_amount}, Average Price: {average_price}')

    
    if profits:
        print(f'Profits: {profits}')

        

weighted_avg = calculate_earning(results)




SQQQ_profits = np.array(profits)

np.set_printoptions(sign=' ', 
                    precision=2,
                    suppress=True, # 禁止科學記號
                    floatmode='fixed', # 禁止科學記號
                    formatter={'float_kind':lambda x: f"{x:+.2f}"} 
                   )

print(SQQQ_profits)


with open('D:\\trading_terminal\\trading_terminal\\SQQQ_profits.txt','w') as file:
    np.savetxt(file, SQQQ_profits.reshape(1,-1), delimiter='\n', fmt='%.2f')
    
    

# 開啟A文件，讀取內容
with open('D:\\trading_terminal\\trading_terminal\\SQQQ_pre_profits.txt', 'r') as file:
    a_content = file.read()

# 開啟B文件，讀取內容
with open('D:\\trading_terminal\\trading_terminal\\SQQQ_profits.txt', 'r') as file:
    b_content = file.read()

# 將B文件的內容串接於A文件之後
a_content += b_content

# 開啟real文件，將串接後的內容寫入
with open('D:\\trading_terminal\\trading_terminal\\SQQQ_real_profits.txt', 'w') as file:
    file.write(a_content)





import numpy as np

avg_positive=0
avg_negative=0


with open('D:\TandS_profits.txt', 'r') as file:
    lines = file.readlines()
    total_positive = 0
    count_positive = 0
    for line in lines:
        numbers = line.strip().split(',') # 假設每行以逗號分隔數字
        for num in numbers:
            try:
                num = float(num)
                if num > 0:
                    total_positive += num
                    count_positive += 1
            except ValueError:
                pass # 忽略無法轉換為浮點數的內容
    if count_positive > 0:
        avg_positive = total_positive / count_positive
       
        print(f"The average of profits: {avg_positive}")
    
    else:
        print("There is no profit number in the file.")
        
        
    total_negative = 0
    count_negative = 0
    for line in lines:
        numbers = line.strip().split(',') # 假設每行以逗號分隔數字
        for num in numbers:
            try:
                num = float(num)
                if num < 0:
                    total_negative += num
                    count_negative += 1
            except ValueError:
                pass # 忽略無法轉換為浮點數的內容
    if count_negative > 0:
        avg_negative =  total_negative/ count_negative
        print(f"The average of loss : {avg_negative}")
    else:
        print("There is no loss in the file.")
        
        
        
    win_rate=count_positive/(count_negative+count_positive)
    betting_odds=abs(avg_positive*count_positive/avg_negative*count_negative)
    normal_kelly=100*((win_rate*(betting_odds+1))-1)/betting_odds
    print("betting_odds:",betting_odds)
    print("win_rate:",win_rate*100,"%")
    print("normal_kelly:",normal_kelly,"%")
    
    


    # 開啟文件，以追加模式打開文件
    with open('D:\\normal_kelly.txt', 'a') as f:
        f.write('%.2f\n' % normal_kelly)


    
        

            
        




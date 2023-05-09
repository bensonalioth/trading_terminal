import numpy as np

avg_positive=0
avg_negative=0
cal_thirty=0
avg_positive_thirty=0
avg_negative_thirty=0


S_profit = np.loadtxt('D:\\trading_terminal\\trading_terminal\\SQQQ_real_profits.txt')
neg_S_profit = S_profit[S_profit < 0]  # 选择所有负数元素
S_loss_median=np.median(neg_S_profit)
S_loss_mean = np.mean(neg_S_profit)

S_maxloss=np.min(S_profit)
S_maxearn=np.max(S_profit)

with open('D:\\trading_terminal\\trading_terminal\\S_loss_median.txt', 'a') as f:
    f.write('%.2f\n' % S_loss_median)
    
with open('D:\\trading_terminal\\trading_terminal\\S_loss_mean.txt', 'a') as f:
    f.write('%.2f\n' % S_loss_mean)


with open('D:\\trading_terminal\\trading_terminal\\S_maxloss.txt', 'a') as f:
    f.write('%.2f\n' % S_maxloss)
            
    
with open('D:\\trading_terminal\\trading_terminal\\S_maxearn.txt', 'a') as f:
    f.write('%.2f\n' % S_maxearn)





with open('D:\\trading_terminal\\trading_terminal\\SQQQ_profits.txt','r') as file:
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
        numbers = line.strip().split(',') 
        for num in numbers:
            try:
                num = float(num)
                if num < 0:
                    total_negative += num
                    count_negative += 1
            except ValueError:
                pass
    if count_negative > 0:
        avg_negative =  total_negative/ count_negative
        print(f"The average of loss : {avg_negative}")
    else:
        print("There is no loss in the file.")
        
        
        
    S_win_rate=100*count_positive/(count_negative+count_positive)
    S_betting_odds=abs((avg_positive*count_positive)/(avg_negative*count_negative))
    S_normal_kelly=100*((0.01*S_win_rate*(S_betting_odds+1))-1)/S_betting_odds
        
    print("sqqq_betting_odds:",S_betting_odds)
    print("sqqq_win_rate:",S_win_rate,"%")
    print("sqqq_normal_kelly:",S_normal_kelly,"%")
    
    with open('D:\\trading_terminal\\trading_terminal\\S_normal_kelly.txt', 'a') as f:
        f.write('%.2f\n' % S_normal_kelly)


    with open('D:\\trading_terminal\\trading_terminal\\S_win_rate.txt', 'a') as f:
        f.write('%.2f\n' % S_win_rate)
            
    
    with open('D:\\trading_terminal\\trading_terminal\\S_betting_odds.txt', 'a') as f:
        f.write('%.2f\n' % S_betting_odds)
        
        
        
        
with open('D:\\trading_terminal\\trading_terminal\\SQQQ_profits.txt','r') as file:
    lines = file.readlines()
    total_positive_thirty = 0
    count_positive_thirty = 0
    total_negative_thirty = 0
    count_negative_thirty = 0
    for line in lines:
        numbers = line.strip().split(',') # 假設每行以逗號分隔數字
        for num in numbers:
            
            cal_thirty+=1
            if(cal_thirty==30):break
            
            try:
                num = float(num)
                if num > 0:
                    total_positive_thirty += num
                    count_positive_thirty += 1
                elif num < 0:
                    total_negative_thirty += num
                    count_negative_thirty += 1
            except ValueError:
                pass # 忽略無法轉換為浮點數的內容
    if count_positive_thirty > 0:
        avg_positive_thirty = total_positive_thirty/ count_positive_thirty
       
        print(f"The thirty average of profits: {avg_positive_thirty}")
    
    else:
        print("There is no profit number in the thirty file.")
    
    if count_negative_thirty > 0:
        avg_negative_thirty =  total_negative_thirty/ count_negative_thirty
        print(f"The thirty average of loss : {avg_negative_thirty}")
    else:
        print("There is no loss in the thirty file.")
        
        

    
    S_win_rate_thirty=100*count_positive_thirty/(count_negative_thirty+count_positive_thirty)
    S_betting_odds_thirty=abs((avg_positive_thirty*count_positive_thirty)/(avg_negative_thirty*count_negative_thirty))
    S_normal_kelly_thirty=100*((0.01*S_win_rate_thirty*(S_betting_odds_thirty+1))-1)/S_betting_odds_thirty
    
    print("sqqq_betting_odds_thirty:",S_betting_odds_thirty)
    print("sqqq_win_rate_thirty:",S_win_rate_thirty,"%")
    print("sqqq_normal_kelly_thirty:",S_normal_kelly_thirty,"%")
    
    
    with open('D:\\trading_terminal\\trading_terminal\\S_normal_kelly_thirty.txt', 'a') as f:
        f.write('%.2f\n' % S_normal_kelly_thirty)


    with open('D:\\trading_terminal\\trading_terminal\\S_win_rate_thirty.txt', 'a') as f:
        f.write('%.2f\n' % S_win_rate_thirty)
            
    
    with open('D:\\trading_terminal\\trading_terminal\\S_betting_odds_thirty.txt', 'a') as f:
        f.write('%.2f\n' % S_betting_odds_thirty)
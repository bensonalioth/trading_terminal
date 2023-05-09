import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import datetime
import os
import time





# 從文件中讀取數據並轉換為numpy陣列
tqqq_win_rate = np.loadtxt('D:\\trading_terminal\\trading_terminal\\T_win_rate.txt')
tqqq_win_rate_thirty = np.loadtxt('D:\\trading_terminal\\trading_terminal\\T_win_rate_thirty.txt')
tqqq_betting_odds = np.loadtxt('D:\\trading_terminal\\trading_terminal\\T_betting_odds.txt')
tqqq_betting_odds_thirty = np.loadtxt('D:\\trading_terminal\\trading_terminal\\T_betting_odds_thirty.txt')

sqqq_win_rate = np.loadtxt('D:\\trading_terminal\\trading_terminal\\S_win_rate.txt')
sqqq_win_rate_thirty = np.loadtxt('D:\\trading_terminal\\trading_terminal\\S_win_rate_thirty.txt')
sqqq_betting_odds= np.loadtxt('D:\\trading_terminal\\trading_terminal\\S_betting_odds.txt')
sqqq_betting_odds_thirty = np.loadtxt('D:\\trading_terminal\\trading_terminal\\S_betting_odds_thirty.txt')

TandS_win_rate = np.loadtxt('D:\\trading_terminal\\trading_terminal\\TandS_win_rate.txt')
TandS_win_rate_thirty = np.loadtxt('D:\\trading_terminal\\trading_terminal\\TandS_win_rate_thirty.txt')
TandS_betting_odds= np.loadtxt('D:\\trading_terminal\\trading_terminal\\TandS_betting_odds.txt')
TandS_betting_odds_thirty = np.loadtxt('D:\\trading_terminal\\trading_terminal\\TandS_betting_odds_thirty.txt')




# 創建日期變數
today = datetime.date.today().strftime("%Y/%m/%d")



fig, (ax1, ax2, ax3,ax4,ax5,ax6) = plt.subplots(6,1, sharex=True)


ax1.plot(tqqq_win_rate, label='historical')
ax1.plot(tqqq_win_rate_thirty, label='MA30')
ax1.set_title('{}\ntqqq_winrate'.format(today))
ax2.plot(sqqq_win_rate, label='historical')
ax2.plot(sqqq_win_rate_thirty, label='MA30')
ax2.set_title('sqqq_winrate')
ax3.plot(TandS_win_rate, label='historical')
ax3.plot(TandS_win_rate_thirty, label='MA30')
ax3.set_title('TandS_winrate')
ax4.plot(tqqq_betting_odds, label='historical')
ax4.plot(tqqq_betting_odds_thirty, label='MA30')
ax4.set_title('tqqq_betting_odds')
plt.tight_layout()
ax5.plot(sqqq_betting_odds, label='historical')
ax5.plot(sqqq_betting_odds_thirty, label='MA30')
ax5.set_title('sqqq_betting_odds')
plt.tight_layout()
ax6.plot(TandS_betting_odds, label='historical')
ax6.plot(TandS_betting_odds_thirty, label='MA30')
ax6.set_title('TandS_betting_odds')
plt.tight_layout()




plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=5, hspace=0.2, wspace=0.1)


fig.set_size_inches(10, 3)


save_dir = 'charts/'
file_name = 'TandS_trading_report'

# 確保保存文件的文件夾存在
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 在文件名中添加時間戳以生成唯一的文件名
time_stamp = time.strftime('%Y%m%d_%H%M%S')
file_name = f'{file_name}_{time_stamp}'

# 調用plt.savefig()以保存文件
plt.savefig(os.path.join(save_dir, f'{file_name}.png'), dpi=300, bbox_inches='tight')







import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import base64
import datetime


# 創建日期變數
today = datetime.date.today().strftime("%Y/%m/%d")

# 創建郵件主題，並在其中添加日期變數
subject = f"交易報告 - {today}"


# 設置發送者和接收者
sender = 'a091695361@gmail.com'
recipient = 'alioth0105@gmail.com'

# 設置SMTP伺服器地址和端口號碼
smtp_server = 'smtp.gmail.com'
port = 587


# 讀最後一行

    
with open('D:\\trading_terminal\\trading_terminal\\TandS_normal_kelly.txt') as f:
    TandS_normal_kelly_last_line = f.readlines()[-1].strip()

with open('D:\\trading_terminal\\trading_terminal\\TandS_win_rate.txt') as f:
    TandS_win_rate_last_line = f.readlines()[-1].strip()
    
with open('D:\\trading_terminal\\trading_terminal\\TandS_betting_odds.txt') as f:
    TandS_betting_odds_last_line = f.readlines()[-1].strip()
    
with open('D:\\trading_terminal\\trading_terminal\\TandS_normal_kelly_thirty.txt') as f:
    TandS_normal_kelly_thirty_last_line = f.readlines()[-1].strip()

with open('D:\\trading_terminal\\trading_terminal\\TandS_win_rate_thirty.txt') as f:
    TandS_win_rate_thirty_last_line = f.readlines()[-1].strip()
    
with open('D:\\trading_terminal\\trading_terminal\\TandS_betting_odds_thirty.txt') as f:
    TandS_betting_odds_thirty_last_line = f.readlines()[-1].strip()



with open('D:\\trading_terminal\\trading_terminal\\T_win_rate.txt') as f:
    T_win_rate_last_line = f.readlines()[-1].strip()
    
with open('D:\\trading_terminal\\trading_terminal\\T_win_rate_thirty.txt') as f:
    T_win_rate_thirty_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\T_betting_odds.txt') as f:
    T_betting_odds_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\T_betting_odds_thirty.txt') as f:
    T_betting_odds_thirty_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\T_normal_kelly.txt') as f:
    T_normal_kelly_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\T_normal_kelly_thirty.txt') as f:
    T_normal_kelly_thirty_last_line = f.readlines()[-1].strip()
    
    
with open('D:\\trading_terminal\\trading_terminal\\S_win_rate.txt') as f:
    S_win_rate_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\S_win_rate_thirty.txt') as f:
    S_win_rate_thirty_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\S_betting_odds.txt') as f:
    S_betting_odds_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\S_betting_odds_thirty.txt') as f:
    S_betting_odds_thirty_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\S_normal_kelly.txt') as f:
    S_normal_kelly_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\S_normal_kelly_thirty.txt') as f:
    S_normal_kelly_thirty_last_line = f.readlines()[-1].strip()
    
    
with open('D:\\trading_terminal\\trading_terminal\\TandS_loss_median.txt') as f:
    TandS_loss_median_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\TandS_loss_mean.txt') as f:
    TandS_loss_mean_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\TandS_maxloss.txt') as f:
    TandS_maxloss_last_line = f.readlines()[-1].strip()
#with open('D:\\trading_terminal\\trading_terminal\\TandS_maxearn.txt') as f:
    #TandS_maxearn_last_line = f.readlines()[-1].strip()

with open('D:\\trading_terminal\\trading_terminal\\T_loss_median.txt') as f:
    T_loss_median_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\T_loss_mean.txt') as f:
    T_loss_mean_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\T_maxloss.txt') as f:
    T_maxloss_last_line = f.readlines()[-1].strip()
#with open('D:\\trading_terminal\\trading_terminal\\T_maxearn.txt') as f:
    #T_maxearn_last_line = f.readlines()[-1].strip()
    
with open('D:\\trading_terminal\\trading_terminal\\S_loss_median.txt') as f:
    S_loss_median_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\S_loss_mean.txt') as f:
    S_loss_mean_last_line = f.readlines()[-1].strip()
with open('D:\\trading_terminal\\trading_terminal\\S_maxloss.txt') as f:
    S_maxloss_last_line = f.readlines()[-1].strip()
#with open('D:\\trading_terminal\\trading_terminal\\S_maxearn.txt') as f:
    #S_maxearn_last_line = f.readlines()[-1].strip()
    
    
    





msg = MIMEMultipart()

body = '整體策略:\n歷史勝率：{}%      近30筆勝率：{}%\n歷史賺賠比：{}      近30筆賺賠比：{}\n歷史凱利：{}%      近30筆凱利：{}%\n\n做多策略:\n歷史勝率：{}%      近30筆勝率：{}%\n歷史賺賠比：{}    近30筆賺賠比：{}\n歷史凱利：{}%      近30筆凱利：{}%\n\n做空策略:\n歷史勝率：{}%      近30筆勝率：{}%\n歷史賺賠比：{}    近30筆賺賠比：{}\n歷史凱利：{}%      近30筆凱利：{}%\n\n歷史虧損報告:\n整體:最大:{}平均:{}中位:{}\n做多:最大:{}平均:{}中位:{}\n做空:最大:{}平均:{}中位:{}\n'.format(TandS_win_rate_last_line
                                                                                                                                  ,TandS_win_rate_thirty_last_line
                                                                                                                                  ,TandS_betting_odds_last_line
                                                                                                                                  ,TandS_betting_odds_thirty_last_line
                                                                                                                                  ,TandS_normal_kelly_last_line
                                                                                                                                  ,TandS_normal_kelly_thirty_last_line
                                                                                                                                  ,T_win_rate_last_line
                                                                                                                                  ,T_win_rate_thirty_last_line
                                                                                                                                  ,T_betting_odds_last_line
                                                                                                                                  ,T_betting_odds_thirty_last_line
                                                                                                                                  ,T_normal_kelly_last_line
                                                                                                                                  ,T_normal_kelly_thirty_last_line
                                                                                                                                  ,S_win_rate_last_line
                                                                                                                                  ,S_win_rate_thirty_last_line
                                                                                                                                  ,S_betting_odds_last_line
                                                                                                                                  ,S_betting_odds_thirty_last_line
                                                                                                                                  ,S_normal_kelly_last_line
                                                                                                                                  ,S_normal_kelly_thirty_last_line
                                                                                                                                  ,TandS_maxloss_last_line
                                                                                                                                  ,TandS_loss_mean_last_line
                                                                                                                                  ,TandS_loss_median_last_line
                                                                                                                                  ,T_maxloss_last_line
                                                                                                                                  ,T_loss_mean_last_line
                                                                                                                                  ,T_loss_median_last_line
                                                                                                                                  ,S_maxloss_last_line
                                                                                                                                  ,S_loss_mean_last_line
                                                                                                                                  ,S_loss_median_last_line)




msg.attach(MIMEText(body))

# 指定目標文件夾路徑和文件類型
folder_path = 'D:\\trading_terminal\\trading_terminal\\charts'
file_type = '.png'

# 列出目標文件夾中所有文件的名稱列表
file_names = os.listdir(folder_path)

# 創建一個字典，存儲每個文件的名稱和最後修改時間
file_dict = {}
for file_name in file_names:
    if file_name.endswith(file_type):
        file_path = os.path.join(folder_path, file_name)
        file_dict[file_name] = os.path.getmtime(file_path)

# 按照最後修改時間排序，取得最晚的文件名
latest_file_name = sorted(file_dict, key=file_dict.get)[-1]

# 打開這個文件，讀取其中的圖片數據
with open(os.path.join(folder_path, latest_file_name), 'rb') as f:
    img_data = f.read()

# 創建MIMEImage對象，並添加Content-Disposition頭部
image = MIMEImage(img_data)
image.add_header('Content-Disposition', 'attachment', filename=latest_file_name)

# 添加附件
msg.attach(image)

# 設置郵件標題、收件人和寄件人
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient





# 連接SMTP伺服器並啟用TLS加密
server = smtplib.SMTP(smtp_server, port)
server.starttls()

# 登錄到Gmail帳戶
email = 'a0916295361@gmail.com'
password = 'ldzazxxnxxvsxgvb'
server.login(email, password)


# 傳送郵件
try:
    server.sendmail(sender, recipient, msg.as_string())
    print('Email sent successfully!')
except Exception as e:
    print(f'Sending email failed due to {e}')

# 關閉SMTP連接
server.quit()









import smtplib
import os
from email.mime.text import MIMEText
import base64

# 設置電子郵件發送者和接收者
sender = 'a091695361@gmail.com'
recipient = 'alioth0105@gmail.com'

# 設置SMTP伺服器地址和端口號碼
smtp_server = 'smtp.gmail.com'
port = 587

# 讀取最後一行
file_path = 'D:\\normal_kelly.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()
    last_line = lines[-1]

# 構建電子郵件訊息
body = '一倍凱利：{}%。'.format(last_line.strip())
message = MIMEText(body)
message['to'] = recipient
message['subject'] = '交易報告'

# 將訊息轉換成原始格式
raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

# 連接SMTP伺服器並啟用TLS加密
server = smtplib.SMTP(smtp_server, port)
server.starttls()

# 登錄到Gmail帳戶
email = 'a0916295361@gmail.com'
password = 'ldzazxxnxxvsxgvb'
server.login(email, password)

# 發送電子郵件
try:
    server.sendmail(sender, recipient,message.as_string())
    print('Email sent successfully!')
except Exception as e:
    print(f'Sending email failed due to {e}')

# 關閉連接
server.quit()

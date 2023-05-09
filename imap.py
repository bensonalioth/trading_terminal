import imaplib
import email
import os


mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('a0916295361@gmail.com', 'your_app_password')



mail.select("inbox")

# 搜尋條件
search_criteria = 'UNSEEN OR SUBJECT "BOUGHT" SUBJECT "SOLD"'

# 搜尋符合條件的郵件
result, data = mail.search(None, search_criteria)

# 檢查郵件主題
for num in data[0].split():
    typ, msg_data = mail.fetch(num, '(RFC822)')
    email_message = email.message_from_bytes(msg_data[0][1])
    subject = email_message['subject']
 
    if len(subject) < 43:
        
        with open(os.path.join(r'D:\\trading_terminal\\trade_big_data', 'email_subjects.txt'), 'a') as f:
            f.write(subject + '\n')
        print(subject)
mail.logout()


def extract_TQQQ_subjects(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f_input, \
         open(output_file_path, 'w') as f_output:
        
        for line in f_input:
            if 'TQQQ' in line:
                f_output.write(line)
                
input_file_path =r'D:\trading_terminal\trade_big_data\email_subjects.txt'
output_file_path =r'D:\trading_terminal\trade_big_data\TQQQ_subjects.txt'
extract_TQQQ_subjects(input_file_path, output_file_path)

def extract_SQQQ_subjects(input_file_path, output_file_path):
    with open(input_file_path, 'r') as f_input, \
         open(output_file_path, 'w') as f_output:
        
        for line in f_input:
            if 'SQQQ' in line:
                f_output.write(line)
                
input_file_path =r'D:\\trading_terminal\\trade_big_data\\email_subjects.txt'
output_file_path =r'D:\\trading_terminal\\trade_big_data\\SQQQ_subjects.txt'
extract_SQQQ_subjects(input_file_path, output_file_path)




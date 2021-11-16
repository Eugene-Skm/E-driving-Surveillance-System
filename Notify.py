# -*- coding: utf-8 -*-
"""
Spyder Editor
2021-5-12 Yujin-Sakuma reitaku-University
"""
import requests
from bs4 import BeautifulSoup
import winsound
import smtplib, ssl
from email.mime.text import MIMEText
import sys
winsound.Beep(1000, 200)

def send_line_notify(notification_message):#LINEに通知する
    line_notify_token = '********************'#ラインで生成されるトークン
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f' {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)
            
# メールアドレスとパスワードの指定
USER = "1****4"
PASS = "1****2"
STNO="1****4"
PCD=""
KCD=""
SCLCD="***********"
INDEX=""
SERVER="qar004"
METHOD="ログイン"

# セッションを開始
session = requests.session()
# ログイン情報設定　Developperツールより
login_info = {
    "b.studentId":USER,
    "b.password":PASS,
    "b.wordsStudentNo":STNO,
    "b.processCd":PCD,
    "b.kamokuCd":KCD,
    "b.schoolCd":SCLCD,
    "index" :INDEX,
    "server":SERVER,
    "method:doLogin":METHOD
}
# action
url_login = "https://www.e-license.jp/el25/pc/********"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

#BeautifulSoup化
soup = BeautifulSoup(res.text,"html.parser")
center_soup=soup.find('td',class_='center')

status0=center_soup.find_all('td',class_='status0')#空き無し
status1=center_soup.find_all('td',class_='status1')#予約可能
status3=center_soup.find_all('td',class_='status3')#予約済み
status4=center_soup.find_all('td',class_='status4')#乗車済み
status7=center_soup.find_all('td',class_='status7')#現在時限
status8=center_soup.find_all('td',class_='status8')#当日終了時限
status9=center_soup.find_all('td',class_='status9')#予約不可
sumt=len(status0)+len(status1)+len(status3)+len(status4)+len(status7)+len(status8)+len(status9)

if len(status1)>0:
    send_line_notify('予約可能枠'+str(len(status1))+'\r\n https://www.e-license.jp/el25/?***********************');
    #winsound.Beep(6000, 1000)
    # 以下にGmailの設定を書き込む
    gmail_account = "y*******3@gmail.com"
    gmail_password = "*****************"
    # メールの送信先
    mail_to = "a*****y@r*****u.jp"
    
    # メールデータ(MIME)の作成 ---
    subject = "教習所予約状況：予約可能枠あり"
    body = "予約可能枠:"+str(len(status1))+"\r\n https://www.e-license.jp/el25/?***********************"
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = gmail_account
    
    # Gmailに接続 --- 
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
        context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg) # メールの送信
    #print("ok.")
sys.exit()



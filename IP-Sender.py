import urllib2,smtplib,socket,time,os,platform
from email.mime.text import MIMEText
receiver_address=''
sender_address = ''
sender_password=''
SMTP_server =''



Internet='http://info.tsinghua.edu.cn'

def get_net_status():
    try:
        urllib2.urlopen(Internet)
        return True
    except Exception ,e:
        return False

def get_ip():
    if platform.system()=='Linux':
         os.system('sudo systemctl restart dhcpd@eth0.service')
    return socket.gethostbyname(socket.gethostname())
    socket.get

def send_mail(content):
    session = smtplib.SMTP(SMTP_server, port = 25)
    session.set_debuglevel(True)
    session.login(sender_address, sender_password)
    msg = MIMEText(content)
    msg['Subject'] = 'Paspberry Pi IP Address'
    msg['From'] = sender_address
    msg['To'] = receiver_address
    session.sendmail(sender_address, receiver_address, msg.as_string())
    session.quit()

if __name__ == '__main__':
    while(True):
        if get_net_status:
            send_mail( get_ip())
            break
        else:
            time.sleep(600)



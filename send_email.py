# --*-- coding:utf-8 --*--
import threading

from flask import Flask, render_template
from flask_mail import Mail,Message
app=Flask(__name__)
#配置发邮件设置
app.config['MAIL_SERVER']='smtp.qq.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='954182252@qq.com'
app.config['MAIL_PASSWORD']=''
app.config['MAIL_USE_SSL']=True
app.config['MAIL_DEFAULT_SENDER'] = 'ChenGuangHai<954182252@qq.com>'
# 创建邮件连接对象
conn = Mail(app)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

def async_send_mail(mesg):
    with app.app_context():
        conn.send(mesg)

@app.route('/send_eamil')
def send_email():
    """
        :param subject: Email subject
        :param body: Email body
        :param from_email: Email address of sender
        :param to: Email addresses of receivers
        :type to: list
        :param bcc: Blind carbon copy
        :param connection: Instance of :class:`Mail`
        :param attachments: Attachments to the email
        :param headers: Headers for the email message
        :param cc: Carbon copy email addresses
    """
    mesg = Message(subject=u'陈光海的发送邮件测试案例。！',
                   recipients=[u'1746665264@qq.com'],
                   html=u'<h1>测试发送邮件成功。。。！</h1>')
    trd = threading.Thread(target=async_send_mail, args=(mesg,))
    trd.start()
    return u'发送中....'

if __name__ == '__main__':

    app.run(debug=True)

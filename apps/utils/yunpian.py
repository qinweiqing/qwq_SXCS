import requests
import json

class YunPian(object):
    def __init__(self,api_key):
        self.api_key=api_key
        self.single_send_url='https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self,code,mobile):
        # 需要传递的参数
        parmas={
            'apikey':self.api_key,
            'mobile':mobile,
            "text": "【宋东波】您的验证码是{code}".format(code=code)
        }
        response=requests.post(self.single_send_url,data=parmas)
        re_dict=json.loads(response.text)
        return re_dict




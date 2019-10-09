from random import randrange

import requests
from django.core.cache import cache

from common import keys
from tool import config


def gen_vcode(length=4):
    '''生成一个验证码'''
    start = 10 ** (length - 1)
    end = 10 ** length
    return str(randrange(start, end))


def send_sms(phonenum):
    '''发送手机验证码'''
    # 从config.py 配置中复制短信参数 dict
    params = config.YZX_SMS_PARAMS.copy()

    # 赋值手机号
    params['mobile'] = phonenum

    # 创建验证码，并添加到缓存
    vcode = gen_vcode()

    # 赋值验证码和过期时间
    params['param'] = vcode + ", 180"
    print('----------->', vcode)
    cache.set(keys.VCODE_KEY % phonenum, vcode, 180)
    # 向短信接口提交发短信请求
    resp = requests.post(config.YZX_SMS_API, json=params)
    print(resp.json())
    # 根据结果返回成功失败
    if resp.status_code == 200:
        result = resp.json()
        if result['code'] == '000000':
            return True, result['msg']
        else:
            return False, result['msg']
    else:
        return False, '短信服务器错误'
if __name__=="__main__":
    send_sms(15210603679)
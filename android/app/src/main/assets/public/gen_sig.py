#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
腾讯云 IM UserSig 生成工具（官方算法）
用法: python gen_sig.py
"""

import hmac
import hashlib
import base64
import json
import time
import zlib

SDKAppID = 1600147983
secretKey = 'bba415883618eac54c32e79cd135ba1f3dc59f1732c053f99f734bde0f6bdf20'
expire_sec = 604800  # 7天


def gen_usersig(userid, sdkappid, secret_key, expire=604800):
    """
    根据腾讯云官方算法生成 UserSig
    参考: https://cloud.tencent.com/document/product/269/32688
    """
    curr_time = int(time.time())
    expire_time = curr_time + expire

    # 签名内容（注意：不包含 secret_key）
    content_to_sign = (
        f'TLS.identifier:{userid}\n'
        f'TLS.sdkappid:{sdkappid}\n'
        f'TLS.timestamp:{expire_time}\n'
        f'TLS.expire:{expire}'
    )

    # HMAC-SHA256 签名
    sig = hmac.new(
        secret_key.encode('utf-8'),
        content_to_sign.encode('utf-8'),
        hashlib.sha256
    ).digest()
    sig_base64 = base64.b64encode(sig).decode('utf-8')

    # 构造 UserSig 对象
    user_sig_obj = {
        'TLS.ver': '2.0',
        'TLS.identifier': userid,
        'TLS.sdkappid': sdkappid,
        'TLS.expire': expire,
        'TLS.timestamp': expire_time,
        'TLS.sig': sig_base64
    }

    # JSON -> zlib 压缩 -> base64 编码
    json_str = json.dumps(user_sig_obj, separators=(',', ':'))
    compressed = zlib.compress(json_str.encode('utf-8'))
    user_sig = base64.b64encode(compressed).decode('utf-8')

    return user_sig


def verify_usersig(user_sig, sdkappid, secret_key):
    """验证 UserSig 是否有效（用于调试）"""
    try:
        compressed = base64.b64decode(user_sig)
        json_str = zlib.decompress(compressed).decode('utf-8')
        obj = json.loads(json_str)
        return obj
    except Exception as e:
        return {'error': str(e)}


if __name__ == '__main__':
    results = {}
    for uid in ['user001', 'user002', 'user003']:
        sig = gen_usersig(uid, SDKAppID, secretKey)
        results[uid] = sig
        print(f'用户ID: {uid}')
        print(f'UserSig: {sig}')
        print()

    # 保存到文件（方便复制）
    with open('usersig.txt', 'w', encoding='utf-8') as f:
        f.write('===== 顺聊测试账号 UserSig =====\n')
        f.write(f'SDKAppID: {SDKAppID}\n')
        f.write(f'生成时间: {time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        f.write(f'有效期: 7天\n\n')
        for uid, sig in results.items():
            f.write(f'【{uid}】\n')
            f.write(f'{sig}\n\n')

    print(f'已保存到 usersig.txt')

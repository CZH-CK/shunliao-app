#!/usr/bin/env python3
"""生成 Android 签名用的 PKCS12 keystore"""

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.serialization import pkcs12
import datetime
import os

# 密钥库配置
KEYSTORE_PATH = "shunliao-release-key.p12"
KEYSTORE_PASSWORD = "shunliao2024"
KEY_ALIAS = "shunliao"

print("正在生成 RSA 密钥...")
# 生成私钥
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

print("正在生成自签名证书...")
# 生成自签名证书
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "CN"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Guangdong"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Shenzhen"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "ShunLiao"),
    x509.NameAttribute(NameOID.COMMON_NAME, "ShunLiao App"),
])
cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) - datetime.timedelta(days=1)
).not_valid_after(
    datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(days=365*25)
).sign(private_key, hashes.SHA256())

print(f"正在保存 keystore 到 {KEYSTORE_PATH}...")
# 保存为 PKCS12 格式
p12_data = pkcs12.serialize_key_and_certificates(
    name=KEY_ALIAS.encode(),
    key=private_key,
    cert=cert,
    cas=None,
    encryption_algorithm=serialization.BestAvailableEncryption(KEYSTORE_PASSWORD.encode())
)
with open(KEYSTORE_PATH, "wb") as f:
    f.write(p12_data)

print(f"✅ Keystore 生成成功！")
print(f"   路径: {os.path.abspath(KEYSTORE_PATH)}")
print(f"   密码: {KEYSTORE_PASSWORD}")
print(f"   别名: {KEY_ALIAS}")
print(f"   有效期: 25年")
print(f"\n⚠️  请妥善保管此文件，丢失后无法更新已上架的应用！")

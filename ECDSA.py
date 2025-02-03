from ecdsa import SECP256k1, SigningKey, VerifyingKey
import hashlib

# 读取消息和随机数
with open('secret.txt', 'r') as f:
    lines = f.readlines()
    message = lines[0].strip().encode()  # 消息是第一行
    k = int(lines[1].strip())  # 随机数（k）是第二行

# 生成私钥（可以从文件中提供或者使用随机生成）
sk = SigningKey.generate(curve=SECP256k1)

# 使用提供的k进行签名
sig = sk.sign(message, k=k)

# 获取公钥
vk = sk.verifying_key

# 将私钥、公钥、签名结果保存到文件
with open('out.txt', 'w') as out_file:
    out_file.write(f"Private Key: {sk.to_string().hex()}\n")
    out_file.write(f"Public Key: {vk.to_string().hex()}\n")
    out_file.write(f"Signature: {sig.hex()}\n")

print("签名完成，并已将公钥和私钥保存到 out.txt 文件中")

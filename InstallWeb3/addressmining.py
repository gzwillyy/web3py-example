# _*_ encoding=utf-8 _*_
import os
import json
from concurrent.futures import ProcessPoolExecutor

try:
    from web3 import Web3
except ImportError:
    os.system("pip3 install web3")
# from pprint import pprint as dump


pp = ProcessPoolExecutor(4)


def todo(item):
    w3 = Web3()
    arr = [
        "00000000",
        "000000000",
        "11111111",
        "111111111",
        "22222222",
        "222222222",
        "33333333",
        "333333333",
        "55555555",
        "555555555",
        "66666666",
        "666666666",
        "88888888",
        "888888888",
        "99999999",
        "999999999",
        "aaaaaaaa",
        "aaaaaaaaa",
        "bbbbbbbb",
        "bbbbbbbbb",
        "cccccccc",
        "ccccccccc",
        "dddddddd",
        "ddddddddd",
        "eeeeeeee",
        "eeeeeeeee",
        "ffffffff",
        "fffffffff",
        "19951028",
    ]
    while True:
        acct = w3.eth.account.create("19951028")
        a = [acct.address.endswith(item) for item in arr]
        print(acct.address)
        if any(a) or acct.address.startswith("0x19951028"):
            content = {
                'address': acct.address,
                'key': acct.key.hex(),
            }
            # dump(content)
            json_adr = 'info'+str(item)+'.json'
            with open(json_adr, 'a') as fb:
                json.dump(content, fb, indent=4)


futures = []

for item in range(4):
    future = pp.submit(todo,item)
    futures.append(future)

for future in futures:
    print(future.result())

# public address: 0xabc63486f9...
# private key: 0xb3138d6b67...

# 发布或使用虚荣心地址工具非常简单，但出于安全原因，我不鼓励它；对于一个坏人来说，将任何成功挖掘的密钥发送到私有服务器也是直截了当的。你自己写剧本就行了。
# 我们使用的create函数接受输入作为额外的熵，即额外的随机性，使您的帐户更难重现。在那里添加一些独特的输入，并将其视为密码。例如：w3.eth.account.create("4%das$adA1r28hlnk")。
# 以太坊地址是十六进制数字，这意味着它们包括字母a到f和数字0到9。不要为了g而去采矿。
# 请注意，您想要挖掘的角色越多，需要的时间就越长——数量级！超过几个字符，您可能需要等待几天才能随机生成该序列。



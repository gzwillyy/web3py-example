# _*_ encoding=utf-8 _*_
import os
import json
from concurrent.futures import ProcessPoolExecutor

try:
    from web3 import Web3
except ImportError:
    os.system("pip3 install web3")
# from pprint import pprint as dump


pp = ProcessPoolExecutor(2)


def todo(item):
    w3 = Web3()
    arr = [
        "1",
        "000",
        "000000000",
        "111111111",
        "222222222",
        "333333333",
        "555555555",
        "666666666",
        "888888888",
        "999999999",
        "aaaaaaaaa",
        "bbbbbbbbb",
        "ccccccccc",
        "ddddddddd",
        "eeeeeeeee",
        "fffffffff",
        "19951028",
    ]
    while True:
        acct = w3.eth.account.create()
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

for item in range(2):
    future = pp.submit(todo,item)
    futures.append(future)

for future in futures:
    print(future.result())

# public address: 0xabc63486f9...
# private key: 0xb3138d6b67...

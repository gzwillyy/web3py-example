# _*_ encoding=utf-8 _*_

import os

# 安装IPython 供了选项卡完成，使您可以更轻松地查看Web3.py中可能的内容
# pip3 install ipython
# ipython
# from web3 import Web3

try:
    from web3 import Web3
except ImportError:
    os.system("pip3 install web3")
    # 模拟节点
    os.system('pip3 install "web3[tester]"')
    os.system('pip3 install eth-tester')

try:
    from pprint import pprint as dump
except ImportError:
    os.system("pip3 install PrettyPrinter")

wei = Web3.toWei(1, "ether")
dump(" 1 eth = {} wei".format(wei))

wei = Web3.fromWei(500000000, 'gwei')
dump(" 500000000 gwei = {} wei".format(wei))


# 这些概念有的必须在IPython shell中演示
# 模拟节点
w3 = Web3(Web3.EthereumTesterProvider())

# 检查
is_con = w3.isConnected()
dump("检查连接 : {}".format(is_con))

# 帐户的列表
accounts = w3.eth.accounts
dump("账户列表 : {} ".format(w3.eth.accounts))

# 账户余额
accounts_0_balance = w3.eth.get_balance(accounts[0])
dump("账户余额(wei) : {}".format(accounts_0_balance))

# 转换成eth
accounts_0_eth_balance = w3.fromWei(accounts_0_balance, 'ether')
dump("账户余额(eth) : {}".format(accounts_0_eth_balance))
w3.eth.get_balance(w3.eth.accounts[0])

# 最新块的所有信息
latest_block_info = w3.eth.get_block("latest")
dump(latest_block_info)

# 交易参数举例
tx_param_example = {
    "chainId": 1,
    # HexStr
    "data": "",
    # str 发送方 地址或ens
    "from": "",
    # int 可以消耗的 Gas 的最大数量
    "gas": 0,
    # int
    "gasPrice": 0,
    # int 愿意为交易支付的最大 gas 数量（包括 baseFeePerGas 和 maxPriorityFeePerGas）
    "maxFeePerGas": 0,
    # int 作为矿工小费包含的最大 gas 数量
    "maxPriorityFeePerGas": 0,
    # int 随机数
    "nonce": 12,
    # str 接收方 地址或ens
    "to": "",
    # 交易类型
    "type": "",
    # 交易数量
    "value": 0,
}


tx_param = {
   'from': w3.eth.accounts[0],
   'to': w3.eth.accounts[1],
   'value': w3.toWei(3, 'ether')
}

# 以太从一个帐户发送到另一个帐户
tx_hash = w3.eth.send_transaction(tx_param)


# 这通常是您等待几秒钟才能将交易挖掘到新块的点。整个过程是这样的：
# 提交交易并保留交易哈希。在开采之前，交易是“待定的”。
# tx_hash = w3.eth.send_transaction({ … })
# 等待交易被挖掘：
# w3.eth.wait_for_transaction_receipt(tx_hash)
# 继续应用逻辑。要查看成功的交易：
# w3.eth.get_transaction(tx_hash)

# 查看交易事务
w3.eth.get_transaction(tx_hash)

# AttributeDict({'type': '0x2',
#  'hash': HexBytes('0x9e473ea541a2df4b180a45585a7751e48a753f7ba6e5d46f35d59bff6046b4bb'),
#  'nonce': 0,
#  'blockHash': HexBytes('0x7fc813d198bc931d2ddd2359b2d121f4009fe020b014daabe1bce8f67762cf5d'),
#  'blockNumber': 1,
#  'transactionIndex': 0,
#  'from': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
#  'to': '0x2B5AD5c4795c026514f8317c7a215E218DcCD6cF',
#  'value': 3000000000000000000,
#  'gas': 121000,
#  'data': '0x',
#  'r': HexBytes('0x6ee7b2551baa2de937502e2286a6dca35164b5e9a4a7d4a6fff4c616e5f3e671'),
#  's': HexBytes('0x441615d3bde4467c387fd45455909fa243c4881d17c9fa83ccd2dc0e7eb5bb1d'),
#  'v': 0,
#  'chain_id': 131277322940537,
#  'maxFeePerGas': 1000000000,
#  'maxPriorityFeePerGas': 1000000000,
#  'accessList': [],
#  'gasPrice': 1000000000})

# 详细信息：from、to和value字段应与我们send_transaction调用的输入匹配。
# 另一个令人放心的是，此事务被包含在1号块中作为第一个事务（“'transactionIndex': 0）

# 还可以通过检查两个相关帐户的余额来轻松验证这笔交易的成功
w3.eth.get_balance(w3.eth.accounts[0])
w3.eth.get_balance(w3.eth.accounts[1])



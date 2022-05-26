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


# 这些概念有的必须在IPython shell中演示

# 部署智能合约
# 与智能合同互动看起来与标准交易非常相似。
# 智能合同是生活在以太坊区块链上的程序，任何人都可以使用。
# 当您准备部署智能合约时，您将代码编译为字节码，并将其作为data值包含在事务中：

# bytecode = "6080604052348015610...36f6c63430006010033"
# tx = {
#    'data': bytecode,
#    'value': 0,
#    'nonce': 0,
#    ...
# }

# 除了需要更多的手续费外，合同部署交易中唯一的其他区别是没有to字段。
# 该过程的其余部分与eth的交易转移相同。

# 签名消息
#
# 交易是影响区块链状态的唯一方式，但它们不是使用帐户的唯一方式。
# 简单地证明特定帐户的所有权本身就有用。
# 例如，以太坊市场OpenSea将允许您通过在帐户上签名消息来竞标待售商品。
# 只有当拍卖到期或卖方接受您的报价时，才会进行实际交易。
# 同样，该应用程序在向您显示一些帐户详细信息之前，会使用签名消息作为身份验证形式。
# 与交易不同，签名消息无需任何费用。
# 它们不会广播到网络，也不包含在块中。
# 消息只是用私钥签名的一点数据。
# 正如您所料，发件人的私钥仍然隐藏，但接收方可以从数学上证明发件人的公共地址。
# 换句话说，消息发送者不能被欺骗。
# 注意：“链上”和“链外”这两个术语是数据是否存在于以太坊区块链上的缩写。
# 例如，帐户余额和智能合同状态在链上管理，但消息签名发生在链外。

# 之后会对消息签名深入研究，但这里有一些伪代码可以让您了解工作流程：
# 1. write a message
# msg = "amanaplanacanalpanama"

# 2. sign it with an account's private key
# pk = b"..."
# signed_message = sign_message(message=msg, private_key=pk)

# 3. send `signed_message` over the wire

# 4. message receiver decodes sender's public address
# sender = decode_message_sender(msg, signed_message.signature)
# print(sender)
# '0x5ce9454...b9aB12E'



# web3账户含义
# 轻松创建以太坊帐户：离线并与任何应用程序分开
# 这些帐户可用于签署消息或发送各种类型的交易


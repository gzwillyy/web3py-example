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

# 帐户生成 不需要提供程序
w3 = Web3()
acct = w3.eth.account.create()
dump(acct.address)

# private key
dump(acct.key)

# 没有注册流程，也没有往返区块链或任何服务器。
# 事实上，您可以完全断开与互联网的连接，仍然可以创建一个有效的以太坊帐户
# 在上面的代码中，您将找到帐户的两个组件：公共地址和私钥。
# 简而言之，私钥是帐户的密码。
# 公共地址是从私钥派生的可共享帐号。
# 如代码示例所示，两者都通常表示为十六进制数字。


# 使用帐户

# 影响区块链更改的唯一方法是通过交易，每笔交易都必须由帐户签名
# 帐户可以启动以太传输、部署智能合同或与合同交互的交易，以完成铸造新令牌等操作。
w3 = Web3(Web3.EthereumTesterProvider())
accounts = w3.eth.accounts
acct_one = w3.eth.accounts[0]
acct_one_balance = w3.eth.get_balance(acct_one)

# 创建新账户
acct_two = w3.eth.account.create()
dump(acct_two.address)

# private key
dump(acct_two.key)

# 发送交易
# 此事务将立即执行，但一些重要细节将隐藏在视图中。
# Web3.py足够聪明，知道EthereumTesterProvider正在管理acct_one，我们正在使用测试环境
# 为了方便起见，acct_one是“解锁的”，这意味着默认情况下，帐户中的交易被批准（签名）
tx_hash_1 = w3.eth.send_transaction({
    'from': acct_one,
    'to': acct_two.address,
    'value': Web3.toWei(1, 'ether')
})

# 如果不是来自解锁帐户的交易，会是什么样子？
# 要了解情况，让我们从acct_two发送一些以太，acct_two是一个不由EthereumTesterProvider管理的帐户。
# 这个更手动的过程有三个步骤：
# 1）指定交易详细信息，
# 2）签署交易，然后
# 3）将交易广播到网络

# 1) 手动生成事务
tx = {
    'to': acct_one,
    'value': 10000000,
    'gas': 21000,
    'gasPrice': w3.eth.get_block('pending')['baseFeePerGas'],
    'nonce': 0
}

# 2) 使用发件人的私钥签署交易
signed = w3.eth.account.sign_transaction(tx, acct_two.key)

# 3) 发送“原始”事务
tx_hash_2 = w3.eth.send_raw_transaction(signed.rawTransaction)
# HexBytes('0x48e3a8de38831d4f5a5be95d40557b08e757073d586a67e86d96bb425e134ce9')

# 第1步定义了一个带有所需事务字段的Python字典。
# 我们在第一部分了解了gas和gasPrice。
# 在以太坊中，nonce只是帐户的交易计数 ,以太坊协议跟踪此值，以防止重复支出
# 由于这是acct_two进行的第一笔交易，其nonce为零。
# 如果您提供了错误的值，结果是无效的事务，并被Web3.py拒绝： ValidationError: Invalid transaction nonce: Expected 0, but got 4
# 请注意，从acct_one发送交易时仍然需要nonce，但EthereumTesterProvider会跟踪托管帐户的交易计数，并将适当的nonce添加到新事务中。
# 您可能已经注意到的另一个细节是，from tx的值缺失。
# 在这种情况下，sign_transaction方法可以从发件人的私钥中推断出发件人的地址。
# 同样，公共地址可以从私钥派生，但私钥不能从其公共地址反向工程。
# 最后，“原始”事务只是以字节表示的事务数据和签名。在引擎盖下，send_transaction执行sendsend_raw_transaction所需的相同编码。


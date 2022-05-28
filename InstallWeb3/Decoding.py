# _*_ encoding-utf-8 _*_

from web3 import Web3, HTTPProvider

from web3.exceptions import (
    TimeExhausted,
    TransactionNotFound,
)

# 有一小部分用例，您可能需要解码尚未包含在块中的已签名事务。
# 例如，MEV协议与主事务池分开的已签名事务包一起工作。
# 如果这一系列词对你来说毫无意义，那么你很有可能不需要这篇博客文章的内容，而是对获取挖掘的交易数据感兴趣。
# 所以，让我们从那里开始。

# 获取挖掘交易
# 如果您有兴趣从以太坊区块链获取交易数据，则存在一个简单的API。
# 请注意，这些交易已广播到网络，并且已经成功挖掘到块中。

w3 = Web3(HTTPProvider('https://eth-mainnet.public.blastapi.io'))
tx_hash = "0xf5747509ae0df156636a297f74eed12a0577432dd54854dc334ac943a939d4b2"
try:
    trans_dict = w3.eth.get_transaction(tx_hash)
except TransactionNotFound:
    print("transaction not found : {}".format(tx_hash))

print(trans_dict)




# 解码已签名的交易
# 在撰写本文时，Web3.py中不存在用于解码未排雷签名事务的专用API，但该功能可以从py-evm和eth-utils库中找到的实用程序构建。
# https://github.com/ethereum/py-evm/    https://github.com/ethereum/eth-utils/
# py-evm 不能使用root用户安装 pip3 install py-evm
# 解码事务的逻辑现在需要考虑“类型交易”，这些交易是在柏林网络升级中引入以太坊的
# 升级后，传统事务继续受到支持，但键入的事务对事务哈希的第一个字节具有专用值范围
# 例如，EIP-1559事务的事务类型为0x02，其次是rlp编码的事务主体：0x02 || rlp([chain_id, nonce, amount, data, ...])

# 根据定义，每个类型事务都有一个唯一的数据有效负载，必须编码和解码。
# 这些映射统称为sedes，是序列化/反序列化的缩写。
# 幸运的是，py-evm将这些实现详细信息隐藏在TransactionBuilder类中

# 把它们放在一起——下面的代码将事务哈希转换为字节，然后使用py-evm的最新TransactionBuilder解码有效负载。


from eth.vm.forks.arrow_glacier.transactions import ArrowGlacierTransactionBuilder as TransactionBuilder
from eth_utils import (
  encode_hex,
  to_bytes,
)

# 1) 要解码的签名交易:
original_hexstr = '0x02f86b010...'

# 2) 将十六进制字符串转换为字节:
signed_tx_as_bytes = to_bytes(hexstr=original_hexstr)

# 3) 使用最新的事务构建器反序列化事务:
decoded_tx = TransactionBuilder().decode(signed_tx_as_bytes)
print(decoded_tx.__dict__)
# {'type_id': 2, '_inner': DynamicFeeTransaction(chain_id=1, nonce=4, max_priority_fee_per_gas=2500000000, max_fee_per_gas=118977454018, gas=45000, to=b'\xe9\xcb\...', value=0, data=b'', access_list=(), y_parity=1, r=23532..., s=28205...)}

# 4) the (human-readable) sender's address:
sender = encode_hex(decoded_tx.sender)
print(sender)
# 0xe9cb1f...







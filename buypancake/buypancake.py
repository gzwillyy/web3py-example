# _*_ encoding=utf-8 _*_
import json
import config
import time
import os
import console as con

try:
    from web3 import Web3
    from web3.exceptions import ValidationError
except ImportError:
    os.system("pip3 install web3")

# 加载命令行输出
console = con.Console()

# 节点信息配置
bsc_node = "http://18.167.191.229/eth"
# 连接rpc
web3 = Web3(Web3.HTTPProvider(bsc_node))

# 节点是否连接
is_connerct = web3.isConnected()
console.log_connerct(is_connerct)

# pancake router , abi
pan_router_contract_address = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
console.log_address("薄饼 router", pan_router_contract_address)

# BNB token address
bnb_token = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
console.log_address("Wbnb _token", bnb_token)

# CATS token address
cats_token = "0x3B3691d4C3EC75660f203F41adC6296a494404d0"
console.log_address("Cats _token", cats_token)

with open(os.path.abspath(os.path.dirname(__file__)) + "/router.json", "r") as load_f:
    pan_router_contract_abi = load_f.read()
with open(os.path.abspath(os.path.dirname(__file__)) + "/cats.json", "r") as load_f:
    cats_contract_abi = load_f.read()

#  sender address
sender_address = config.PRIVATE_KEY
console.log_address("地址 sender", sender_address)

# 查询当前地址BNB余额
balance = web3.eth.get_balance(sender_address)
human_readable = web3.fromWei(balance, "ether")
console.log_balance(sender_address, "BNB", human_readable)

# 实例化路由合约
contract = web3.eth.contract(pan_router_contract_address, abi=pan_router_contract_abi)
cats_contract = web3.eth.contract(cats_token, abi=cats_contract_abi)

# 查询当前地址cats余额
cats_balance = cats_contract.functions.balanceOf(sender_address).call()
console.log_balance(sender_address, "Cats", cats_balance)

# 指定购买代币
token_address = "0x3B3691d4C3EC75660f203F41adC6296a494404d0"
# token_address = console.log_input("交易的代币地址 : ")

# 检查地址正确性
try:
    token = web3.toChecksumAddress(token_address)
    spend = web3.toChecksumAddress(bnb_token)
except:
    console.log_address_err(token_address)

# 获取交易随机数
nonce = web3.eth.get_transaction_count(sender_address)

# 输入交易多少BNB
bnb_amount = console.log_input("交易的BNB数量 : ")

# 构建交易 用BNB买token

# 1) 手动生成事务
pancake_tx = contract.functions.swapExactETHForTokens(
    0,  # 最低获得的代币数量
    [spend, token],  # 路由路径 bnb token
    sender_address,  # 交换代币的用户
    int(time.time() + 10000)  # 交易最后期限
).buildTransaction({
    # str 发送方 地址或ens
    "from": sender_address,
    # 支付的数量
    "value": web3.toWei(bnb_amount, "ether"),
    # int 可以消耗的 Gas 的最大数量
    "gas": 250000,
    # int
    "gasPrice": web3.toWei(6, "gwei"),
    # int 随机数
    "nonce": nonce,
})

# 2) 使用发件人的私钥签署交易
signed_txn = web3.eth.account.sign_transaction(pancake_tx, private_key=config.PRIVATE_KEY)

# 3) 发送“原始”事务
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
trader_hash = web3.toHex(tx_hash)
console.log_address("交易hash : ", trader_hash)

# swapETHForExactTokens 使用bnb交换代币
# swapExactETHForTokens 代币交换bnb

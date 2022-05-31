# _*_ encoding=utf-8 _*_

import os

try:
    from colorama import Fore, Back, Style
except ImportError:
    os.system("pip3 install colorama")


class Console:
    def __init__(self):
        print(Fore.GREEN + '>>>>>>>>>>>')
        print(Style.RESET_ALL)

    def log_connerct(self,is_connerct):
        """
        输出节点连接结果 成功:继续执行 失败: 退出执行
        :param is_connerct: 连接结果
        :return:
        """
        print(Fore.CYAN + "节点是否连接: {}".format(is_connerct))
        print(Style.RESET_ALL)
        if not is_connerct:
            exit()

    def log_address_err(self,address):
        """
        输出地址错误
        :param address: address
        :return:
        """
        print(Fore.RED + "地址错误: {}".format(address))
        print(Style.RESET_ALL)
        exit()

    def log_address(self,addressname,address):
        """
        输出地址信息
        :param addressname: 地址名
        :param address: 地址
        :return:
        """
        print(Fore.CYAN + "{} : {}".format(addressname,address))
        print(Style.RESET_ALL)

    def log_balance(self,holder,symbol,balance):
        """
        输出持有人持有币种数量
        :param holder: 持有者
        :param symbol: 币种
        :param balance: 余额
        :return:
        """
        print(Fore.CYAN + "当前 {}  地址剩余 : {} {}".format(holder,balance,symbol))
        print(Style.RESET_ALL)

    def log_input(self,prompt):
        """
        获取返回输入
        :param prompt:
        :return:
        """
        try:
            inputstr = input(Fore.MAGENTA + prompt)
            print(Style.RESET_ALL)
            return inputstr
        except KeyboardInterrupt:
            print(Style.RESET_ALL)
            exit()





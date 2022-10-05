def privateKey():
    import random
    private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])
    private_key = '0x'+private_key
    print(private_key)

def mnemonicANDkey():
    #pip install mnemonic
    #pip install web3
    #pip install binascii
    #бібліотеки для 2-ї функції. Скачувати через термінал або командну строку.
    from web3 import Web3
    import mnemonic
    import binascii
    passphrase = mnemonic.Mnemonic('english')
    passphrase = passphrase.generate(strength=256)
    w3 = Web3()
    w3.eth.account.enable_unaudited_hdwallet_features()
    account = w3.eth.account.from_mnemonic(passphrase, account_path="m/44'/60'/0'/0/0")
    private_key = account.privateKey
    private_key = binascii.hexlify(private_key)
    private_key='0x'+private_key.decode("utf-8")
    print('mnemonic: '+passphrase)
    print('privateKey: '+private_key)
    print('address: '+account.address)

#privateKey()
mnemonicANDkey()
input('Press ENTER to close')
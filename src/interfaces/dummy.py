import logging

def getUrl(request_string):
    return requests.get(request_string).json()

def setHost():
    if config.LOCAL_BLOCKCHAIN and config.BLOCKCHAIN_CONNECT: pass
    elif config.LOCAL_BLOCKCHAIN:
        config.BLOCKCHAIN_CONNECT = ('http://localhost:3001' if config.TESTNET else 'http://localhost:3000')
    else: 
        config.BLOCKCHAIN_CONNECT = ("https://test-insight.bitpay.com/" if config.TESTNET else "https://insight.bitpay.com/")
    
def check():
    return True
    
def getInfo():
    return getUrl(config.BLOCKCHAIN_CONNECT + '/api/status?q=getInfo')

def getUtxo(address):
    return getUrl(config.BLOCKCHAIN_CONNECT + '/api/addr/' + address + '/utxo/')

def getAddressInfo(address):
    return getUrl(config.BLOCKCHAIN_CONNECT + '/api/addr/' + address + '/')

def getTxInfo(tx_hash):
    return getUrl(config.BLOCKCHAIN_CONNECT + '/api/tx/' + tx_hash + '/')

def getBlockInfo(block_hash):
    return getUrl(config.BLOCKCHAIN_CONNECT + '/api/block/' + block_hash + '/')
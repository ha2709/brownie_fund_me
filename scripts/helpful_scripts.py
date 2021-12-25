from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3
DECIMAL = 18
STARTING_PRICE = 2000
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development","ganache-local"]
FORKED_LOCAL_ENVIROMENTS =["mainnet-fork","mainnet-fork-dev-1"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS or \
          network.show_active() in FORKED_LOCAL_ENVIROMENTS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks")
    if len(MockV3Aggregator) <= 0 :
        MockV3Aggregator.deploy(
            DECIMAL, Web3.toWei(STARTING_PRICE,"ether"), {"from":get_account()})
    print("Mocked Deploy")   
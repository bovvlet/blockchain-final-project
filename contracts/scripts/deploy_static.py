from brownie import staticMinter, accounts

def main():

    account = accounts.load('testac')
    contract = staticMinter.deploy({'from': account}, publish_source=False)

    print(f"Your contract deployed at {contract}")



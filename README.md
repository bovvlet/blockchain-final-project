# Dynamic_NFT_bot
<h3>This Telegram bot allows you to mint dynamic NFTs with ease. The bot is built using Solidity, Chainlink keepers, OpenZeppelin, Python, and pyTelegramBotAPI.

</h4>

<br/><br/>
<p align="center">
<img src="https://github.com/bovvlet/blockchain-final-project/blob/main/images/1.png" width="190" height="270">
<img src="https://github.com/bovvlet/blockchain-final-project/blob/main/images/2.png" width="190" height="270">
<img src="https://github.com/bovvlet/blockchain-final-project/blob/main/images/3.png" width="190" height="270">
</p><br>

<p align="center">
<img src="https://github.com/bovvlet/blockchain-final-project/blob/main/images/4.png" width="290" height="300">
</p><br>

## Prerequisites
Please install or have installed the following:

- [Python](https://www.python.org/downloads/)
- [Telegram](https://telegram.org/)
- [Metamask](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjtl7Oi6N_4AhWei_0HHbjzDH4QjBB6BAgHEAE&url=https%3A%2F%2Fmetamask.io%2Fdownload%2F&usg=AOvVaw049ASZIf5umKu9KN8vjUeH)


## Installation
[Install virtualenv](https://virtualenv.pypa.io/en/latest/installation.html), To get started, install virtualenv if you haven't already. Here is a simple way to install venv:

```bash
python -m pip install --user virtualenv
python -m virtualenv --help
```
<br/>
Alternatively, you can use pipx:

```bash
pipx install virtualenv
virtualenv --help
```

Next, create a virtual environment and activate it:
```bash
python3 -m virtualenv venv
cd venv/bin
source activate
```

<br/>After that, install the following libraries using pip:


```bash
pip install web3
pip install eth-brownie
pip install ipfshttpclient
pip install pyTelegramBotAPI
```

# Usage
To initialize IPFS, run the following command:

```bash
ipfs daemon 
export IPFS_FILE_URL = "File_url"
export IPFS_CONNECT_URL= "Connect_url"
```

<br>To deploy the smart contract using Brownie, clone this repository and run the following commands:
```bash
cd ../contracts
brownie compile
brownie run scripts/deploy_dynamic.py --network <NETWORK>
brownie run scripts/deploy_static.py --network <NETWORK>
```

<br>Finally, set your API key and web3 provider (Alchemy or Infura) using the following command:
```bash
export WEB3_PROVIDER= "Web3_provider"
export API_KEY= "Api_key"
```


<br>Once you have completed these steps, you can run the bot using the following command:


```bash
python3 main.py
```

## License

This project is licensed under the [MIT license](LICENSE).

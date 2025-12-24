import requests
import sys

ETH_RPC = "https://ethereum.publicnode.com"
BASE_RPC = "https://mainnet.base.org"

def get_balance(address, rpc_url):
    data = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1
    }
    response = requests.post(rpc_url, json=data)
    result = response.json().get("result")
    if result:
        return int(result, 16) / 10**18  # Wei → ETH
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <wallet_address>")
        return

    address = sys.argv[1]
    print(f"🔎 Checking balance for: {address}\n")

    eth_balance = get_balance(address, ETH_RPC)
    base_balance = get_balance(address, BASE_RPC)

    print(f"🌐 Ethereum Balance: {eth_balance} ETH")
    print(f"🔵 Base Balance: {base_balance} ETH")

if __name__ == "__main__":
    main()
# This function retrieves wallet balance from Ethereum or Base network

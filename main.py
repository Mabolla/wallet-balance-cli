import re
import sys

import requests


ETH_RPC = "https://ethereum.publicnode.com"
BASE_RPC = "https://mainnet.base.org"

ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
REQUEST_TIMEOUT = 10


def is_valid_address(address):
    return bool(ADDRESS_PATTERN.fullmatch(address))


def get_balance(address, rpc_url):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [address, "latest"],
        "id": 1,
    }

    try:
        response = requests.post(
            rpc_url,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return None, data["error"].get("message", "Unknown RPC error")

        result = data.get("result")

        if result is None:
            return None, "RPC response did not contain a balance"

        return int(result, 16) / 10**18, None

    except requests.RequestException as exc:
        return None, f"Network error: {exc}"
    except (ValueError, TypeError):
        return None, "Invalid response received from RPC endpoint"


def print_balance(network, balance, error):
    if error:
        print(f"{network}: unavailable ({error})")
    else:
        print(f"{network}: {balance:.6f} ETH")


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <wallet_address>")
        sys.exit(1)

    address = sys.argv[1].strip()

    if not is_valid_address(address):
        print("Error: invalid EVM wallet address.")
        sys.exit(1)

    print(f"Checking balances for {address}\n")

    eth_balance, eth_error = get_balance(address, ETH_RPC)
    base_balance, base_error = get_balance(address, BASE_RPC)

    print_balance("Ethereum", eth_balance, eth_error)
    print_balance("Base", base_balance, base_error)


if __name__ == "__main__":
    main()
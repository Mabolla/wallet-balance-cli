<div align="center">

# Wallet Balance CLI 🔵

**A lightweight command-line tool for checking native wallet balances on Ethereum and Base.**

Built as part of my ongoing work with Base and onchain developer tooling.

</div>

---

## Overview

`wallet-balance-cli` is a lightweight Python CLI that reads the native ETH balance of any EVM address across:

- **Ethereum Mainnet**
- **Base Mainnet**

The tool communicates directly with public JSON-RPC endpoints using `eth_getBalance` and converts the returned Wei value into ETH.

No wallet connection or private key is required.

---

## Features

- Check Ethereum and Base balances in one command
- Validate EVM wallet addresses before making RPC requests
- Handle network, HTTP, and JSON-RPC errors
- Use direct JSON-RPC requests
- No private key or wallet connection required
- Minimal dependencies
- Read-only by design

---

## How It Works

    Wallet Address
          |
          +--> Ethereum RPC --> eth_getBalance
          |
          +--> Base RPC ------> eth_getBalance
                                  |
                                  v
                               Wei -> ETH

The application only reads publicly available blockchain state. It does not sign or submit transactions.

---

## Installation

Clone the repository:

    git clone https://github.com/Mabolla/wallet-balance-cli.git
    cd wallet-balance-cli

Install the dependency:

    pip install -r requirements.txt

---

## Usage

Run:

    python main.py <wallet_address>

Example:

    python main.py 0x94705a9d675daa924f9190eca4c05ed6b12d5345

Example output:

    Checking balances for 0x94705a9d675daa924f9190eca4c05ed6b12d5345

    Ethereum: 0.003207 ETH
    Base: 0.003171 ETH

Invalid addresses are rejected before an RPC request is made:

    Error: invalid EVM wallet address.

---

## Tech

`Python` · `JSON-RPC` · `Ethereum` · `Base`

---

## Roadmap

- [x] Ethereum native balance
- [x] Base native balance
- [x] Wallet address validation
- [x] Improved RPC error handling
- [ ] ERC-20 token balances
- [ ] Configurable networks and RPC endpoints

---

## Why Base?

This project started as a small utility for working with wallet data across Ethereum and Base.

It is being developed incrementally as part of a broader effort to build useful onchain tooling and Base-native applications.

---

## License

MIT License.
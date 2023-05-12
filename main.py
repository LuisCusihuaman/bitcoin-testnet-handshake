from network import SimpleNode


def main():
    testnet = True
    testnet_host = "195.201.126.87"
    '''hand shake and get verack'''
    node = SimpleNode(testnet_host, testnet=testnet, logging=True)
    node.handshake()


if __name__ == '__main__':
    main()

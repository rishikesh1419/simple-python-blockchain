from Block import *
from Blockchain import *

if __name__ == "__main__":
    blockchain = Blockchain()
    for i in range(3):
        b = Block(str(i))
        blockchain.mine_block(b)
    print(blockchain)

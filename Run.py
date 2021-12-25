from Block import *
from Blockchain import *
from Transaction import Transaction

if __name__ == "__main__":
    blockchain = Blockchain()
    for i in range(3):
        b = Block(str(i))
        blockchain.add_block(b)
    print(blockchain)

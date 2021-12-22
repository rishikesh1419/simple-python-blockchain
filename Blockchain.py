from Block import *


class Blockchain:
    head = None
    last_block = None
    chain = []
    difficulty = 3
    prefix = "".join(["0" for _ in range(difficulty)])

    def __init__(self) -> None:
        self.head = self.last_block = Block("Genesis block")

    def __str__(self) -> str:
        temp = self.head
        while temp != None:
            print("Data:", temp.data)
            print("Hash:", temp.hash)
            # print("Next", temp.next)
            temp = temp.next

    def add_block(self, block: Block) -> None:
        # print(block)
        self.last_block.next = block
        self.last_block = block
        print(self.last_block)

    def mine_block(self, block: Block) -> None:
        # nonce = 0
        hash = block.get_hash()
        # print(hash[: self.difficulty])
        # print(self.prefix)
        while hash[: self.difficulty] != self.prefix:
            block.nonce = block.nonce + 1
            hash = block.get_hash()
        block.hash = hash
        self.add_block(block)

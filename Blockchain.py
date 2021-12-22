from Block import *


class Blockchain:
    head = None
    last_block = None
    chain = []
    difficulty = 5
    prefix = "".join(["0" for _ in range(difficulty)])

    def __init__(self) -> None:
        self.head = self.last_block = Block("Genesis block")

    def __str__(self) -> str:
        string = ""
        temp = self.head
        while temp != None:
            string = string + "Data: " + temp.data + "\n"
            string = string + "Hash: " + str(temp.hash) + "\n"
            string = string + "Nonce: " + str(temp.nonce) + "\n"
            temp = temp.next
        return string

    def add_block(self, block: Block) -> None:
        self.last_block.next = block
        self.last_block = block

    def mine_block(self, block: Block) -> None:
        hash = block.get_hash()
        while hash[: self.difficulty] != self.prefix:
            block.nonce = block.nonce + 1
            hash = block.get_hash()
        block.hash = hash
        self.add_block(block)

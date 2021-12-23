from Block import *


class Blockchain:
    chain = []
    difficulty = 1
    prefix = "".join(["0" for _ in range(difficulty)])

    def __init__(self) -> None:
        self.add_block(Block("Genesis Block"))

    def __str__(self) -> str:
        string = ""
        for i in range(len(self.chain)):
            temp = self.chain[i]
            string = string + "Data: " + temp.data + "\n"
            string = string + "Hash: " + str(temp.hash) + "\n"
            string = string + "Prev Hash: " + str(temp.prev_hash) + "\n"
            string = string + "Nonce: " + str(temp.nonce) + "\n\n"
        return string

    def add_block(self, block: Block) -> None:
        if len(self.chain):
            block.prev_hash = self.chain[-1].hash
        block.mine_block(self.difficulty, self.prefix)
        self.chain.append(block)

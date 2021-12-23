from Block import *


class Blockchain:
    chain = []
    difficulty = 1
    prefix = "".join(["0" for _ in range(difficulty)])

    def __init__(self) -> None:
        self.add_block(Block("Genesis Block"))

    def __str__(self) -> str:
        string = ""
        for block in self.chain:
            string = string + "\nData: " + block.data + "\n"
            string = string + "Hash: " + str(block.hash) + "\n"
            string = string + "Prev Hash: " + str(block.prev_hash) + "\n"
            string = string + "Nonce: " + str(block.nonce) + "\n"
        return string

    def add_block(self, block: Block) -> None:
        if len(self.chain):
            block.prev_hash = self.chain[-1].hash
        block.mine_block(self.difficulty, self.prefix)
        self.chain.append(block)

    def verify_chain(self) -> bool:
        if len(self.chain) == 1:
            if self.chain[0].hash != self.chain[0].get_hash():
                return False
            return True
        for i in range(1, len(self.chain)):
            current: Block = self.chain[i]
            prev: Block = self.chain[i - 1]
            if current.hash != current.get_hash():
                return False
            if current.prev_hash != prev.hash:
                return False
        return True

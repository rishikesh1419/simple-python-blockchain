from Block import *


class Blockchain:
    head = None
    last_block = None
    chain = []
    difficulty = 20
    prefix = "".join(["0" for _ in range(difficulty)])

    def __init__(self) -> None:
        self.head = self.last_block = Block("Genesis block")
        pass

    def add_block(self, block: Block) -> None:
        self.last_block.next = block

    def mine_block(self, block: Block) -> None:
        # How?? Prefoix 0s??
        # String substring
        ## What about prefix 0x
        nonce = 0
        hash = block.get_hash()
        while hash[: self.difficulty] != self.prefix:
            nonce = nonce + 1
            hash = block.get_hash()
        block.hash = hash
        self.add_block(block)

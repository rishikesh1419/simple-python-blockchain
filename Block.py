import datetime
import hashlib


class Block:
    block_number: int = 0
    data: str = None
    hash: str = None
    nonce: int = 0
    prev_hash: str = None

    def __init__(self, data) -> None:
        self.data = data
        self.timestamp = datetime.datetime.now()

    def __str__(self) -> str:
        return (
            "Block Number: "
            + str(self.block_number)
            + "\n"
            + "Hash: "
            + str(self.hash)
            + "\n"
            + "Prev Hash: "
            + str(self.prev_hash)
            + "\n"
            + "Data: "
            + str(self.data)
            + "\n"
        )

    def get_hash(self):
        hash = hashlib.sha256()
        hash.update(
            str(self.block_number).encode()
            + str(self.timestamp).encode()
            + str(self.prev_hash).encode()
            + str(self.nonce).encode()
            + str(self.data).encode()
        )
        return hash.hexdigest()

    def mine_block(self, difficulty: int, prefix: str) -> None:
        hash = self.get_hash()
        while hash[:difficulty] != prefix:
            self.nonce = self.nonce + 1
            hash = self.get_hash()
        self.hash = hash

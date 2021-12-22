import datetime
import hashlib


class Block:
    block_number = 0
    data = None
    next = None
    hash = None
    nonce = 0
    prev_hash = None
    timestamp = datetime.datetime.now()

    def __init__(self, data) -> None:
        self.data = data

    def __str__(self) -> str:
        return (
            "Block Number: "
            + str(self.block_number)
            + "\n"
            + "Hash: "
            + str(self.hash)
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


if __name__ == "__main__":

    print("Testing")
    b = Block("Newblock mfs")
    print(b.get_hash())
    print(b)
    print("Lol")

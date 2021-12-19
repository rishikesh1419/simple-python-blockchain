import datetime
import hashlib


class Block:
    block_number = 0
    data = None
    next = None
    hash = None
    nonce = 0
    prev_hash = "0x0"
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def get_hash(self):
        hash = hashlib.sha256()
        hash.update(
            str(self.block_number).encode()
            + str(self.timestamp).encode()
            + str(self.prev_hash).encode()
            + str(self.nonce).encode
            + str(self.data).encode()
        )
        return hash.hexdigest()

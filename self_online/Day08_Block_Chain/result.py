import hashlib
import time
import json

class Block():
    def __init__(self, index, timestamp, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = 0
        self.nonce = 0
        self.hash = self.calHash()

    def calHash(self):
        return hashlib.sha256(str(self.index).encode() + str(self.data).encode() +
                            str(self.nonce).encode() + str(self.timestamp).encode() + str(self.previousHash).encode()).hexdigest()

    def mine(self, difficulty):
        ans = ["0"]*difficulty
        answer = "".join(ans)
        while(str(self.hash)[:difficulty] != answer):
            self.nonce += 1
            self.hash = self.calHash()

        return self.hash


class BlockChain:
    def __init__(self, ):
        self.chain = []
        self.difficulty = 5
        self.createGenesis()

    def createGenesis(self):
        self.chain.append(Block(0, time.time(), 'Genesis Block'))

    def addBlock(self, nBlock):
        nBlock.previousHash = self.chain[len(self.chain)-1].hash
        nBlock.hash = nBlock.mine(self.difficulty)
        self.chain.append(nBlock)

    def getLatestBlock(self):
        return self.chain[len(self.chain)-1]

    def isValid(self):
        i = 1
        while(i<len(self.chain)):
            if(self.chain[i].hash != self.chain[i].calHash()):

                return False
            if(self.chain[i].previousHash != self.chain[i-1].hash):

                return False
            i += 1
        return True

onion = BlockChain()
onion.addBlock(Block(len(onion.chain),time.time(), "2nd"))
onion.addBlock(Block(len(onion.chain),time.time(), "3rd"))
onion.addBlock(Block(len(onion.chain),time.time(), "4rd"))
onion.addBlock(Block(len(onion.chain),time.time(), "5rd"))
for block in onion.chain:
    print(json.dumps(vars(block), indent=4))
# This file is an example script that needed to be created to test out the blockchain that was created

# import the blockchain
from blockchain import Blockchain

# transactions for testing
block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

# create a blockchain called "local_blockchain"
local_blockchain = Blockchain()
# local_blockchain.print_blocks()

# adding and printing the blocks
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
# local_blockchain.print_blocks()

# tamper with the blockchain to see what happens
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()

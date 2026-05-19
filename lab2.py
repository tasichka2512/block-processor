from dataclasses import dataclass
 
@dataclass
class Vote:
    blockId: str
 
    def __hash__(self):
        return hash(self.blockId)
    
@dataclass
class Block:
    blockId: str
    view: int

with open('lab2.csv') as data:
    votes = set()
    blocks = {}
    current_view = 0
    seen_ids = set()
    chain = []
    for line in data:
        recordType, blockId, vote, view = [s.strip() for s in line.split(',')]
        if recordType == 'block':
            new_block = Block(blockId, int(view))
            blocks[new_block.view] = new_block
        elif recordType == 'vote':
            new_vote = Vote(vote)
            votes.add(new_vote)
        while current_view in blocks:
            block_current = blocks[current_view]
            if Vote(block_current.blockId) in votes:
                if block_current.blockId not in seen_ids:
                   chain.append(block_current)
                   seen_ids.add(block_current.blockId)
                del blocks[current_view]
                current_view += 1
            else:
                break
for b in chain:
    print(b.view, b.blockId)
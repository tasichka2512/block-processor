from pydantic import BaseModel, Field
import sqlite3

class Block(BaseModel):
    id: str = Field(pattern=r"^[0-9a-fA-F]{8}$") 
    view: int = Field(ge=0) 
    desc: str = Field(min_length=1)
    img: bytes

    @classmethod
    def get_all(cls, cur: sqlite3.Cursor):
        rows = cur.execute("SELECT id, view, desc, img FROM blocks").fetchall()
        blocks_list = []
        for row in rows:
            block = cls(id=row[0], view=row[1], desc=row[2], img=row[3])
            blocks_list.append(block)
        return blocks_list
    
class Source(BaseModel):
    id: int = Field(ge=0)
    ip_addr: str = Field(min_length=7, max_length=15)
    country_code: str = Field(pattern=r"^[A-Z]{2}$")

    @classmethod
    def get_all(cls, cur: sqlite3.Cursor):
        rows = cur.execute("SELECT id, ip_addr, country_code FROM sources").fetchall()
        sources_list = []
        for row in rows:
            source = cls(id=row[0], ip_addr=row[1], country_code=row[2])
            sources_list.append(source)
        return sources_list
    
class Vote(BaseModel):
    block_id: str = Field(pattern=r"^[0-9a-fA-F]{8}$")
    voter_id: int = Field(ge=0)
    timestamp: str
    source_id: int = Field(ge=0)

    @classmethod
    def get_all(cls, cur: sqlite3.Cursor):
        rows = cur.execute("SELECT block_id, voter_id, timestamp, source_id FROM votes").fetchall()
        votes_list = []
        for row in rows:
            vote = cls(block_id=row[0], voter_id=row[1], timestamp=row[2], source_id=row[3])
            votes_list.append(vote)
        return votes_list
    
class Person(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(min_length=2)
    addr: str = Field(min_length=3)

    @classmethod
    def get_all(cls, cur: sqlite3.Cursor):
        rows = cur.execute("SELECT id, name, addr FROM persons").fetchall()
        persons_list = []
        for row in rows:
            person = cls(id=row[0], name=row[1], addr=row[2])
            persons_list.append(person)
        return persons_list
    
if __name__ == "__main__":
    con = sqlite3.connect('blocks.db')
    cur = con.cursor()

    blocks = Block.get_all(cur)
    sources = Source.get_all(cur)
    votes = Vote.get_all(cur)
    persons = Person.get_all(cur)

    con.close()
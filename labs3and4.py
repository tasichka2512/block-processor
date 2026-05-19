import sqlite3
from dataclasses import dataclass

@dataclass
class Block:
    id: str
    view: int
    desc: str
    img: bytes = None

    @classmethod
    def get_all(cls, cur: sqlite3.Cursor):
        return [cls(*row) for row in cur.execute("SELECT id, view, desc, img FROM blocks").fetchall()]
    
@dataclass
class Source:
    id: int
    ip_addr: str
    country_code: str

    @classmethod
    def get_all(cls, cur: sqlite3.Cursor):
        return [cls(*row) for row in cur.execute("SELECT id, ip_addr, country_code FROM sources").fetchall()]

@dataclass
class Vote:
    block_id: str
    voter_id: int
    timestamp: str
    source_id: int

    @classmethod
    def get_all(cls, cur: sqlite3.Cursor):
        return [cls(*row) for row in cur.execute("SELECT block_id, voter_id, timestamp, source_id FROM votes").fetchall()]

@dataclass
class Person:
    id: int
    name: str
    addr: str

    @classmethod
    def get_all(cls, cur: sqlite3.Cursor):
        return [cls(*row) for row in cur.execute("SELECT id, name, addr FROM persons").fetchall()]

con = sqlite3.connect('blocks.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS blocks (id TEXT PRIMARY KEY, view INTEGER, desc TEXT, img BLOB)')
cur.execute('CREATE TABLE IF NOT EXISTS sources (id INTEGER PRIMARY KEY, ip_addr TEXT, country_code TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS votes (block_id TEXT, voter_id INTEGER, timestamp TEXT, source_id INTEGER)')
cur.execute('CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY, name TEXT, addr TEXT)')

blocks1 = [('0x156', 0, 'block1', None),
            ('0x123', 1, 'block2', None)]
cur.executemany("INSERT OR IGNORE INTO blocks VALUES (?, ?, ?, ?)", blocks1)

sources1 =[(0, '123.45.67.890', 'UA'),
            (1, '17.172.224.47', 'DE')]
cur.executemany("INSERT OR IGNORE INTO sources VALUES (?, ?, ?)", sources1)

votes1 = [('0x156', 0, '2026-03-12', 0),
        ('0x123', 1, '2026-03-15', 1)]
cur.executemany("INSERT OR IGNORE INTO votes VALUES(?, ?, ?, ?)", votes1)

persons1 = [(0, 'Kate', 'Lviv'),
            (1, 'John', 'Mykolaiv')]
cur.executemany("INSERT OR IGNORE INTO persons VALUES (?, ?, ?)", persons1)
con.commit()

blocks = Block.get_all(cur)
for b in blocks:
    print(f"Блок: {b.id}; View: {b.view}; Опис: {b.desc}")

sources = Source.get_all(cur)
for s in sources:
    print(f"IP-адреса: {s.ip_addr}; Країна: {s.country_code}")    

votes = Vote.get_all(cur)
for v in votes:
        print(f"Блок: {v.block_id}; Voter: {v.voter_id}; Дата: {v.timestamp}; Джерело: {v.source_id}")

persons = Person.get_all(cur)
for p in persons:
    print(f"Особа: {p.name}, Адреса: {p.addr}")

con.close()
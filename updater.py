import sqlite3

def main():
    con = sqlite3.connect('blocks.db')
    cur = con.cursor()

    print("updater started...")
    print("comands: block, exit")

    while True:
        cmd = input("\nchoose your command: ").strip().lower()
        if cmd == 'exit':
            break
        elif cmd == 'block':
            b_id = input("input block id: ")
            try:
                b_view = int(input("input block view: "))
                b_desc = input("description: ")
                cur.execute("INSERT OR IGNORE INTO blocks (id, view, desc) VALUES (?, ?, ?)", 
                            (b_id, b_view, b_desc))
                cur.execute("INSERT INTO event_stream (type, id) VALUES ('block', ?)", (b_id,))
                con.commit()
                print(f"block {b_id} was added")
            except ValueError:
                print("view has to be an integer")
        else:
            print("unknown command")
    con.close()

if __name__ == "__main__":
    main()
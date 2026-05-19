import sqlite3
import time

def run_processor():
    con = sqlite3.connect('blocks.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS event_stream (type TEXT, id TEXT, processed INTEGER DEFAULT 1)')
    con.commit()

    print('Block Processor started...')

    try:
        while True:
            cur.execute('SELECT type, id FROM event_stream WHERE processed = 1 LIMIT 1')
            row = cur.fetchone()

            if row:
                new_type, new_id = row
                print(f'New object: type - {new_type}, id - {new_id}')
                if new_type == 'block':
                    cur.execute('SELECT id, view FROM blocks WHERE id = ?', (new_id,))
                cur.execute('UPDATE event_stream SET processed = 0 WHERE id = ?', (new_id,))
                con.commit()
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        print("\n Processor stopped by input")
    finally:
        con.close()

if __name__ == "__main__":
    run_processor()
import db

def add_item(title, author, genre, description, rate, user_id):
    sql = """INSERT INTO items (title, author, genre, description, rate, user_id) 
               VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, author, genre, description, rate, user_id])


def get_items():
    sql = "SELECT id, title FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = "SELECT id, title, author, genre, description, rate, user_id FROM items WHERE id = ?"
    result = db.query(sql, [item_id])
    return result[0] if result else None

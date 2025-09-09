import sqlite3

# Replace with your real database filename if different
db_path = 'database.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Add the missing column
try:
    cursor.execute('ALTER TABLE unfinished_operations ADD COLUMN message_id INTEGER;')
    print("✅ Column 'message_id' added successfully.")
except sqlite3.OperationalError as e:
    print(f"⚠️ Error: {e}")

# Add lottery tickets column
try:
    cursor.execute("ALTER TABLE users ADD COLUMN lottery_tickets INTEGER DEFAULT 0;")
    print("✅ Column 'lottery_tickets' added successfully.")
except sqlite3.OperationalError as e:
    print(f"⚠️ Error: {e}")

# Add streak tracking columns
try:
    cursor.execute("ALTER TABLE users ADD COLUMN purchase_streak INTEGER DEFAULT 0;")
    print("✅ Column 'purchase_streak' added successfully.")
except sqlite3.OperationalError as e:
    print(f"⚠️ Error: {e}")

try:
    cursor.execute("ALTER TABLE users ADD COLUMN last_purchase_date TEXT;")
    print("✅ Column 'last_purchase_date' added successfully.")
except sqlite3.OperationalError as e:
    print(f"⚠️ Error: {e}")

try:
    cursor.execute("ALTER TABLE users ADD COLUMN streak_discount INTEGER DEFAULT 0;")
    print("✅ Column 'streak_discount' added successfully.")
except sqlite3.OperationalError as e:
    print(f"⚠️ Error: {e}")

# Ensure stock notifications table
try:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS stock_notifications (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, item_name TEXT);"
    )
    print("✅ Stock notifications table ensured.")
except sqlite3.OperationalError as e:
    print(f"⚠️ Error: {e}")

conn.commit()
conn.close()

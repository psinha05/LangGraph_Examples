import sqlite3

def delete_thread(thread_id):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM conversations WHERE thread_id = ?",
        (str(thread_id),)
    )

    conn.commit()
    conn.close()

   

import sqlite3
from transformers import pipeline

# 感情分析モデルをロードする
classifier = pipeline('sentiment-analysis', model="jarvisx17/japanese-sentiment-analysis")

# SQLiteデータベースに接続する
conn = sqlite3.connect('notes.db')

# テーブルを作成する
conn.execute('''CREATE TABLE IF NOT EXISTS notes
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT NOT NULL,
             content TEXT NOT NULL,
             sentiment TEXT);''')

# メモを作成する関数
def create_note():
    title = input("タイトルを入力してください：")
    content = input("内容を入力してください：")
    sentiment = classifier(content)[0]['label']
    
    # メモをデータベースに追加する
    conn.execute("INSERT INTO notes (title, content, sentiment) VALUES (?, ?, ?)", (title, content, sentiment))
    conn.commit()
    print("メモが作成されました。")

# メモを表示する関数
def view_notes():
    cursor = conn.execute("SELECT * FROM notes")
    for row in cursor:
        print(f"{row[0]} - {row[1]} ({row[2]})")
        print(f"{row[3]}\n")

def delete_note():
    """
    指定されたIDのメモを削除する
    """
    note_id = input("削除するIDを指定してください:")
    
    # tryで書く
    try:
        # データベースからメモを削除する
        conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        print("メモが削除されました")
    except:
        print("メモの削除に失敗しました")

# メニューを表示する関数
def menu():
    while True:
        print("\nメニュー\n1. メモを作成する\n2. メモを表示する\n3. メモを削除する\n4. 終了する")
        choice = input("選択してください：")
        
        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            break
        else:
            print("無効な選択です。")

# アプリを実行する
if __name__ == "__main__":
    menu()

# データベースを閉じる
conn.close()
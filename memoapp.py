tasks = []  # タスクを格納するリスト

# タスクの追加
def add_task():
    task_name = input("タスク名を入力してください: ")
    tasks.append(task_name)
    print(f"{task_name}をタスクに追加しました。")

# タスクの表示
def show_tasks():
    if not tasks:
        print("現在、タスクはありません。")
    else:
        print("現在のタスク:")
        for task in tasks:
            print(task)

# タスクの削除
def remove_task():
    task_name = input("削除するタスク名を入力してください: ")
    if task_name in tasks:
        tasks.remove(task_name)
        print(f"{task_name}をタスクから削除しました。")
    else:
        print(f"{task_name}はタスクにありません。")

# メイン処理
while True:
    print("\n[メニュー]")
    print("1: タスクの追加")
    print("2: タスクの表示")
    print("3: タスクの削除")
    print("4: 終了")
    choice = input("選択してください: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("アプリを終了します。")
        break
    else:
        print("無効な選択肢です。もう一度選択してください。")

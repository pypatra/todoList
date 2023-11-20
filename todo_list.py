class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" ditambahkan.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" dihapus.')
        else:
            print(f'Task "{task}" tidak ditemukan.')

    def view_tasks(self):
        if not self.tasks:
            print("To-Do List kosong.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Tambah Task")
        print("2. Hapus Task")
        print("3. Lihat To-Do List")
        print("4. Keluar")

        choice = input("Pilih menu (1/2/3/4): ")

        if choice == '1':
            new_task = input("Masukkan task baru: ")
            todo_list.add_task(new_task)
        elif choice == '2':
            task_to_remove = input("Masukkan task yang ingin dihapus: ")
            todo_list.remove_task(task_to_remove)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()

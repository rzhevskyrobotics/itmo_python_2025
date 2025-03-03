class TreeNode:
    """Узел дерева"""

    def __init__(self, value):
        self.value = value  # ключ со значением в узле
        self.left = None    # ключ-ссылка на узел левого потомка
        self.right = None   # ключ-ссылка на узел правого потомка
        self.parent = None  # ключ-ссылка на родительский узел


class BinarySearchTree:
    """Поиск по бинарному дереву"""

    def __init__(self):
        self.root = None # Инициализация с корнем

    # Метод для добавления элемента в дерево
    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right

    # Метод для поиска элемента в дереве
    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    # Метод для удаления элемента из дерева
    def delete(self, value):
        node = self.search(value)
        if node is None:
            print(f"Элемент {value} не найден.")
            return

        # Метод для склейки веток при удалении
        def transplant(u, v):
            if u.parent is None:
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            if v is not None:
                v.parent = u.parent

        # Если у узла нет левого потомка
        if node.left is None:
            transplant(node, node.right)
        # Если у узла нет правого потомка
        elif node.right is None:
            transplant(node, node.left)
        else:
            # Находим минимальный элемент в правом поддереве
            successor = self._min(node.right)
            if successor.parent != node:
                transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    # Метод для поиска минимального значения в дереве
    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Метод для печати дерева (in-order обход)
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)


# Функция для реализации CLI интерфейса
def cli():
    bst = BinarySearchTree()
    while True:
        print("\nВыберите действие:")
        print("1. Добавить элемент")
        print("2. Найти элемент")
        print("3. Удалить элемент")
        print("4. Печать дерева")
        print("5. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            value = int(input("Введите значение для добавления: "))
            bst.insert(value)
            print(f"Элемент {value} успешно добавлен.")

        elif choice == "2":
            value = int(input("Введите значение для поиска: "))
            result = bst.search(value)
            if result:
                print(f"Элемент {value} найден.")
            else:
                print(f"Элемент {value} не найден.")

        elif choice == "3":
            value = int(input("Введите значение для удаления: "))
            bst.delete(value)

        elif choice == "4":
            print("\nПечать дерева:")
            bst.print_tree()

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    cli()
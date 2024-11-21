# task 1 Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable

class TaskOneIterator:

    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2
    
    def __iter__(self):
        self.current = max(self.num1, self.num2)
        return self

    def __next__(self):
        if self.current == min(self.num1, self.num2) - 1:
            raise StopIteration()
        
        result = self.current
        self.current -= 1
        return result

iterable_obj = TaskOneIterator(5, 11)
    
for i in iterable_obj:
    print(i)

# task 2 Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, додавши методи очищення списку,
# додавання елемента у довільне місце списку, видалення елемента з кінця та довільного місця списку.

# task 3 Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

class ReverseListIterator:

    def __init__(self, given_list: list):
        self.given_list = given_list
        self.index = len(given_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration()

        result = self.given_list[self.index]
        self.index -= 1
        return result


str_list = ['You', 'are', 'the', 'best']

for i in ReverseListIterator(str_list):
    print(i)

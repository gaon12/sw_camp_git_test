class ListNode:
        def __init__(self, newItem, nextNode: 'ListNode'):
                self.item = newItem
                self.next = nextNode

class LinkedListBasic:
        def __init__(self):
                self.__head = ListNode("dummy", None)
                self.__numItems = 0

        def insert(self, i: int, newItem):
                if i >= 0 and i <= self.__numItems:
                        prev = self.__getNode(i - 1)
                        newNode = ListNode(newItem, prev.next)
                        prev.next = newNode
                        self.__numItems += 1
                else:
                        print("index", i, ": out of bound in insert()")    # 필요 시 에러 처리

        def append(self, newItem):
                self.insert(self.__numItems, newItem)

        def pop(self, i: int):    # i번 노드 삭제. 고정 파라미터
                if (i >= 0 and i <= self.__numItems - 1):
                        prev = self.__getNode(i - 1)
                        curr = prev.next
                        prev.next = curr.next
                        retItem = curr.item
                        self.__numItems -= 1
                        return retItem
                else:
                        return None

        def remove(self, x):
                (prev, curr) = self.__findNode(x)
                if curr != None:
                        prev.next = curr.next
                        self.__numItems -= 1
                        return x
                else:
                        return None

        def get(self, i: int):
                if self.isEmpty():
                        return None
                if (i >= 0 and i <= self.__numItems - 1):
                        return self.__getNode(i).item
                else:
                        return None

        def index(self, x) -> int:
                curr = self.__head.next    # 0번 노드: 더미 헤드 다음 노드
                for index in range(self.__numItems):
                        if curr.item == x:
                                return index
                        else:
                                curr = curr.next
                return -12345    # 안쓰는 인덱스

        def isEmpty(self) -> bool:
                return self.__numItems == 0

        def size(self) -> int:
                return self.__numItems

        def clear(self):
                self.__head = ListNode("dummy", None)
                self.__numItems = 0

        def count(self, x) -> int:
                cnt = 0
                curr = self.__head.next    # 0번 노드
                while curr != None:
                        if curr.item == x:
                                cnt += 1
                        curr = curr.next
                return cnt

        def extend(self, a):    # 여기서 a는 self와 같은 타입의 리스트
                for index in range(a.size()):
                        self.append(a.get(index))

        def copy(self):
                a = LinkedListBasic()
                for index in range(self.__numItems):
                        a.append(self.get(index))
                return a

        def reverse(self):
                a = LinkedListBasic()
                for index in range(self.__numItems):
                        a.insert(0, self.get(index))
                self.clear()
                for index in range(a.size()):
                        self.append(a.get(index))

        def sort(self) -> None:
                a = []
                for index in range(self.__numItems):
                        a.append(self.get(index))
                a.sort()
                self.clear()
                for index in range(len(a)):
                        self.append(a[index])

        def __findNode(self, x) -> ListNode:
                prev = self.__head
                curr = prev.next
                while curr != None:
                        if curr.item == x:
                                return (prev, curr)
                        else:
                                prev = curr
                                curr = curr.next
                return (None, None)

        def __getNode(self, i: int) -> ListNode:
                if i < -1 or i >= self.__numItems:
                        return None
                else:
                        curr = self.__head
                        for j in range(i + 1):
                                curr = curr.next
                        return curr

        def printList(self):
                curr = self.__head.next    # 0번 노드: 더미 헤드 다음 노드
                while curr != None:
                        print(curr.item, end=" ")
                        curr = curr.next
                print()

class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()
    
    def push(self, newItem):
        self.__list.insert(0, newItem)
    
    def pop(self):
        return self.__list.pop(0)
    
    def top(self):
        return self.__list.get(0)
    
    def isEmpty(self) -> bool:
        return self.__list.isEmpty()
    
    def popAll(self):
        self.__list.clear()
    
    def printStack(self):
        print("Stack from top:", end=' ')
        for i in range(self.__list.size()):
            print(self.__list.get(i), end=' ')
        print()

st1 = LinkedStack()
st1.push(100)
st1.push(200)
print("Top is", st1.top())
st1.pop()
st1.push('Monday')
st1.printStack()
print('isEmpty?', st1.isEmpty())
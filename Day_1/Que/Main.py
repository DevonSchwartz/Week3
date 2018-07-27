class MyQue:
    def __init__(self):
        self.lst = []

    def push(self, x):
        lst = self.lst
        lst.append(x)
        return (lst)

    def push_lst(self,inpt_lst):
        inpt_lst = inpt_lst.split(',')
        print (inpt_lst)
        for i in inpt_lst:
            self.lst.append(i)
        print (self.lst)

    def pop(self):
        old_lst = self.lst[0]
        self.lst.append(self.lst[0])
        self.lst = self.lst[1:]
        return (old_lst)
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
    def pop_lst(self, n):
        result = []
        #while int(n) > 0:
            #old_lst = self.lst[-1]
            #[old_lst] + self.lst
            #self.lst = self.lst[1:-1]
        #return ("The last element was "+ old_lst)
        while n > 0:
            result.append(self.pop())
            n -= 1
        for i in result:
            print ("The first element was " + str(i) + " for the " + str(result.index(i) + 1) + " item popped.")




    def peek(self):
        return ("The first element is now " + self.lst[0])
        """
        Get the front element.
        :rtype: int
        """


    def empty(self):
        lst = self.lst
        if len(lst) == 0:
            return (str(True) + ": The list is empty")
            print (lst)
        elif len(lst) != 0:
            return (str(False) + ": The list contains elements")
            print (lst)
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

f = MyQue()

choice = input("Type 'list'to input an entire list or 'one' to input one \
item at a time: ")

if choice == 'one':
    count = eval(input("How many items would you like to input: "))
    while count > 0:
        inpt = input("What would you like to input: ")
        r = f.push(inpt)
        count -= 1

elif choice == 'list':
    inpt = input("Input a list and separate with commas: ")
    f.push_lst(inpt)


choice_2 = input("Would you like to specify the amount of elements you \
would like to pop or simply pop the first one? Type 'specify'\
to specify or 'first' to pop the first: ")

if choice_2 == 'specify':
    n = eval(input("How many items would you like to pop?: "))
    print(f.pop_lst(n))

elif choice_2 == 'first':
    print (f.pop())

print (f.peek())
print (f.empty())

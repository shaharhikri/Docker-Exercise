# fibonacci sequence index starts from 1 (not from 0!).
def print_fib(index: int):
    if index<1:
        return
    print(1, end=' ')
    if index==1:
        return
    print(1, end=' ')
    if index==2:
        return
    
    a1 = 1
    a2 = 1
    a3 = a2+a1
    print(a3, end=' ')
    for _ in range(4,index+1):
        a1 = a2
        a2 = a3
        a3 = a2+a1
        print(a3, end=' ')
    
    return

if __name__ == "__main__":
    print('My container is online!\nThe first 50 members of the Fibonacci sequence:',end = ' ')
    print_fib(50)
    print()
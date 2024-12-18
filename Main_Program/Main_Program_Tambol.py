import os
from datetime import datetime
import sys
sys.setrecursionlimit(8000)

def clearScreen ():
    os.system('cls')
    return

def getMainMenu():

    #clearScreen()
    print(f'========================')
    print(f'        Main MENU       ')
    print(f'========================')
    print(f' 1. Bubble Sort      <b>')
    print(f' 2. Insertion Sort   <i>')
    print(f' 4. Merge Sort       <m>')
    print(f' 3. Selection Sort   <s>')
    print(f' 5. Quick Sort       <q>')
    print(f' 6. Exit             <x>')
    print(f'========================')
    
    chList = ['b', 'i', 'm', 's', 'q', 'x']
    ch = input ('\nSelect <b, i, m, s, q, x> = ')
    while (ch not in chList):
        ch = input ('\nPlease Select <b, i, m, s, q, x> = ')
    
    return ch
    
def BubbleSort():

    with open("a_list.txt", "r", encoding="utf-8") as file:
        a_list = file.readlines()

    #for i in range(0, 10):
    #    print(f"before = {a_list[i]}")

    xstart = datetime.now()
    swap = 0
    n = len(a_list)
    for k in range(1, n):
        flag = 0
        for i in range(0, n - k):
            if a_list[i] > a_list[i+1]:
                swap += 1
                tmp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = tmp
                flag = 1
                if flag == 0:
                    break

    xend = datetime.now()    
    xdiff = xend - xstart
    ms = xdiff.total_seconds() * 1000
    print(f"Total Swapped = {swap}")
    print(f"Bubble Sort | Total used time {ms} milliseconds")

    #for i in range(0, 10):
    #    print(a_list[i])

    ch = input ('\nPress any key : ')

    return ms

def SelectionSort():

    with open("a_list.txt", "r", encoding="utf-8") as file:
        a_list = file.readlines()

    xstart = datetime.now()
    n = len(a_list)

    for i in range(0, n-1):
        iMin = i

        for j in range(i+1, n):
            if a_list[j] < a_list[iMin]:
                iMin = j

            temp = a_list[i]
            a_list[i] = a_list[iMin]
            a_list[iMin] = temp

    xend = datetime.now()    
    xdiff = xend - xstart
    ms = xdiff.total_seconds() * 1000
    print(f"Selection Sort | Total used time {ms} milliseconds")
    ch = input ('\nPress any key : ')
    return ms
    
def InsertionSort():

    with open("a_list.txt", "r", encoding="utf-8") as file:
        a_list = file.readlines()

    xstart = datetime.now()
    n = len(a_list)

    for i in range(1, n):

        temp = a_list[i]
        hole = i

        while hole > 0 and a_list[hole-1] > temp:
            a_list[hole] = a_list[hole-1]
            hole = hole-1

        a_list[hole] = temp

        xend = datetime.now()    
    xdiff = xend - xstart
    ms = xdiff.total_seconds() * 1000
    print(f"Selection Sort | Total used time {ms} milliseconds")
    ch = input ('\nPress any key : ')
    return ms

def MergeSort():

    with open("a_list.txt", "r", encoding="utf-8") as file:
        a_list = file.readlines()
    
    xstart = datetime.now()
    n = len(a_list)

    if n < 2:
        return a_list

    mid = n // 2
    left = a_list[:mid]
    right = a_list[mid:]

    MergeSort(left)
    MergeSort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a_list[k] = left[i]
            i = i + 1
        else:
            a_list[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        a_list[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        a_list[k] = right[j]
        j = j + 1
        k = k + 1

    xend = datetime.now()    
    xdiff = xend - xstart
    ms = xdiff.total_seconds() * 1000
    print(f"Merge Sort | Total used time {ms} milliseconds")
    ch = input ('\nPress any key : ')

    return ms

def QuickSort(a_list, start, end):
    n = len(a_list)

    if start < end:
        pIndex = QuickSort_partition(a_list, start, end)

        QuickSort(a_list, start, pIndex-1)
        QuickSort(a_list, pIndex+1, end)

    return a_list

def QuickSort_partition(a_list, start, end):
    pIndex = start
    # select last pos as index
    pivot = a_list[end]

    # push less value to the left
    for i in range(start, end):
        if a_list[i] <= pivot:
            temp = a_list[i]
            a_list[i] = a_list[pIndex]
            a_list[pIndex] = temp
            pIndex = pIndex + 1
    temp = a_list[pIndex]
    a_list[pIndex] = a_list[end]
    a_list[end] = temp

    return pIndex

def QuickSort_Main():
    with open("a_list.txt", "r", encoding="utf-8") as file:
        a_list = file.readlines()
    
    xstart = datetime.now()

    QuickSort(a_list, 0, len(a_list)-1)

    xend = datetime.now()    
    xdiff = xend - xstart
    ms = xdiff.total_seconds() * 1000
    print(f"Quick Sort | Total used time {ms} milliseconds")
    ch = input ('\nPress any key : ')

if __name__ == "__main__":

    iMain = getMainMenu()
    while (iMain != 'x'):
        if iMain == 'b':
            ms = BubbleSort()
        elif iMain == 's':
            ms = SelectionSort()
        elif iMain == 'i':
            ms = InsertionSort()
        elif iMain == 'm':
            ms = InsertionSort()
        elif iMain == 'q':
            ms = QuickSort_Main()    

        iMain = getMainMenu()

    input('\nShutdown')
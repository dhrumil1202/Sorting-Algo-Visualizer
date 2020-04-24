import time as t

def bubblesort(data,getData,timetick):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if(data[j]>data[j+1]):
                data[j],data[j+1]=data[j+1],data[j]
                colorarray=[]
                for x in range(len(data)):
                    if(x==j):
                        colorarray.append('green')
                    elif(x==j+1):
                        colorarray.append('blue')
                    elif (x>=len(data)-i):
                        colorarray.append('green')
                    else:
                        colorarray.append('red')
                getData(data,colorarray)
                t.sleep(timetick)
    getData(data,['green' for x in range(len(data))])

def selectionsort(data,getData,timetick):
    for i in range(len(data)):
        min=i
        for j in range(i+1,len(data)):
            if data[min]>data[j]:
                min=j
            colorarray = []
            for x in range(len(data)):
                if (x<i):
                    colorarray.append('green')
                elif(x==min):
                    colorarray.append('blue')
                elif(x==j):
                    colorarray.append('green')
                else:
                    colorarray.append('red')
            getData(data,colorarray)
            t.sleep(timetick)
        if(min!=i):
            data[min],data[i]=data[i],data[min]
    getData(data,['green' for x in range(len(data))])

def Insertionsort(data, getData, timetick):

    for i in range(1, len(data)):
        colorarray=[]
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            colorarray.clear()
            for x in range(len(data)):
                if(x==j):
                    colorarray.append('blue')
                elif(x<=i):
                    colorarray.append('green')
                else:
                    colorarray.append('red')
            getData(data,colorarray)
            t.sleep(timetick)
        data[j + 1] = key
        colorarray=[]
        for x in range(len(data)):
            if (x <= i):
                colorarray.append('green')
            else:
                colorarray.append('red')
        getData(data,colorarray)
    getData(data,['green' for x in range(len(data))])


def partition(arr, low, high,data,n,getData,timetick):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        colorarray = []
        for x in range(n):
            if x==j:
                colorarray.append('cyan')
            elif x==arr.index(pivot):
                colorarray.append('blue')
            elif x<low:
                colorarray.append('green')
            else:
                colorarray.append('red')
        getData(data,colorarray)
        t.sleep(timetick)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    colorarray=[]
    for x in range(n):
        if x<i+1:
            colorarray.append('green')
        else:
            colorarray.append('red')
    getData(data,colorarray)
    return (i + 1)


def quickSort(arr, low, high,getData,timetick):
    if low < high:
        pi = partition(arr, low, high,arr,len(arr),getData,timetick)
        quickSort(arr, low, pi - 1,getData,timetick)
        quickSort(arr, pi + 1, high,getData,timetick)
    getData(arr,['green'for x in range(len(arr))])

def mergeSort(arr,n,data,getData,timetick):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L,n,data,getData,timetick)
        mergeSort(R,n,data,getData,timetick)
        i = j = k = 0
        check=False
        check2=False
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                check=True
                i += 1
            else:
                arr[k] = R[j]
                check2=True
                j += 1
            k += 1
            colorarray=[]
            for x in range(n):
                if x==i and check2==True:
                    check2=False
                    colorarray.append('blue')
                elif x==j and check==True:
                    check=False
                    colorarray.append('blue')
                elif x==k:
                    colorarray.append('green')
                else:
                    colorarray.append('red')
            getData(data,colorarray)
            t.sleep(timetick)

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            colorarray=[]
            for x in range(n):
                if x==i:
                    colorarray.append('cyan')
                elif x==k:
                    colorarray.append('green')
                else:
                    colorarray.append('red')
            getData(data,colorarray)
            t.sleep(timetick)


        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            colorarray = []
            for x in range(n):
                if x == j:
                    colorarray.append('cyan')
                elif x == k:
                    colorarray.append('green')
                else:
                    colorarray.append('red')
            getData(data, colorarray)
            t.sleep(timetick)
        getData(data, ['green' for x in range(n)])
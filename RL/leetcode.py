import sys



def getWinner(arr, k: int) -> int:

    for i in range(0, len(arr)):

        if i == len(arr) -1:
            return arr[i]
        
        temp_List = []
        for x in arr:
            temp_List.append(x)

        counter = k

        for j in range(1, len(arr)):

            if counter == 0:
                return arr[0]

            if arr[0] >= arr[1]:
                counter = counter - 1
                print(counter)
                if counter == 0:
                    return arr[0]

                if j == len(arr) - 1:
                    return arr[0]

                for x in range(1, len(arr)):
                    if x == len(arr) - 1:
                        arr[x] = temp_List[1]

                    else:
                        arr[x] = temp_List[x + 1]


            else:
                for x in range(0, len(arr)):
                    if x == len(arr) - 1:
                        arr[x] = temp_List[0]
                    else:
                        arr[x] = temp_List[x + 1]

                if (counter - 1) == 0:
                    return arr[0]

                break

    return 0

getWinner([2,1,3,5,4,6,7], 2)
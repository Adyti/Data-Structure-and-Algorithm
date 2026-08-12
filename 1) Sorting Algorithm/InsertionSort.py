class InsertionSort:
    def sort(self, arr):

        for i in range (1, len(arr)):
            curr = arr[i] 
            prev = i - 1

            while prev >= 0 and arr[prev] > curr:
                arr[prev + 1] = arr[prev]
                prev = prev - 1

                #Put curr value at its correct position
                arr[prev + 1] = curr

        return arr

arr = [4, 1, 5, 2, 3]

insertion_sort = InsertionSort()
print(insertion_sort.sort(arr))

#Best Case: O(n)
#Average Case: O(n²)
#Worst Case: O(n²)
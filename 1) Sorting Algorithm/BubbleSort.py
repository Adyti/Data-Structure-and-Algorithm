class BubbleSort:
    def sort(self, arr):

        n = len(arr)

        for i in range (n - 1):
            for j in range (n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

arr = [5, 3, 8, 4, 2]

bubble_sort = BubbleSort()
print(bubble_sort.sort(arr))

#Best Case: O(n²)
#Average Case: O(n²)
#Worst Case: O(n²)
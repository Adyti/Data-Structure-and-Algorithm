class BubbleSort_Optimized:
    def sort(self, arr):

        n = len(arr)

        for i in range (n - 1):
            swapped = False

            for j in range (n - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if swapped == False:
                break

        return arr

arr = [2, 3, 5, 6, 8, 9]

bubblesort_optimized = BubbleSort_Optimized()
print(bubblesort_optimized.sort(arr))

#Best Case: O(n)
#Average Case: O(n²)
#Worst Case: O(n²)
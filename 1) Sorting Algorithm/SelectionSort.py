class SelectionSort:
    def sort(self, arr):

        n = len(arr)

        for i in range (n - 1):
            min_idx = i

            for j in range (i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr

arr = [2, 6, 4, 1, 9, 3]

selection_sort = SelectionSort()
print(selection_sort.sort(arr))

#Best Case: O(n²)
#Average Case: O(n²)
#Worst Case: O(n²)
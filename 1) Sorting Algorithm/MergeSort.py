class MergeSort:
    def sort(self, arr):

        # Base case
        if len(arr) <= 1:
            return arr

        # Divide
        mid = len(arr) // 2

        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])

        # Merge
        result = []
        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])

        return result


arr = [12, 31, 35, 8, 32, 17]

merge_sort = MergeSort()

print(merge_sort.sort(arr))


# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n log n)
# Space Complexity: O(n)
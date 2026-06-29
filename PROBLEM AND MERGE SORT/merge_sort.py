def mergeSort(self, arr):

        self.divide(arr, 0, len(arr) - 1)

        return arr


def divide(self, arr, left, right):

        # Base Case
        if left >= right:
            return

        mid = (left + right) // 2

        # Sort left half
        self.divide(arr, left, mid)

        # Sort right half
        self.divide(arr, mid + 1, right)

        # Merge both halves
        self.merge(arr, left, mid, right)


def merge(self, arr, left, mid, right):

        temp = []

        i = left
        j = mid + 1

        while i <= mid and j <= right:

            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[left + k] = temp[k]
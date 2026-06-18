class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idn, n in enumerate(numbers):

            arr = numbers[idn + 1:]

            sup_i = idn + 1
            while arr != []:
                mid = arr[int(len(arr)/2)]
                if mid == target - n:
                    return [idn + 1, sup_i + 1 + int(len(arr)/2)]
                elif mid < target - n:
                    sup_i += int(len(arr)/2) + 1
                    arr = arr[int(len(arr)/2) + 1:]
                else:
                    arr = arr[:int(len(arr)/2)]

        
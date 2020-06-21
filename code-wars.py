#  Your task is to find the first element of an array that is not consecutive.
#  If the whole array is consecutive then return null

def first_non_consecutive(arr):
    for i, v in enumerate(arr, arr[0]):
        if v != i:
            return v




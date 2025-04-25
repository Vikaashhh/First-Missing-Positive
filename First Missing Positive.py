#User function Template for python3

class Solution:

    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Ignore negative numbers and numbers greater than n
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = 0

        # Step 2: Mark existing numbers by index
        for i in range(n):
            val = abs(arr[i])
            if 1 <= val <= n:
                if arr[val - 1] > 0:
                    arr[val - 1] *= -1
                elif arr[val - 1] == 0:
                    arr[val - 1] = -1 * (n + 1)

        # Step 3: First index with positive value is the missing number
        for i in range(n):
            if arr[i] >= 0:
                return i + 1  # 1-based indexing

        # Agar sab numbers 1 se n tak present hain, toh answer is n+1
        return n + 1
    
if __name__ == "__main__":
    arr = [0, -10, 1, 3, -20]
    obj = Solution()
    print("Smallest positive missing number is:", obj.missingNumber(arr))
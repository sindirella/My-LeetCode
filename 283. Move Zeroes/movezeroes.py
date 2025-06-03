class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) #inisialisasi panjang nums
        temp = [0] * n #temporary array, membuat list baru bernama temp yang berisi n buah elemen yang diganti dengan angka 0
        j = 0 #awal dari indeks posisi yang sedang/akan diisi

        for i in range(n):
            if nums[i] != 0: #jika dalam nums[i] tidak sama dengan 0 maka
                temp[j] = nums[i] #setiap kali ditemukan angka selain 0 maka nums[i] akan disalin ke temp[j]
                j += 1 #j akan terisi ke index berikutnya
        while j < n: #loop akan terus berjalan jika nilai j kurang dari n 
            temp[j] = 0 # setiap iterasi, nilai di indeks ke-j dari list temp di-set atau diubah menjadi 0
            j += 1

        for i in range (n):
            nums[i] = temp[i]
        
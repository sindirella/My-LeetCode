class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 #index valid m akhir di num1
        j = n - 1 #index valid n akhir di num2
        k = m + n - 1 #index valid m + n akhir di num1, digunakan untuk menggabungkan keduanya
        while j >= 0: #jika nilai j lebih besar sama dengan 0 maka lanjut mengisi nums1
            if i >=0 and nums1[i] > nums2[j]:#jika i lebih besar atau sama dengan 0 dan nums1 lebih besar dari nums2 maka
                nums1[k] = nums1[i]#letakkan nums1[i] ke nums1[k] (sebagai tempat merge)
                i -= 1#kurangi elemen i dan pindah ke posisi elemen sebelumnya
            else: #jika tidak, maka nums2 lebih besar dari nums1 yang artinya list di nums 1 sudah habis
                nums1[k] = nums2[j]#letakkan nums[j] ke dalam nums[k]
                j -= 1#kurangi elemmen j dan pindah ke posisi elemen sebelumnya 
            k -= 1#setiap mengisi nilai nums[k] maka geser k ke kiri posisi elemen sebelumnya

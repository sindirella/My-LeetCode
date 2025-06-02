class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = [] #hasil akan dimasukkan ke dalam list
        for i in range(1, n + 1): #perulangan inklusif pada i hingga nilai n
            if i % 15 == 0: # apabila i habis dibagi dengan 3 dan 5
                result.append("FizzBuzz") #maka tampilkan FizzBuzz
            elif i % 3 == 0: # namun, jika i habis dibagi 3
                result.append("Fizz") #maka tampilkan Fizz
            elif i % 5 == 0: # jika i habis dibagi 5
                result.append("Buzz") #maka tampilkan Buzz
            else:
                result.append(str(i)) #jika tidak ada yang habis dibagi 3 dan 5 atau kondisi di atas tidak terpenuhi maka tampilkan angka asli dalam bentuk string
        return result
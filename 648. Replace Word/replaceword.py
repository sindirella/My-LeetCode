class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dict_set = set(dictionary) #daftar dari dictionary yang sudah ada
        def replace(word):
            for i in range(1, len(word) + 1):# perulangan, mencoba semua kata yang cocok pada dictionary
                if word[:i] in dict_set:#apabila kata yang ada pada sentence memeiliki kecocokan dengan dictionary
                    return word[:i]#mengganti kata dengan dictionary yang cocok
            return word#kembali menggunakan kata aslinya apabila tidak ada kecocokan dengan dictionary
        return ' '.join(replace(word) for word in sentence.split()) #fungsi split untuk memecah string, menjadi pecahan kata dalam list
    #mengganti dan menggabungkan semua kata yang cocok, menghapus semua kalimat dipisahkan oleh spasi
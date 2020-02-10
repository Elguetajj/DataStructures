class topchars:

    @staticmethod
    def countchars(text):
        letters:dict = {}
        for char in str(text).upper().replace(' ',''):
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        sorted_letters = sorted(letters.items(), key=lambda kv: kv[1])
        
        return(sorted_letters[-10:])

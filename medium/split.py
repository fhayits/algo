def split(word):
        result = []
        n = len(word)
        pos = 0
        start_pos = 0
       
        while pos < n:
        
            while pos < n and word[pos] == " ":
                pos += 1
            
            if pos >= n:
                break
            start_pos = pos   

            while pos < n and word[pos] != " ":
                pos += 1
            result.append(word[start_pos:pos])
        
        return result
print(split("salom qalaysan   fjhsdagbf  fdshjkagfhsdk   hgfdjkslhg df            fkhhgdfskjgfd      "))

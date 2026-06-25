def checkIfPangram(self, sentence):
        s=set()
        for ch in sentence:
            s.add(ch)
        if len(s)==26:
            return True
        else:
            return False        
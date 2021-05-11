class wow:

    def __init__(self,txt,name):
        self.txt=txt
        self.n=name

    def bad_chim_name(n):
        return "는" if (ord(n[-1])-44032)%28==0 else "이는"

    def bad_chim_txt(n):
        return "라고" if (ord(n[-1])-44032)%28==0 else "이라고"

    def speak(self):
        print(self.n+wow.bad_chim_name(self.n),self.txt+wow.bad_chim_txt(self.txt),"말했습니다. ")


n1 = wow("안녕","도하")
n2 = wow("하이","도하")
n3 = wow("안녕","민식")
n4 = wow("하이","민식")
n1.speak()
n2.speak()
n3.speak()
n4.speak()





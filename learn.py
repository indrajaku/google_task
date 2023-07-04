class function :
    def __init__(self,name,per):
        self.name = name
        self.per = per

    def fev(self):
        print("my fev is :",self.name,self.per)


func = function("muskan",100)
func_1 = function("chandu",100)
func_2 = function("raksha",100)
func.fev()
func_1.fev()
func_2.fev()
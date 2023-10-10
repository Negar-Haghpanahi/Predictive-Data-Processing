

class DictConverter():

    def __init__(self) -> None:
        
        self.request_dict =None

    def __iter__(self ):
        
        for key in self.__dict__:
            yield (key ,'value {}'.format(key))  




if __name__ =="__main__":

    x =[1 , 3 , 7]

    obj = DictConverter()
    obj.request_dict=x
    print(obj.__dict__)




    



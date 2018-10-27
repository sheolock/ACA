class Register(object):
    def __init__(self, amount=32, bit=32, content=0):
        self.__r = []
        self.__bit = bit
        while len(self.__r) < amount:
            self.__r.append(content)

    # def load(self, no):
    #     if no < len(self.__r):
    #         return self.__r[no]
    #     else:
    #         print("The register" + str(no) + "is not exist!\n")
    #         return -1
    #
    # def save(self, no, content):
    #     if no < len(self.__r):
    #         self.__r[no] = (content % (2 ** self.__bit))
    #     else:
    #         print("The register" + str(no) + "is not exist!\n")
    #     return
    '''
        function:
            save content to register

        input:
            _no:    string or int, the number you want to load
            _content:the content you want to store
            mode:   save mode, 
                    0:  unsigned int
                    1:  signed int

        output:
            null
        '''

    def save(self, _no=0, _content=0, mode=0):
        no = int(_no)
        content = int(_content)
        result = ""
        if no < len(self.__r):
            if mode == 0:
                for i in range(self.__bit):
                    result = str(content % 2) + result
                    content = content // 2
                self.__r[no] = str(result)
            elif mode == 1:
                content = content % (2 ** self.__bit)
                if content < 0:
                    self.__r[no] = bin(~int(bin(content ^ (2 ** self.__bit - 1)), 2))[3:]
                else:
                    self.__r[no] = bin(content)[2:]
        else:
            print("The register" + str(no) + "is not exist!\n")
        return

    '''
        function:
            load register content
            
        input:
            _no:    string or int, the number you want to load
            _pos:   string or int, the bit that starts loading
            _size:  string or int, range 0~self.__bit, the number of bits you want to read
            mode:   load mode, 
                    0:  unsigned int
                    1:  signed int
                    2:  binary
                    
        output:
            result: null with errors or the content you wanted
    '''

    def load(self, _no=0, _pos=0, _size=32, mode=0):
        no = int(_no)
        pos = int(_pos)
        size = int(_size)
        if pos + size > self.__bit:
            print("overloading\n")
            return
        if no < len(self.__r):
            if mode == 0:
                return int(str(self.__r[no]), 2)
            elif mode == 1:
                if self.__r[no][0:1] == 0:
                    return int(str(self.__r[no]), 2)
                else:
                    return 0 - int(self.__r[no][1:], 2)
            elif mode == 2:
                return self.__r[no][pos:pos + size]
            else:
                print("load mode " + str(mode) + " error")
                return
        else:
            print("The register" + str(no) + "is not exist!\n")
            return

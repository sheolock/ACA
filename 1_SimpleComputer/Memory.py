class Memory(object):
    def __init__(self, addr_bit=32, cell_bit=8, content="01010101", split_bit=28):
        self.m = []
        self.addr_bit = addr_bit
        self.cell_bit = cell_bit
        self.split_bit = split_bit

        # while len(self.m) < (2 ** addr_bit):
        #     self.m.append(content)

        for i in range((2 ** addr_bit) // (2 ** split_bit)):
            temp1 = []
            for j in range(2 ** split_bit):
                temp1.append(content)
            self.m.append(temp1)
        temp2 = []
        for i in range((2 ** addr_bit) % (2 ** split_bit)):
            temp2.append(content)
        self.m.append(temp2)

    # def load(self, addr, mode=0):
    #     if addr < len(self.m):
    #         if mode == 0:
    #             return self.m[addr // (2 ** self.split_bit)][addr % (2 ** self.split_bit)]
    #         elif mode == 1:
    #             return self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4] + \
    #                    self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 1] * (2 ** 4) + \
    #                    self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 2] * (2 ** 8) + \
    #                    self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 3] * (
    #                            2 ** 12)
    #     else:
    #         print("The memory is out of range!\n")
    #         return -1

    # def save(self, addr, content, mode=0):
    #     if addr < len(self.m):
    #         if mode == 0:
    #             self.m[addr // (2 ** self.split_bit)][addr % (2 ** self.split_bit)] = (content % (2 ** self.cell_bit))
    #         elif mode == 1:
    #             self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4] = content % (2 ** 4)
    #             self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 1] = (content // (
    #                     2 ** 4)) % (2 ** 4)
    #             self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 2] = (content // (
    #                     2 ** 8)) % (2 ** 4)
    #             self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 3] = (content // (
    #                     2 ** 12)) % (2 ** 4)
    #     else:
    #         print("The memory is out of range!\n")
    #     return

    '''
        function:
            save content to memory

        input:
            _addr:  string or int, the address of memory you want to store contents
            _content:the content you want to store
            mode:   save mode, 
                    0:  content is 8-bit signed int
                    1:  content is 32-bit signed int

        output:
            null
    '''

    def save(self, _addr=0, _content=0, mode=0):
        content = int(_content)
        addr = int(_addr)
        if addr < len(self.m):
            if mode == 0:
                if content > 0:
                    self.m[addr // (2 ** self.split_bit)][addr % (2 ** self.split_bit)] = bin(
                        int(bin(content ^ (2 ** 8)), 2))[3:]
                else:
                    self.m[addr // (2 ** self.split_bit)][addr % (2 ** self.split_bit)] = bin(
                        ~int(bin(content ^ (2 ** 8 - 1)), 2))[3:]
            elif mode == 1:
                if content > 0:
                    result = bin(int(bin(content ^ (2 ** 32)), 2))[3:]
                else:
                    result = bin(~int(bin(content ^ (2 ** 32 - 1)), 2))[3:]
                self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4] = result[24:]
                self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 1] = result[16:24]
                self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 2] = result[8:16]
                self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 3] = result[:8]
        else:
            print("The memory is out of range!\n")
        return

    '''
        function:
            load memory content
    
        input:
            _addr:  string or int, the number you want to load
            mode:   load mode, 
                    0:  unsigned 8-bit int
                    1:  signed 8-bit int
                    2:  unsigned 32-bit int
                    3:  signed 32-bit int                    
                    4:  binary
    
        output:
            result: null with errors or the content you wanted, int with mode 0~3 and binary string with mode 4
    '''

    def load(self, _addr=0, mode=0):
        addr = int(_addr)
        if addr < len(self.m):
            if mode == 0:
                return int(self.m[addr // (2 ** self.split_bit)][addr % (2 ** self.split_bit)], 2)
            elif mode == 1:
                result = self.m[addr // (2 ** self.split_bit)][addr % (2 ** self.split_bit)]
                if result[0] == "0":
                    return int(result[1:], 2)
                else:
                    return 0 - int(bin(~int(bin(int(result[1:], 2) ^ (2 ** 8 - 1)), 2))[3:], 2)
            elif mode == 2:
                result = self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 3] + \
                         self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 2] + \
                         self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 1] + \
                         self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 0]
                return int(result, 2)
            elif mode == 3:
                result = self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 3] + \
                         self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 2] + \
                         self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 1] + \
                         self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 0]
                if result[0] == "0":
                    return int(result[1:], 2)
                else:
                    return 0 - int(bin(~int(bin(int(result[1:], 2) ^ (2 ** 8 - 1)), 2))[3:], 2)
            elif mode == 4:
                return self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 3] + \
                       self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 2] + \
                       self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 1] + \
                       self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 0]
        else:
            print("The memory is out of range!\n")
            return

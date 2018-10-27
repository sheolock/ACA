class Memory(object):
    def __init__(self, addr_bit=32, cell_bit=8, content=1, split_bit=24):
        self.addr_bit = addr_bit
        self.cell_bit = cell_bit
        self.split_bit = split_bit
        for i in range((2 ** addr_bit) // (2 ** split_bit)):
            temp1 = []
            for j in range(2 ** split_bit):
                temp1.append(content)
            with open("mem_" + str(i) + ".txt", "w+") as f:
                for mem_cell in temp1:
                    f.write(str(mem_cell) + "\n")
        temp2 = []
        for i in range((2 ** addr_bit) % (2 ** split_bit)):
            temp2.append(content)
        with open("mem_" + str((2 ** addr_bit) // (2 ** split_bit)) + ".txt", "w+") as f:
            for mem_cell in temp2:
                f.write(str(mem_cell) + "\n")
        print("memory init completed")

    def load(self, addr, mode=0):
        if addr < (2 ** self.addr_bit):
            if mode == 0:
                f = open("mem_" + str(addr // (2 ** self.split_bit)) + ".txt")
                contents = f.readlines()
                f.close()
                return contents[addr % (2 ** self.split_bit)]
            elif mode == 1:
                f = open("mem_" + str(addr // (2 ** self.split_bit)) + ".txt")
                contents = f.readlines()
                f.close()
                return contents[((addr % (2 ** self.split_bit)) // 4) * 4] + \
                       contents[((addr % (2 ** self.split_bit)) // 4) * 4 + 1] * (2 ** 4) + \
                       contents[((addr % (2 ** self.split_bit)) // 4) * 4 + 2] * (2 ** 8) + \
                       contents[((addr % (2 ** self.split_bit)) // 4) * 4 + 3] * (2 ** 12)
        else:
            print("The memory is out of range!\n")
            return -1

    def save(self, addr, content, mode=0):
        if addr < (2 ** self.addr_bit):
            if mode == 0:
                f = open("mem_" + str(addr // (2 ** self.split_bit)) + ".txt", "w+")
                contents = f.readlines()
                contents[addr % (2 ** self.split_bit)] = (content % (2 ** self.cell_bit))
                for items in contents:
                    f.write(str(items) + "\n")
                f.close()
            elif mode == 1:
                f = open("mem_" + str(addr // (2 ** self.split_bit)) + ".txt", "w+")
                contents = f.readlines()
                contents[((addr % (2 ** self.split_bit)) // 4) * 4] = content % (2 ** 4)
                contents[((addr % (2 ** self.split_bit)) // 4) * 4 + 1] = (content // (2 ** 4)) % (2 ** 4)
                contents[((addr % (2 ** self.split_bit)) // 4) * 4 + 2] = (content // (2 ** 8)) % (2 ** 4)
                contents[((addr % (2 ** self.split_bit)) // 4) * 4 + 3] = (content // (2 ** 12)) % (2 ** 4)
                for items in contents:
                    f.write(str(items) + "\n")
                f.close()
        else:
            print("The memory is out of range!\n")
        return

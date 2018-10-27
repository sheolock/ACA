class Memory(object):
    def __init__(self, addr_bit=32, cell_bit=8, content=1, split_bit=28):
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

    def load(self, addr, mode=0):
        if addr < len(self.m):
            if mode == 0:
                return self.m[addr // (2 ** self.split_bit)][addr % (2 ** self.split_bit)]
            elif mode == 1:
                return self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4] + \
                       self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 1] * (2 ** 4) + \
                       self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 2] * (2 ** 8) + \
                       self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 3] * (
                               2 ** 12)
        else:
            print("The memory is out of range!\n")
            return -1

    def save(self, addr, content, mode=0):
        if addr < len(self.m):
            if mode == 0:
                self.m[addr // (2 ** self.split_bit)][addr % (2 ** self.split_bit)] = (content % (2 ** self.cell_bit))
            elif mode == 1:
                self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4] = content % (2 ** 4)
                self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 1] = (content // (
                        2 ** 4)) % (2 ** 4)
                self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 2] = (content // (
                        2 ** 8)) % (2 ** 4)
                self.m[addr // (2 ** self.split_bit)][((addr % (2 ** self.split_bit)) // 4) * 4 + 3] = (content // (
                        2 ** 12)) % (2 ** 4)
        else:
            print("The memory is out of range!\n")
        return

class Register(object):
    def __init__(self, amount=32, bit=32, content=0):
        self.__r = []
        self.__bit = bit
        while len(self.__r) < amount:
            self.__r.append(content)

    def load(self, no):
        if no < len(self.__r):
            return self.__r[no]
        else:
            print("The register" + str(no) + "is not exist!\n")
            return -1

    def save(self, no, content):
        if no < len(self.__r):
            self.__r[no] = (content % (2 ** self.__bit))
        else:
            print("The register" + str(no) + "is not exist!\n")
        return

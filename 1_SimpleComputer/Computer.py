import Register
import Memory_file


class Computer(object):
    def __init__(self):
        self.register = Register.Register()
        self.reg_pc = Register.Register(amount=1, content=0)
        self.memory = Memory_file.Memory()
        self.start()

    def instruction_decode(self, ins):
        operand = ""
        dist = ""
        source_1 = ""
        source_2 = ""
        decode = ins.lower().strip().split()
        op = decode[0]
        # splite the instruction
        if len(decode) == 1:
            pass
        elif len(decode) == 2:
            operand = decode[1].split(",")
            if len(operand) == 1:
                dist = operand[0]
            elif len(operand) == 2:
                dist = operand[0]
                source_1 = operand[1]
            elif len(operand) == 3:
                dist = operand[0]
                source_1 = operand[1]
                source_2 = operand[2]
            else:
                print("command operands error\n")
                return
        # get meaning of instruction
        if op == "add":
            if len(operand) < 3:
                print("command operands error\n")
            else:
                self._save(
                    dist, self.add(self._load(source_1), self._load(source_2)))
        elif op == "load":
            if len(operand) < 2:
                print("command operands error\n")
            else:
                self.load(dist, source_1)
        elif op == "store":
            if len(operand) < 2:
                print("command operands error\n")
            else:
                self.save(source_1, dist)
        elif op == "l":
            for reg in self.register.__r:
                print(reg, end=" ")
            print()

        return

    '''
    Unconditional jump instruction
    
    input:  jal rd,label
    rd:     general register, such as r1
    label:  the row you want to jump
    
    output:
    rd:     PC register's content +1
    pc:     label
    '''

    def jal(self, rd, label):
        self._save(rd, (self.reg_pc.load(0) + 1))
        self.reg_pc.save(0, label)
        return

    '''
    Unconditional jump instruction

    input:  jal rd,label
    rd:     general register, such as r1
    rs1:    general register, such as r1
    imm:    

    output:
    rd:     PC register's content +1
    pc:     rs1+imm
    '''
    def jalr(self, rd, rs1, imm):
        self._save(rd, (self.reg_pc.load(0) + 1))
        self.reg_pc.save(0, (int(self._load(rs1)) + int(imm)))
        return

    '''
    Conditional jump instruction

    input:  jal rd,label
    rd:     general register, such as r1
    rs1:    general register, such as r1
    imm:    

    output:
    rd:PC register's content +1
    '''
    def beq(self, rs1, rs2, label):
        pass

    def bne(self, rs1, rs2, label):
        pass

    def blt(self, rs1, rs2, label):
        pass

    def bltu(self, rs1, rs2, label):
        pass

    def bge(self, rs1, rs2, label):
        pass

    def bgeu(self, rs1, rs2, label):
        pass

    def lw(self,rd,rs1):
        pass

    def lh(self,rd,rs1):
        pass

    def lhu(self,rd,rs1):
        pass

    def lb(self,rd,rs1):
        pass

    def lbu(self,rd,rs1):
        pass

    def sw(self,rd,rs1):
        pass

    def sh(self,rd,rs1):
        pass

    def sb(self,rd,rs1):
        pass

    def _load(self, _operand):
        operand = str(_operand)
        num = operand[1:]
        if operand[0] == "r" and num.isdigit():
            return self.register.load(int(num))
        elif operand[0] == "#" and num.isdigit():
            return self.memory.load(int(num))
        else:
            print("load error\n")
            return

    def _save(self, _operand, _content):
        operand = str(_operand)
        content = str(_content)
        num = operand[1:]
        if operand[0] == "r" and num.isdigit() and content.isdigit():
            return self.register.save(int(num), int(content))
        elif operand[0] == "#" and num.isdigit() and content.isdigit():
            return self.memory.save(int(num), int(content))
        else:
            print("save error\n")
            return

    def add(self, a, b):
        return a + b

    def load(self, dist, source):
        self._save(dist, self._load(source))

    def save(self, source, dist):
        self._save(dist, self._load(source))

    def instruction_fetch(self):
        return input(">")

    def start(self):
        # while True:
        #     self.instruction_decode(self.instruction_fetch())

        inst = self.instruction_fetch()
        prg = []
        while inst != "":
            prg.append(inst)
            inst = self.instruction_fetch()

        while self.reg_pc.load(0) < len(prg):
            self.instruction_decode(prg[self.reg_pc.load(0)])
        # for i in prg:
        #    self.instruction_decode(i)


if __name__ == "__main__":
    computer = Computer()
    computer.start()

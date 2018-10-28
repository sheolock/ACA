import Register
import Memory


class Computer(object):
    def __init__(self):
        self.register = Register.Register()
        self.reg_pc = Register.Register(amount=1, content=0)
        self.memory = Memory.Memory()
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
        
        input:  
            jal rd,label
            rd:     general register, such as r1
            label:  the row you want to jump
        
        output:
            rd:     PC register's content +1
            pc:     label
    '''

    def jal(self, rd, label):
        self._save(rd, (self.reg_pc.load(0) + 1))
        self.reg_pc.save(0, int(label))
        return

    '''
        Unconditional jump instruction
    
        input:  
            jal rd,label
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
        Conditional jump instruction, to jump when rs1 == rs2
    
        input:  
            beq rs1,rs2,label
            rs1:    general register, such as r1
            rs2:    general register, such as r1
            label:  the row you want to jump
    
        output:
            rd:PC register's content +1
    '''

    def beq(self, rs1, rs2, label):
        if self._load(rs1) == self._load(rs2):
            self.reg_pc.save(0, int(label))
        return

    def bne(self, rs1, rs2, label):
        if self._load(rs1) != self._load(rs2):
            self.reg_pc.save(0, int(label))
        return

    def blt(self, rs1, rs2, label):
        if self._load(_operand=rs1, mode=1) < self._load(_operand=rs2, mode=1):
            self.reg_pc.save(0, int(label))
        return

    def bltu(self, rs1, rs2, label):
        if self._load(_operand=rs1) < self._load(_operand=rs2):
            self.reg_pc.save(0, int(label))
        return

    def bge(self, rs1, rs2, label):
        if self._load(_operand=rs1, mode=1) >= self._load(_operand=rs2, mode=1):
            self.reg_pc.save(0, int(label))
        return

    def bgeu(self, rs1, rs2, label):
        if self._load(_operand=rs1) >= self._load(_operand=rs2):
            self.reg_pc.save(0, int(label))
        return

    def lw(self, rd, rs1):
        self._save(_operand=rd, _content=self._load(_operand=rs1, mode=0), mode=0)
        return

    def lh(self, rd, rs1):
        temp = self._load(_operand=rs1, mode=2, pos=16, size=16)
        if temp[0] == 0:
            self._save(_operand=rd, _content=int(temp, 2), mode=0)
        else:
            self._save(_operand=rd, _content=int(self._load(_operand=rs1, mode=1, pos=16, size=16), 2), mode=0)
        return

    def lhu(self, rd, rs1):
        self._save(_operand=rd, _content=int(self._load(_operand=rs1, mode=2, pos=16, size=16), 2), mode=0)
        return

    def lb(self, rd, rs1):
        temp = self._load(_operand=rs1, mode=2, pos=24, size=8)
        if temp[0] == 0:
            self._save(_operand=rd, _content=int(temp, 2), mode=0)
        else:
            self._save(_operand=rd, _content=int(self._load(_operand=rs1, mode=1, pos=24, size=8), 2), mode=0)
        return

    def lbu(self, rd, rs1):
        self._save(_operand=rd, _content=int(self._load(_operand=rs1, mode=2, pos=24, size=8), 2), mode=0)
        return

    def sw(self, rs2, rs1):
        self._save(_operand=rs1, _content=int(self._load(_operand=rs2)))
        return

    def sh(self, rs2, rs1):
        content = self._load(_operand=rs2, mode=2, pos=16, size=16)
        self._save(_operand=rs1, _content=content, mode=2,pos=16,size=16)
        return

    def sb(self, rs2, rs1):
        content = self._load(_operand=rs2, mode=2, pos=24, size=8)
        self._save(_operand=rs1, _content=content, mode=2, pos=24, size=8)
        return

    def _load(self, _operand, mode=0, pos=0, size=32):
        operand = str(_operand)
        num = operand[1:]
        if operand[0] == "r":
            return self.register.load(_no=int(num), mode=mode, _pos=pos, _size=size)
        elif operand[0] == "#":
            return self.memory.load(_addr=int(num), mode=mode)
        else:
            print("load error\n")
            return

    def _save(self, _operand, _content, mode=0, pos=0, size=32):
        operand = str(_operand)
        content = str(_content)
        num = operand[1:]
        if operand[0] == "r":
            return self.register.save(int(num), content, mode, pos, size)
        elif operand[0] == "#":
            return self.memory.save(int(num), content, mode)
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

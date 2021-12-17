from __future__ import annotations
from typing import List, Tuple
from copy import deepcopy
from math import prod


class Packet:
    def __init__(
        self,
        version: int,
        ptype: int,
        value: int = 0,
        ltype: int = 0,
        sublength: int = 0
    ) -> None:
        self.version = version
        self.ptype = ptype

        # if ptype == 0b100:
        self.value = value

        # else:
        self.ltype = ltype
        self.sublength = sublength
        self.subpackets: List[Packet] = []

    def __repr__(self) -> str:
        s = "version " + str(self.version) + "\n"
        s += "type " + str(self.ptype)

        if self.ptype == 0b100:
            s += " (literal value)\n"
            s += "value " + str(self.value)

        else:
            s += " (operator)\n"
            s += "ltype " + str(self.ltype)
            s += " (bits)\n" if self.ltype == 0 else " (packets)\n"
            s += "sublenght " + str(self.sublength) + "\n"
            s += "subpackets " + str(len(self.subpackets))

            for p in self.subpackets:
                s += "\n-"
                s += "\n".join(["  " + l for l in str(p).split("\n")])

        return s

    def add_subpacket(self, p: Packet):
        if self.ptype == 0b100:
            raise Exception

        self.subpackets.append(deepcopy(p))

    def deep_version(self) -> int:
        v = self.version
        for p in self.subpackets:
            v += p.deep_version()

        return v

    def val(self) -> int:
        # sum
        if self.ptype == 0:
            return sum([p.val() for p in self.subpackets])

        # product
        elif self.ptype == 1:
            return prod([p.val() for p in self.subpackets])

        # min
        elif self.ptype == 2:
            return min([p.val() for p in self.subpackets])

        # max
        elif self.ptype == 3:
            return max([p.val() for p in self.subpackets])

        # literal
        elif self.ptype == 4:
            return self.value

        # greater than
        elif self.ptype == 5:
            if self.subpackets[0].val() > self.subpackets[1].val():
                return 1
            else:
                return 0

        # less than
        elif self.ptype == 6:
            if self.subpackets[0].val() < self.subpackets[1].val():
                return 1
            else:
                return 0
        # equal
        elif self.ptype == 7:
            if self.subpackets[0].val() == self.subpackets[1].val():
                return 1
            else:
                return 0


def parse(bin: str) -> Tuple[Packet, int]:
    version = int(bin[0:3], 2)
    ptype = int(bin[3:6], 2)

    # if the packet is a data packet
    if ptype == 0b100:
        i = 0
        value_str = ""
        while True:
            value_str = value_str + bin[7 + (i * 5): 11 + (i * 5)]
            if bin[6 + (i * 5)] == "0":
                break
            i += 1

        value = int(value_str, 2)
        return (Packet(version, ptype, value=value), 6 + ((i + 1) * 5))

    # if the packet is an operator packet
    else:
        ltype = int(bin[6], 2)
        if ltype == 0:
            # length in bits
            sublength = int(bin[7:22], 2)

            p = Packet(version, ptype, ltype=0, sublength=sublength)

            index = 22
            while index < sublength + 22:
                new_p, sub_len = parse(bin[index:])
                p.add_subpacket(new_p)
                index += sub_len

            length = index

        else:
            # length in packets
            sublength = int(bin[7:18], 2)
            p = Packet(version, ptype, ltype=0, sublength=sublength)

            index = 18
            packets = 0
            while packets < sublength:
                new_p, sub_len = parse(bin[index:])
                p.add_subpacket(new_p)
                index += sub_len
                packets += 1

            length = index

        return (p, length)


hex2bin_table = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex2bin(hex: str) -> str:
    return "".join(list(map(lambda c: hex2bin_table[c], hex)))


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.read().strip()

    bin = hex2bin(data)
    p, _ = parse(bin)
    # print(p)
    print(p.deep_version())
    print(p.val())

class Wire:
    def __init__(self


class Gate:

    def __init__(self, gateType, wire1, wire2):
        self.gateType = gateType
        self.wire1 = wire1
        self.wire2 = wire2

    def solve() {
        if gateType == None:
            return wire2.solve()

        if (gateType == "AND"):
            return wire1.solve() & wire2.solve()
        if (gateType == "OR"):
            return wire1.solve() | wire2.solve()
        if (gateType == "NOT"):
            return ~wire2.solve() & 0xFFFF
        if (gateType == "LSHIFT"):
            return wire1.solve() << wire2.solve()
        if (gateType == "RSHIFT"):
            return wire1.solve() >> wire2.solve()
    

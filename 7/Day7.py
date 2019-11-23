
class Wire:
    def __init__(self, instruction):
        self.instruction = instruction
        self.parse_instruction(instruction)
    
    def parse_instruction(self, instruction):
        parts = instruction.split()
        self.output = parts[-1]

        input = parts[:-2]
        self.op = "SET"  # default operation
        for op in ["AND", "NOT", "OR", "LSHIFT", "RSHIFT"]:
            if op in input:
                self.op = op
                input.remove(op)
        self.inputs = [int(i) if i.isdigit() else i for i in input]  # int input indicates already resolved input

    def reset(self):
        self.parse_instruction(self.instruction)

    def process(self):
#        print("[Wire] input: {} op: {} output: {}".format(self.inputs, self.op, self.output))
        if self.op == "SET":
            return int(self.inputs[0])
        elif self.op == "AND":
            return int(self.inputs[0] & self.inputs[1])
        elif self.op == "NOT":
            # 0b1111'1111'1111'1111 == 65535
            return int(65535 - self.inputs[0])
        elif self.op == "OR":
            return int(self.inputs[0] | self.inputs[1])
        elif self.op == "LSHIFT":
            return int(self.inputs[0] << self.inputs[1])
        elif self.op == "RSHIFT":
            return int(self.inputs[0] >> self.inputs[1])

    def resolve_inputs(self, signals):
#        inputs = []
#        for i in self.inputs:
#            if i in signals:
#                inputs.append(signals[i])
#            else:
#                inputs.append(i)
#        self.inputs = inputs
        self.inputs = [signals[i] if i in signals else i for i in self.inputs]

    def resolved(self):
        # If all inputs are resolved, they are all ints
        return all([isinstance(i, int) for i in self.inputs])

if __name__ == "__main__":
    with open("Day7-input.txt") as file:
        instructions = file.read().splitlines()
        wires = [Wire(i) for i in instructions]

    def process_circuit(wires, signals):
        local_wires = list(wires)
        while len(local_wires) != 0:
            unresolved_wires = []
            for wire in wires:
                if wire.resolved():
                    signals[wire.output] = wire.process()
                else:
                    wire.resolve_inputs(signals)
                    unresolved_wires.append(wire)
            local_wires = unresolved_wires
        return signals

    
    signals = process_circuit(wires, {})
    print('a', signals['a'])
    
    [wire.reset() for wire in wires]
    wires = [wire for wire in wires if wire.output != 'b']
    
    signals = {"b": signals["a"]}
    while len(wires) != 0:
        unresolved_wires = []
        for wire in wires:
            if wire.resolved():
                signals[wire.output] = wire.process()
                print("signals[{}]: {}".format(wire.output, signals[wire.output]))
            else:
                wire.resolve_inputs(signals)
                unresolved_wires.append(wire)
        wires = unresolved_wires

    print(signals["a"])

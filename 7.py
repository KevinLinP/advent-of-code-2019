from itertools import permutations

class IntcodeComputer:
    def __init__(self):
        self.pointer = 0
        self.input_buffer = []
        self.output_buffer = []
        self.status = 'running'
        # self.memory = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        self.memory = [3,8,1001,8,10,8,105,1,0,0,21,30,55,76,97,114,195,276,357,438,99999,3,9,102,3,9,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,2,9,1001,9,2,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,2,9,102,5,9,9,1001,9,4,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]

    def run(self, runInput = []):
        if self.status == 'stopped':
            raise Exception()

        self.input_buffer = self.input_buffer + runInput

        while True:
            should_increment_pointer = True
            opcode = self.memory[self.pointer] % 100
            if (opcode == 3) and (len(self.input_buffer) == 0):
                self.status = 'waiting'
                break
            if opcode == 99:
                self.status = 'stopped'
                break

            num_parameters = {
                1: 3,
                2: 3,
                3: 1,
                4: 1,
                5: 2,
                6: 2,
                7: 3,
                8: 3,
            }[opcode]

            num_read_parameters = {
                1: 2,
                2: 2,
                3: 0,
                4: 1,
                5: 2,
                6: 2,
                7: 2,
                8: 2,
            }[opcode]

            parameters = map(lambda i: self.memory[self.pointer + 1 + i], range(0, num_parameters))
            parameters = list(parameters)
            parameter_modes = self.memory[self.pointer] // 100

            for i in range(0, num_read_parameters):
                parameter_mode = parameter_modes % 10
                if parameter_mode == 0:
                    parameters[i] = self.memory[parameters[i]]
                elif parameter_mode == 1:
                    parameters[i]
                else:
                    print(parameters)
                    print(parameter_mode)
                    raise Exception()

                parameter_modes = parameter_modes // 10

            if opcode == 1:
                self.memory[parameters[2]] = parameters[0] + parameters[1]
            elif opcode == 2:
                self.memory[parameters[2]] = parameters[0] * parameters[1]
            elif opcode == 3:
                self.memory[parameters[0]] = self.input_buffer.pop(0)
            elif opcode == 4:
                self.output_buffer.append(parameters[0])
            elif opcode == 5: # jump-if-true
                if parameters[0] != 0:
                    self.pointer = parameters[1]
                    should_increment_pointer = False
            elif opcode == 6: # jump-if-false
                if parameters[0] == 0:
                    self.pointer = parameters[1]
                    should_increment_pointer = False
            elif opcode == 7: # less-than
                self.memory[parameters[2]] = 1 if (parameters[0] < parameters[1]) else 0
            elif opcode == 8: # equals
                self.memory[parameters[2]] = 1 if (parameters[0] == parameters[1]) else 0
            else:
                raise Exception()

            if should_increment_pointer:
                self.pointer += (num_parameters + 1)

        # print(self.memory)
        return self.status

phase_permutations = list(permutations(range(5, 10)))

def thruster_signal(phase_permutation):
    def init_computer(phase_setting):
        computer = IntcodeComputer()
        computer.run([phase_setting])
        if computer.status != 'waiting':
            raise Exception()
        return computer
    computers = list(map(init_computer, phase_permutation))

    pipe = 0
    current_computer_index = 0
    while True:
        current_computer = computers[current_computer_index]
        current_computer.run([pipe])
        pipe = current_computer.output_buffer[-1]
        print(pipe)
        if (current_computer_index == 4) and (current_computer.status == 'stopped'):
            break
        current_computer_index = (current_computer_index + 1) % 5

    return pipe

outputs = map(lambda p: thruster_signal(p), phase_permutations)
# outputs = map(lambda p: thruster_signal(p), [[9,8,7,6,5]])
print(max(outputs))

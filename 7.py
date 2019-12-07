from itertools import permutations

def run(originalInput = []):
    input = list(originalInput)
    output = []
    memory = [3,8,1001,8,10,8,105,1,0,0,21,30,55,76,97,114,195,276,357,438,99999,3,9,102,3,9,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,2,9,1001,9,2,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,2,9,102,5,9,9,1001,9,4,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]
    pointer = 0

    while True:
        should_increment_pointer = True
        opcode = memory[pointer] % 100
        if opcode == 99:
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

        parameters = map(lambda i: memory[pointer + 1 + i], range(0, num_parameters))
        parameters = list(parameters)
        parameter_modes = memory[pointer] // 100

        for i in range(0, num_read_parameters):
            parameter_mode = parameter_modes % 10
            if parameter_mode == 0:
                parameters[i] = memory[parameters[i]]
            elif parameter_mode == 1:
                parameters[i]
            else:
                print(parameters)
                print(parameter_mode)
                raise Exception()

            parameter_modes = parameter_modes // 10


        if opcode == 1:
            memory[parameters[2]] = parameters[0] + parameters[1]
        elif opcode == 2:
            memory[parameters[2]] = parameters[0] * parameters[1]
        elif opcode == 3:
            memory[parameters[0]] = input.pop(0)
        elif opcode == 4:
            output.append(parameters[0])
        elif opcode == 5: # jump-if-true
            if parameters[0] != 0:
                pointer = parameters[1]
                should_increment_pointer = False
        elif opcode == 6: # jump-if-false
            if parameters[0] == 0:
                pointer = parameters[1]
                should_increment_pointer = False
        elif opcode == 7: # less-than
            memory[parameters[2]] = 1 if (parameters[0] < parameters[1]) else 0
        elif opcode == 8: # equals
            memory[parameters[2]] = 1 if (parameters[0] == parameters[1]) else 0
        else:
            raise Exception()

        if should_increment_pointer:
            pointer += (num_parameters + 1)

    # print(memory)
    return output

phase_permutations = list(permutations(range(0, 5)))
# print(phase_permutations)

def thruster_signal(phase_permutation):
    input = 0
    for phase in phase_permutation:
        output = run([phase, input])
        input = output[0]
    return output[0]

outputs = map(lambda p: thruster_signal(p), phase_permutations)
print(max(outputs))

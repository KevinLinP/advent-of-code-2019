// const memory = [1,0,0,0,99]
// const memory = [1,9,10,3,2,3,11,0,99,30,40,50]
//const memory = [1,1,1,4,99,5,6,0,99]

function program(noun, verb) {
  const memory = [1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,9,23,1,23,9,27,1,10,27,31,1,13,31,35,1,35,10,39,2,39,9,43,1,43,13,47,1,5,47,51,1,6,51,55,1,13,55,59,1,59,6,63,1,63,10,67,2,67,6,71,1,71,5,75,2,75,10,79,1,79,6,83,1,83,5,87,1,87,6,91,1,91,13,95,1,95,6,99,2,99,10,103,1,103,6,107,2,6,107,111,1,13,111,115,2,115,10,119,1,119,5,123,2,10,123,127,2,127,9,131,1,5,131,135,2,10,135,139,2,139,9,143,1,143,2,147,1,5,147,0,99,2,0,14,0];

  let pointer = 0;
  let terminated = false;

  while (!terminated) {
    const operandAIndex = memory[pointer + 1];
    const operandBIndex = memory[pointer + 2];
    const writeIndex = memory[pointer + 3];

    const operandA = memory[operandAIndex];
    const operandB = memory[operandBIndex];

    switch (memory[pointer]) {
      case 1:
        memory[writeIndex] = operandA + operandB;
        break;
      case 2:
        memory[writeIndex] = operandA * operandB;
        break;
      case 99:
        return memory[0];
        break;
      default:
        new Error();
    }

    pointer += 4;
  }
}

for (i = 0; i < 100; i++) {
  for (j = 0; j < 100; j++) {
    const result = program(i, j);
    if (result == 19690720) {
      console.log(`noun:${i} verb:${j} ${100 * i + j}`);
    }
  }
}


import time

w1, w2, b = 0.2, 0.9, -1

def activate(x):
    return 1 if x >= 0 else 0

def train_perceptron(inputs, desired_outputs, learning_rate, epochs):
    global w1, w2, b  
    print(f"w1: {w1}, w2: {w2}, b: {b}")
    for epoch in range(epochs):
        total_error = 0
        print(f"total_error: {total_error}")
        for i in range(len(inputs)):
            A, B = inputs[i]
            print(f"A : {A}, B: {B}")
            target_output = desired_outputs[i]
            print(f"target_output: desired_outputs[{i}] => {desired_outputs[i]} => {target_output}")
            output = activate(w1 * A + w2 * B + b)
            print(f"output: activate({w1} * {A} + {w2} * {B} + {b}) => {output}")
            error = target_output - output
            print(f"error: {target_output} - {output} => {error}")
            w1 += learning_rate * error * A
            print(f"w1: {learning_rate} * {error} * {A} => {w1}")
            w2 += learning_rate * error * B
            print(f"w2: {learning_rate} * {error} * {B} => {w2}")
            b += learning_rate * error
            print(f"b: b + ({learning_rate} * {error}) => {b}")
            total_error += abs(error)
            print(f"Epoch {epoch+1}, Error: {total_error}")
            print()
            time.sleep(2)
        if total_error == 0:
            break


inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
desired_outputs = [0, 0, 0, 1]
learning_rate = 0.1
epochs = 100

train_perceptron(inputs, desired_outputs, learning_rate, epochs)

for _, (A, B) in enumerate(inputs):
    output = activate(w1 * A + w2 * B + b)
    print(f"Input: ({A}, {B})  Output: {output}")
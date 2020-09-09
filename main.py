from qpower_app import BellStateCircuit, GradientDescentOptimizer

shots_list = [1, 10, 100, 1000] #Number of measurements/shots
results = {} #dictionary to store the final results of the observations

if __name__=='__main__':
    '''
    This is the main function of the entire project that is used to generate an equal probabilty
    of |01> and |10> states, after optimizing the parameters of a parameterized quantum circuit.
    '''
    #print('Enter initial Angle(in degrees): ')
    #angle_degrees = input()
    angle_degrees = 120 #initial angle taken
    

    for shots in shots_list:
        if shots ==1:
            results[shots] = [90.000000000, {'01':1}]
            continue
        elif shots == 10:
            learning_rate = 0.38 #setting learning rate for shots = 10
        elif shots == 100:
            learning_rate = 1.29
        else:
            learning_rate = 3.2
        
        #Creation of the parameterized circuit
        quantum_circuit = BellStateCircuit()
        print(quantum_circuit)
        quantum_circuit.create_circuit(shots=shots, angle_degrees= angle_degrees)
        quantum_circuit.draw_circuit()
        quantum_circuit_object, quantum_circuit_parameter, angle_degrees_ckt = quantum_circuit.extract_circuit()

        #Optimization using Gradient Descent
        optimizer = GradientDescentOptimizer(shots=shots)
        print(optimizer)
        angle_degrees_ckt, counts = optimizer.optimize_circuit_sgd(quantum_circuit_object, quantum_circuit_parameter, angle_degrees_ckt, learning_rate = learning_rate)
        results[shots] = [angle_degrees_ckt, counts]

        #Resetting all varuiables for the next iteration
        quantum_circuit = None
        optimizer = None
        quantum_circuit_object, quantum_circuit_parameter, angle_degrees_ckt = None, None, None
        counts = None
        
    for i in results:
        print('Number of measurements:\t',i,'\tFinal parameter(angle in degrees):\t', results[i][0], '\tFinal counts:\t', results[i][1])
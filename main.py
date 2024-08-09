import pandas as pd
import matplotlib.pyplot as plt
import random

# person 1 only takes the extreme exits (0 seconds or 10 seconds)
# person 2 takes completely random exits 
# person 3 takes any exit from 3-7 (3 seconds or 7 seconds)

def simulation(numRuns: int):
    df = pd.DataFrame({
        'P1': [10*random.randint(0,1) for _ in range(numRuns)],
        'P2': [random.randint(0, 10) for _ in range(numRuns)],
        'P3': [random.randint(3, 7) for _ in range(numRuns)]
    })
    
    return df

def find_simulation_averages(numRuns: int):
    data = simulation(numRuns)
    return ((data['P1'].sum() / numRuns), 
            (data['P2'].sum() / numRuns), 
            (data['P3'].sum() / numRuns))    

def CLTsimulation(numRuns: int, numAvgs: int):
    df = pd.DataFrame(columns=['P1', 'P2', 'P3'])
    for _ in range(numAvgs):
        x = find_simulation_averages(numRuns)
        new_row = pd.DataFrame([[x[0], x[1], x[2]]], columns=['P1', 'P2', 'P3'])
        df = pd.concat([df, new_row], ignore_index=True)
    
    return df

# wip trying to create bargraph or histogram ig for the CLT simulation

def display_simulation(type: str, numRuns: int, numAvgs: int):
    
    if(type == 'simulation'):
        data = simulation(numRuns)
        data_avg = data.expanding().mean()
        
        plt.figure(figsize=(10,6))
        plt.plot(data_avg.index, data_avg['P1'], marker='.', label='P1')
        plt.plot(data_avg.index, data_avg['P2'], marker='.', label='P2')
        plt.plot(data_avg.index, data_avg['P3'], marker='.', label='P3')

        plt.ylim(0,10)

        plt.xlabel('Index')
        plt.ylabel('Expanding Average')
        plt.title('Expanding Average of P1, P2, P3')
        plt.legend()

        plt.show()
    
    else:
        print()

display_simulation('CLT', 100, 10)

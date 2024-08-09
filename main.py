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

def find_simulation_averages(data, numRuns: int):
    return ((data['P1'].sum() / numRuns), 
            (data['P2'].sum() / numRuns), 
            (data['P3'].sum() / numRuns))    

def CLTsimulation(numRuns: int, numAvgs: int):
    df = pd.DataFrame(columns=['P1', 'P2', 'P3'])
    for _ in range(numAvgs):
        data = simulation(numRuns)
        x = find_simulation_averages(data, numRuns)
        new_row = pd.DataFrame([[x[0], x[1], x[2]]], columns=['P1', 'P2', 'P3'])
        df = pd.concat([df, new_row], ignore_index=True)
    
    return df

def display_simulation(type: str, numRuns: int, numAvgs = 0):
    
    if(type == 'simulation'):
        data = simulation(numRuns)
        data_avg = data.expanding().mean()
        avg = find_simulation_averages(data, numRuns)

        plt.figure(figsize=(10,6))
        plt.plot(data_avg.index, data_avg['P1'], marker='.', label='P1')
        plt.plot(data_avg.index, data_avg['P2'], marker='.', label='P2')
        plt.plot(data_avg.index, data_avg['P3'], marker='.', label='P3')

        plt.ylim(0,10)

        plt.text(0.939 * numRuns, 7.35, 
        f'P1: {avg[0]:.2f} \nP2: {avg[1]:.2f} \nP3: {avg[2]:.2f}')

        plt.xlabel('Iterations')
        plt.ylabel('Expanding Average')
        plt.title('Single Simulation')
        plt.legend()

        plt.show()
    
    elif(type == 'CLT'):
        
        data = CLTsimulation(numRuns, numAvgs)

        plt.figure(figsize=(10, 6))
        plt.hist(data['P1'], alpha=0.8, edgecolor='black', label='P1')
        plt.hist(data['P2'], alpha=0.7, edgecolor='black', label='P2')
        plt.hist(data['P3'], alpha=0.6, edgecolor='black', label='P3')
        
        ymax = (numAvgs / 4)+ 50
        plt.xlim(0, 10)
        plt.ylim(0, ymax)
        plt.xlabel('Average')
        plt.ylabel('Counts')
        plt.title('Central Limit Theorem')

        CLTaverage = find_simulation_averages(data, numAvgs)
        plt.text(9.1, .735 * ymax, 
        f'P1: {CLTaverage[0]:.2f} \nP2: {CLTaverage[1]:.2f} \nP3: {CLTaverage[2]:.2f}')

        plt.legend()
        plt.show()
    
    else:
        print("Invalid simulation...")

# test runs
# display_simulation('simulation', 100)
# display_simulation('CLT', 10, 750)

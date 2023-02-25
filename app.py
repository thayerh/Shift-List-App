import pandas as pd
import PyQt5
from typing import List, Dict
import random as rd

def main():
    for i in range(1000):
        pres = Presentable(['10', '10:30', '11'], ['Bar', 'Front', 'Back'], ['jacob', 'coop', 'jon', 'rome', 'dean'])

class GUI:
    ...

class Options:
    jobs: List[str]
    workers: List[str]

    def __init__(self, jobs: List[str], workers: List[str]) -> None:
        self.jobs = jobs
        self.workers = workers

class Presentable:
    def __init__(self, shiftTimes: List[str], positions: List[str], workers: List[str]) -> None:
        #Calculate max shifts per worker with even distribution
        if len(workers) < len(positions):
            raise ValueError("Not enough workers")

        print("----------------------------")
    
        numPos = len(positions)
        numWrk = len(workers)
        numShifts = len(shiftTimes)
        maxShifts = 1 + ((numPos * numShifts) // numWrk)
        #nummaxes
        shiftPerWrk: Dict[str, int] = {}
        for worker in workers:
            shiftPerWrk[worker] = 0

        print(maxShifts)
        #Assign shifts randomly
        data = {}
        for time in shiftTimes:
            wrkThisTime = list(shiftPerWrk.keys())
            print(time + str(wrkThisTime))
            data[time] = {}
            for position in positions:
                worker = rd.choice(wrkThisTime)
                shiftPerWrk[worker] += 1
                data[time][position] = worker
                wrkThisTime.remove(worker)
                if shiftPerWrk[worker] >= maxShifts:
                    shiftPerWrk.pop(worker)

        #print(data)
        







if __name__ == "__main__":
    main()
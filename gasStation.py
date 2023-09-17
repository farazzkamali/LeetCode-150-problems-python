class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)

        # Initialize variables to keep track of the current starting station and the total gas in the tank.
        start_station = 0
        current_gas = 0
        total_gas = 0

        for i in range(n):
            # Calculate the net gas at each station (gas available minus gas required to travel to the next station).
            net_gas = gas[i] - cost[i]
            current_gas += net_gas
            total_gas += net_gas

            # If the gas at this station is negative, it means we can't start from the current station.
            # Move to the next station and reset the current_gas.
            if current_gas < 0:
                start_station = i + 1
                current_gas = 0

        # If the total_gas is negative, it means we can't complete the circular journey.
        if total_gas < 0:
            return -1
        else:
            return start_station

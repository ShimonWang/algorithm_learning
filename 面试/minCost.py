class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        # diff = costs[:, 0] - costs[:, 1]
        # for i, cost in enumerate(costs):
        #     print(i, cost)
        costs.sort(key=lambda x: x[0] - x[1])
        print(costs)

        n = len(costs) // 2
        total_cost = 0

        # for i in range(n):
        #     total_cost += costs[i][0]
        # for i in range(n, len(costs)):
        #     total_cost += costs[i][1]
        for i in range(n):
            total_cost += costs[i][1]
        for i in range(n, len(costs)):
            total_cost += costs[i][0]

        return total_cost


sol = Solution()
costs = [[10, 20], [10, 60], [50, 30], [30, 50]]
print(sol.minCost(costs))
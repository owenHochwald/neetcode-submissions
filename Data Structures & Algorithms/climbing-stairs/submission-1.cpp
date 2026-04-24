class Solution {
public:
    map<int, int> ways = {{1,1}, {2,2}, {3,3}};

    int climbStairs(int n) {
        auto itr = ways.find(n);
        if (itr == ways.end()) {
            int curr = climbStairs(n-1) + climbStairs(n-2);
            ways[n] = curr;
        }
        return ways[n];

        
    }
};

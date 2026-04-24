class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<double, vector<int>>> pq;

        for (vector<int> point : points) {
            double distance = sqrt((point[0] * point[0]) + (point[1] * point[1]));
            pq.push({distance, point});

            if (pq.size() > k) pq.pop();
        }

        vector<vector<int>> ret;
        while (!pq.empty()) {
            ret.push_back(pq.top().second);
            pq.pop();
        }
        return ret;
        
    }
};

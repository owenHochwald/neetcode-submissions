class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }

        priority_queue<pair<int, int>, vector<pair<int,int>>, greater<>> pq;

        for (auto pair : freq) {
            if (pq.size() >= k && pair.second > pq.top().first) {
                pq.pop();
                pq.push({pair.second, pair.first});
            } else if (pq.size() < k) {
                pq.push({pair.second, pair.first});
            }
        }
        vector<int> ret;
        while (!pq.empty()) {
            ret.push_back(pq.top().second);
            pq.pop();
        }

        return ret;
        
    }
};

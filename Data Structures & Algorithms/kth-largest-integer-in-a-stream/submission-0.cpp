class KthLargest {
public:
    priority_queue<int, vector<int>, greater<>> pq;
    int kth;
    KthLargest(int k, vector<int>& nums) {
                kth = k;

        for (int num : nums) {
            add(num);
        }
        
    }
    
    int add(int val) {
        pq.push(val);
        if (pq.size() > kth) {
            pq.pop();
        }
        return pq.top();
    }
};

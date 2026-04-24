class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> d1;
        unordered_map<char, int> d2;

        for (char c : s) {
            d1[c]++;
        }
        for (char c : t) {
            d2[c]++;
        }

        for (auto p : d1) {
            if (d2[p.first] != p.second) {
                return false;
            }
        }

        for (auto p : d2) {
            if (d1[p.first] != p.second) {
                return false;
            }
        }
        return true;        
    }
};

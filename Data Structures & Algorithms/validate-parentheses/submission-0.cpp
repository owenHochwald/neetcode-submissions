class Solution {
public:
    bool isValid(string s) {
        stack<string> st;

        for (int i = 0; i < s.length(); i++) {
            string curr = string(1, s[i]);

            if (!st.empty() && ((st.top() == "(" && curr == ")") ||
                                (st.top() == "[" && curr == "]") ||
                                (st.top() == "{" && curr == "}"))) {
                st.pop();
            } else {
                st.push(curr);
            }
        }
        return st.empty();
    }
};

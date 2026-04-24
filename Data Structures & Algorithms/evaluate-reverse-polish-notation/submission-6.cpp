class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> numbers;

        for (int i = 0; i < tokens.size(); ++i) {
            string token = tokens[i];

            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int b = numbers.top(); numbers.pop();
                int a = numbers.top(); numbers.pop();

                if (token == "+") numbers.push(a + b);
                else if (token == "-") numbers.push(a - b);
                else if (token == "*") numbers.push(a * b);
                else if (token == "/") numbers.push(a / b); // integer division
            } else {
                numbers.push(stoi(token));
            }
        }

        return numbers.top();
    }
};

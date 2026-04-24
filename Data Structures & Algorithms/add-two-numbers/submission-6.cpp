/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* start = l1;
        ListNode* curr = start;

        while (l1 && l2) {
            int val1 = l1->val;
            int val2 = l2->val;
            if (val1 + val2 > 9) {
                if (curr->next) {
                    curr->next->val++;
                } else {
                    curr->next = new ListNode(1);
                }
                curr->val = (val1 + val2) % 10;
            } else {
                curr->val = val1 + val2;
            }
            l1 = l1->next;
            l2 = l2->next;
            curr = curr->next;
        }

        if (l2) {
            curr = l1 ? curr : curr;  // safety
            if (!curr) {
                curr = start;
                while (curr->next) curr = curr->next;
            }
            curr->next = l2;
            curr = curr->next;
        }

        while (curr) {
            if (curr->val > 9) {
                if (curr->next) {
                    curr->next->val++;
                } else {
                    curr->next = new ListNode(1);
                }
                curr->val = curr->val - 10;
            }
            curr = curr->next;

        }



        return start;
        
    }
};

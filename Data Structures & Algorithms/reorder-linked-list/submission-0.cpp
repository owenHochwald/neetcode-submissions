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
    void reorderList(ListNode* head) {
        // find midpoint to reverse
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // split into two and reverse middle
        ListNode* prev = nullptr;
        // ListNode* l2 = slow;
        while(slow) {
            ListNode* temp = slow;
            slow = slow->next;
            temp->next = prev;
            prev = temp;
        }

        // patch together the two lists

        ListNode* l1 = head;
        // cout << prev->val <<endl;
        ListNode* l2 = prev;

        // iterate over the length of l2
        while(l2->next) {
            ListNode* temp1 = l1;
            ListNode* temp2 = l2;
            l1 = l1->next;
            l2 = l2->next;
            temp1->next = temp2;
            temp2->next = l1;
        }
    }
};

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head) return nullptr;
        
        ListNode* curr = head;
        int length = 0;
        while (curr)  {
            length++;
            curr = curr->next;
        }
        if (n > length) return head;

        int idxR = length - n + 1;

        int idx = 1;
        curr = head;
        ListNode* prev = nullptr;
        while (curr) {
            if (idx == idxR) {
                // removal logic
                if (!prev) {
                    // ListNode* temp = curr;
                    // prev = curr->next;
                    // delete temp;
                    // break;
                    return curr->next;
                } else {
                    prev->next = curr->next;
                    delete curr;
                    break;
                }
                break;

            } else {
                prev = curr;
                curr = curr->next;
                idx++;
            }

        }
        return head;      
    }
};

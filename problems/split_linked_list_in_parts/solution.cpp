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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        // #first check the length of array and divide it by k.
        // #if length=10,k=4 then in each box there can be 2 . so remaining will be 2 which must be added to 1st and 2nd box
                int len=0;
        ListNode*temp=head;
        while(temp!=NULL){
            len++;
            temp=temp->next;
        }
        vector<ListNode*>v(k,NULL);
        int p=len/k;
        int extra=len%k;
        temp=head;
        int j=0;
        // understood till here
        while(temp!=NULL){
            ListNode*c=temp;
            ListNode*dummy=new ListNode(-1);
            ListNode*curr=dummy;
            for(int i=0;i<p;i++){
                curr->next=new ListNode(temp->val);
                temp=temp->next;
                curr=curr->next;
            }
            if(extra>0){
                curr->next=new ListNode(temp->val);
                temp=temp->next;
                curr=curr->next;
                extra--;
            }
            v[j]=dummy->next;
            j++;
        }
        return v;
        
    }
};
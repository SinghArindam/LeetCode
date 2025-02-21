#include <unordered_set>

using namespace std;

// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode() : val(0), left(nullptr), right(nullptr) {}
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };

class FindElements {
private:
    unordered_set<int> values; // Store valid values for fast lookup

    void recover(TreeNode* node, int val) {
        if (!node) return;
        node->val = val;
        values.insert(val);
        recover(node->left, 2 * val + 1);
        recover(node->right, 2 * val + 2);
    }

public:
    FindElements(TreeNode* root) {
        if (root) {
            recover(root, 0); // Start recovery with root value as 0
        }
    }
    
    bool find(int target) {
        return values.count(target);
    }
};

#include<stdio.h>
#include <stdlib.h>
#include <LIMITS.h>

struct TreeNode {
    int value;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* create(int value) {
    struct TreeNode* node = malloc(sizeof(struct TreeNode));
    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct TreeNode* insert(struct TreeNode* root, int value) {
    if (root == NULL) {
        return create(value);
    } else if (root->value > value) {
        root->left = insert(root->left, value);
    } else if (root->value < value) {
        root->right = insert(root->right, value);
    }
    return root;
}

struct TreeNode* minimum(struct TreeNode* root) {
    if (root == NULL) {
        return NULL;
    } else if (root->left != NULL) {
        return minimum(root->left);
    }
    return root;
}

struct TreeNode* maximum(struct TreeNode* root) {
    if (root == NULL) {
        return NULL;
    } else if (root->right != NULL) {
        return maximum(root->right);
    }
    return root;
}

struct TreeNode* delete(struct TreeNode* root, int value) {
    if (root == NULL) {
        return NULL;
    }
    if (root->value > value) {
        root->left = delete(root->left, value);
    } else if (root->value < value) {
        root->right = delete(root->right, value);
    } else {
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        } else if (root->left == NULL || root->right == NULL) {
            struct TreeNode* temp;
            if (root->left == NULL) {
                temp = root->right;
            } else {
                temp = root->left;
            }
            free(root);
            return temp;
        } else {
            root->value = maximum(root->left)->value;
            root->left = delete(root->left, root->value);
        }
    }
    return root;
}

void traverseTree(struct TreeNode* root) {
    if (root == NULL) {
        return;
    }
    traverseTree(root->left);
    printf("%d\n", root->value);
    traverseTree(root->right);
}

void printTreeLevel(struct TreeNode* root, int level) {
    if (root == NULL) {
        return;
    }
    if (root->left != NULL) {
        printf("%d -- %d : %d\n", root->value, root->left->value, level);
    }
    if (root->right != NULL) {
        printf("%d -- %d : %d\n", root->value, root->right->value, level);
    }
    printTreeLevel(root->left, level + 1);
    printTreeLevel(root->right, level + 1);
}

void printTree(struct TreeNode* root) {
    printTreeLevel(root, 1);
}

int lrlpSum(struct TreeNode* root) {
    if (root == NULL) {
        return INT_MIN;
    }
    if (root->left == NULL && root->right == NULL) {
        return root->value;
    }
    int left = lrlpSum(root->left);
    int right = lrlpSum(root->right);
    return (left > right ? left : right) + root->value;
}

int lrlpPath(struct TreeNode* root, int sum) {
    if (root == NULL && sum == 0) {
        return 1;
    }
    if (root == NULL) {
        return 0;
    }
    int left = lrlpPath(root->left, sum - root->value);
    int right = left == 0 ? lrlpPath(root->right, sum - root->value) : 0;
    if (left == 1 || right == 1) {
        printf("--%d", root->value);
    }
    return left == 1 || right == 1;
}

void lrlp(struct TreeNode* root) {
    int sum = lrlpSum(root);
    lrlpPath(root, sum);
    printf(" = %d\n", sum);
}

int main() {
    struct TreeNode* root2 = create(4);
    insert(root2, 2);
    insert(root2, 3);
    insert(root2, 8);
    insert(root2, 6);
    insert(root2, 7);
    insert(root2, 9);
    insert(root2, 12);
    insert(root2, 1);
    printTree(root2);
    traverseTree(root2);
    delete(root2, 4);
    delete(root2, 12);
    delete(root2, 2);
    printTree(root2);
    traverseTree(root2);

    struct TreeNode* root3 = create(7);
    insert(root3, 5);
    insert(root3, 2);
    insert(root3, 15);
    insert(root3, 21);
    insert(root3, 10);
    insert(root3, 9);
    insert(root3, 13);
    printTree(root3);
    lrlp(root3);

    return 0;
}
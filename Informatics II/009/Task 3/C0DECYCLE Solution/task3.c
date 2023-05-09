#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int value;
    struct TreeNode* left;
    struct TreeNode* right;
    struct TreeNode* parent;
};

struct TreeNode* insert(struct TreeNode* root, struct TreeNode* parent, int value) {
    struct TreeNode* node = NULL;
    if (root == NULL) {
        node = malloc(sizeof(struct TreeNode));
        node->value = value;
        node->left = NULL;
        node->right = NULL;
        node->parent = parent;
        return node;
    }
    if (value > root->value) {
        root->right = insert(root->right, root, value);
    } else {
        root->left = insert(root->left, root, value);
    }
    return root;
}

struct TreeNode* search(struct TreeNode* root, int value) {
    struct TreeNode* current = root;
    while (current != NULL && current->value != value) {
        if (value < current->value) {
            current = current->left;
        } else {
            current = current->right;
        }
    }
    return current;
}


struct TreeNode* leftRotate(struct TreeNode* root, int key) {
    struct TreeNode* temp = search(root, key);
    if (temp == NULL || temp->right == NULL) {
        return root;
    }
    struct TreeNode* right = temp->right;
    temp->right = right->left;
    if (right->right != NULL) {
        right->right->parent = temp;
    }
    right->parent = temp->parent;
    if (temp->parent == NULL) {
        right->left = temp;
        temp->parent = right;
        return right;
    } else if (temp == temp->parent->left) {
        temp->parent->left = right;
    } else {
        temp->parent->right = right;
    }
    right->left = temp;
    temp->parent = right;
    return root;
}

struct TreeNode* rightRotate(struct TreeNode* root, int key) {
    struct TreeNode* temp = search(root, key);
    if (temp == NULL || temp->left == NULL) {
        return root;
    }
    struct TreeNode* left = temp->left;
    temp->left = left->right;
    if (left->left != NULL) {
        left->left->parent = temp;
    }
    left->parent = temp->parent;
    if (temp->parent == NULL) {
        left->right = temp;
        temp->parent = left;
        return left;
    } else if (temp == temp->parent->left) {
        temp->parent->left = left;
    } else {
        temp->parent->right = left;
    }
    left->right = temp;
    temp->parent = left;
    return root;
}

void printTreeRecursive(struct TreeNode* root) {
    if (root == NULL) {
        return;
    }
    if (root->left != NULL) {
        printf("  %d -- %d\n", root->value, root->left->value);
        printTreeRecursive(root->left);
    }
    if (root->right != NULL) {
        printf("  %d -- %d\n", root->value, root->right->value);
        printTreeRecursive(root->right);
    }
}

void printTree(struct TreeNode* root) {
    printf("graph g {\n");
    printTreeRecursive(root);
    printf("}\n");
}

int main() {
    struct TreeNode* root = NULL;
    printf("Inserting: 4, 2, 3, 8, 6, 7, 9, 12, 1\n");
    root = insert(root, root,  4);
    root = insert(root, root, 2);
    root = insert(root, root, 3);
    root = insert(root, root, 8);
    root = insert(root, root, 6);
    root = insert(root, root, 7);
    root = insert(root, root, 9);
    root = insert(root, root, 12);
    root = insert(root, root, 1);
    printTree(root);
    root = leftRotate(root,8);
    printTree(root);
    root = rightRotate(root,4);
    printTree(root);
    return 0;
}
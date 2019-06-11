// Problem from Cracking the Coding Interview: Chapter 1
// 2.2: Return Kth to Last
// Implement an algorithm to find the kth to last element of a singly linked list

#include <iostream>
#include "linked_list.h"

int size(Node*);
Node* kthToLast(Node*, int);
Node* nodeAt(Node*, int);
int kToIndex(int, int);


Node* kthToLast(Node* head, int k) {
    int index = kToIndex(size(head), k);
    return nodeAt(head, index);
}

int size(Node* head) {
    int len = 1;
    Node* t = head;

    while (t->getNext() != nullptr) {
        len++;
        t = t->getNext();
    }

    return len;
}

Node* nodeAt(Node* head, int index) {
    Node* t = head;
    for (int i = 0; i < index; i++) {
        t = t->getNext();
    }
    return t;
}

int kToIndex(int size, int k) {
    return size - 1 - k;
}

int main() {
    LinkedList* list1 = new LinkedList();

    list1->insert(new Node("0"));
    list1->insert(new Node("1"));
    list1->insert(new Node("2"));
    list1->insert(new Node("3"));
    list1->insert(new Node("4"));
    list1->insert(new Node("5"));
    
    std::cout << list1->getPrintString();
    
    Node* head = list1->nodeAt(0);
    std::cout << kthToLast(head, 0)->getData() << std::endl;
    std::cout << kthToLast(head, 1)->getData() << std::endl;
    std::cout << kthToLast(head, 2)->getData() << std::endl;
    std::cout << kthToLast(head, 3)->getData() << std::endl;
    std::cout << kthToLast(head, 4)->getData() << std::endl;

    return 0;
}

// Pseudocode
// Kth element from last element 

// kToIndex(int k, int length)
// size(Node* head)
// nodeAt(int index, Node* head)

// kthElement(int k, Node* head):
// int index = kToIndex(k, size(head))
// Return nodeAt(index, head)

// kToIndex(int k, int length):
// Return length - 1 - k

// size(Node* head):
// len = 1
// t = head
// While t->getNext != nullptr:
// Len++
// Return len


// Problem from Cracking the Coding Interview: Chapter 1
// 2.2: Return Kth to Last
// Implement an algorithm to find the kth to last element of a singly linked list

#include <iostream>
#include "linked_list.h"

int size(Node*);
Node* kthToLast(LinkedList*, int);
int kToIndex(int, int);


Node* kthToLast(LinkedList* list, int k) {
    Node* head = list->nodeAt(0);
    int index = kToIndex(size(head), k);
    return list->nodeAt(index);
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

    std::cout << kthToLast(list1, 0)->getData() << std::endl;
    std::cout << kthToLast(list1, 1)->getData() << std::endl;
    std::cout << kthToLast(list1, 2)->getData() << std::endl;
    std::cout << kthToLast(list1, 3)->getData() << std::endl;
    std::cout << kthToLast(list1, 4)->getData() << std::endl;

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


// Problem from Cracking the Coding Interview: Chapter 1
// 2.1: Remove Dups
// Write code to remove duplicates from an unsorted linked list.
// FOLLOW UP
// How would you solve the problem if a temporary buffer is not allowed?

#include <iostream>
#include "linked_list.h"

void remove_dups(LinkedList* list) {
    if (list->size() < 2) return;

    bool arr[26];
    Node* prev = list->nodeAt(0);
    arr[prev->getData()[0] - 65] = true;

    Node* n = prev->getNext();
    while (n != nullptr) {
        char charValue = n->getData()[0];
        charValue -= 65;
        if (!arr[charValue]) {
            arr[charValue] = true;
            prev = n;
        } else {
            prev->setNext(n->getNext());
        }
        n = n->getNext();
    }
}

int main() {
    LinkedList* list1 = new LinkedList();

    list1->insert(new Node("F"));
    list1->insert(new Node("O"));
    list1->insert(new Node("L"));
    list1->insert(new Node("L"));
    list1->insert(new Node("O"));
    list1->insert(new Node("W"));
    list1->insert(new Node(" "));
    list1->insert(new Node("U"));
    list1->insert(new Node("P"));

    std::cout << list1->getPrintString();

    remove_dups(list1);

    std::cout << list1->getPrintString();

    LinkedList* list2 = new LinkedList();

    list2->insert(new Node("F"));
    list2->insert(new Node("F"));
    list2->insert(new Node("F"));
    list2->insert(new Node("O"));
    list2->insert(new Node("O"));
    list2->insert(new Node("H"));
    list2->insert(new Node("P"));

    std::cout << list2->getPrintString();

    remove_dups(list2);

    std::cout << list2->getPrintString();

    return 0;
}


// Thoughts
// Do spaces count? I will assume it does not for simplicity sake.
// Make an boolean array of size 26, and toggle on for a character if found.
// If you come across a character that already exists, remove the node. Done!

// Time complexity: O(n)
// Space complexity: O(n)


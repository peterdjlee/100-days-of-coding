// Problem from Cracking the Coding Interview: Chapter 1
// 2.4: Partition
// Write code to partition a linked list around a value x,
// such that all nodes less than x come before all nodes
// greater than or equal to x. 
// EXAMPLE
// Input: 3->5->8->5->10->2->1 [partition = 5]
// Output: 3->1->2 | 10->5->5->8

#include <iostream>
#include "node.h"

void partition(Node* head, int partNum) {
    Node* newHead = head;
    Node* prev = nullptr;
    Node* temp = head;

    while (temp->getNext() != nullptr) {
        if (temp->getData() < partNum && temp != head) {
            prev->setNext(temp->getNext());
            temp->setNext(newHead);
            newHead = temp;
        } else {
            prev = temp;
        }
        temp = temp->getNext();
    }
}

std::string printList(Node* head) {
    std::string output;
    Node* n = head;
    while (n != nullptr) {
        output += n->getData();
        output += " -> ";
        n = n->getNext();
    }
    output += "null\n";

    return output;
}

int main() {
    Node* head = new Node(3);
    Node* t = head;
    
    t->setNext(new Node(5));
    t = t->getNext();
    t->setNext(new Node(8));
    t = t->getNext();
    t->setNext(new Node(5));
    t = t->getNext();
    t->setNext(new Node(10));
    t = t->getNext();
    t->setNext(new Node(2));
    t = t->getNext();
    t->setNext(new Node(1));
    
    std::cout << printList(head);

    partition(head, 5);

    std::cout << printList(head);

    return 0;
}

// Thoughts
// 

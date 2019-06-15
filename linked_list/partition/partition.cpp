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

Node* partition(Node* head, int partNum) {
    Node* bigger = new Node();
    Node* startBigger = bigger;
    Node* smaller = new Node();

    Node* t = head;
    while (t->getNext() != nullptr) {
        if (t->getData() < partNum) {
            smaller->setNext(t);
            smaller = smaller->getNext();
        } else {
            bigger->setNext(t);
            bigger = bigger->getNext();
        }
        t = t->getNext();
    }
    smaller->setNext(startBigger->getNext());
    return smaller;
}

void printList(Node* head) {
    std::string output;
    Node* n = head;
    while (n != nullptr) {
        std::cout << n->getData();
        std::cout << " -> ";
        n = n->getNext();
    }
    std::cout <<  "null\n";

    std::cout << output << std::endl;
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
    
    printList(head);

    printList(partition(head, 5));

    return 0;
}

// Thoughts
// 

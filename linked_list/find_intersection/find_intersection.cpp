// Problem from Cracking the Coding Interview: Chapter 2
// 2.7: Intersection
// Given two (singly) linked lists, determine if the two lists intersect.
// Return the intersecting node. Note that the intersection is defined based 
// on reference, not value. That is, if the kth node of the first linked list
// is the exact same node (by reference) as the jth node of the second linked
// list, then they are intersecting.

#include <iostream>
#include "node.h"

void printList(Node*);

Node* findIntersection(Node* head1, Node* head2) {
    int length1 = 1;
    int length2 = 1;
    Node* temp1 = head1;
    Node* temp2 = head2;

    while (temp1->getNext() != nullptr) {
        length1++;
        temp1 = temp1->getNext();
    }

    while (temp2->getNext() != nullptr) {
        length2++;
        temp2 = temp2->getNext();
    }

    if (temp1 != temp2) return nullptr;

    int lenDiff = 0;
    lenDiff = length1 - length2;
    if (lenDiff < 0) lenDiff *= -1;

    temp1 = head1;
    temp2 = head2;
    if (length1 > length2) {
        for (int i = 0; i < lenDiff; i++) {
            temp1 = temp1->getNext();
        }
    } else {
        for (int i = 0; i < lenDiff; i++) {
            temp2 = temp2->getNext();
        }
    }

    while (temp1->getNext() != nullptr) {
        if (temp1 == temp2) return temp1;
        temp1 = temp1->getNext();
        temp2 = temp2->getNext();
    }

    return nullptr;
}

void printList(Node* head) {
    std::string output;
    Node* n = head;
    while (n != nullptr) {
        output += n->getData();
        output += " -> ";
        n = n->getNext();
    }
    output += "null\n";

    std::cout << output << std::endl;
}

int main() {
    Node* intersection = new Node("b");
    Node* t = intersection;
    t->setNext(new Node("o"));
    t = t->getNext();
    t->setNext(new Node("o"));
    t = t->getNext();
    t->setNext(new Node("k"));
    
    Node* head1 = new Node("M");
    t = head1;
    t->setNext(new Node("a"));
    t = t->getNext();
    t->setNext(new Node("c"));
    t = t->getNext();
    t->setNext(intersection);

    Node* head2 = new Node("N");
    t = head2;
    t->setNext(new Node("o"));
    t = t->getNext();
    t->setNext(new Node("t"));
    t = t->getNext();
    t->setNext(new Node("e"));
    t = t->getNext();
    t->setNext(intersection);
    
    printList(head1);
    printList(head2);

    std::cout << "The intersection of the two lists is: " << std::endl;
    printList(findIntersection(head1, head2));

    return 0;
}
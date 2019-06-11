// Problem from Cracking the Coding Interview: Chapter 1
// 2.3: Delete Middle Node
// Implemenet an algorithm to delete a node in the middle
// (i.e., any node but the first and last node, not necessarily
// the exact middle) of a singly linked list, given only access to that node.

// EXAMPLE
// Input: the node c from linked list a->b->c->d->e->f
// Output: nothing is returned, but the new linked list looks like a->b->d->e->f

#include <iostream>
#include "node.h"

// void deleteMiddleNode(Node* toBeDeleted) {
//     Node* t = toBeDeleted;
//     Node* prev = t;
//     std::string data;
//     while (t->getNext() != nullptr) {
//         data = t->getNext()->getData();
//         t->setData(data);
//         prev = t;
//         t = t->getNext();
//     }
//     prev->setNext(nullptr);
// }

void deleteMiddleNode(Node* toBeDeleted) {
    toBeDeleted->setData(toBeDeleted->getNext()->getData());
    toBeDeleted->setNext(toBeDeleted->getNext()->getNext());
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
    Node* head = new Node("a");
    Node* t = head;
    Node* toBeDeleted;

    t->setNext(new Node("b"));
    t = t->getNext();
    t->setNext(new Node("c"));
    t = t->getNext();
    toBeDeleted = t; // c should be deleted
    t->setNext(new Node("d"));
    t = t->getNext();
    t->setNext(new Node("e"));
    t = t->getNext();
    t->setNext(new Node("f"));
    
    printList(head);

    deleteMiddleNode(toBeDeleted);

    printList(head);

    return 0;
}

// Thoughts
// In order to delete a node, prevNode->setNext(node->getNext())
// But we cannot get access to previous node at all, only the nodes after.
// So instead of changing the pointer itself, 
// data must be transferred and last node needs to be deleted

// After looking at the solution, I realize it was unnecessary to copy over every node.
// Might be a reoccurring mistake if I'm not being aware of the property of linked lists.

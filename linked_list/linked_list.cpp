#include <iostream>
#include "linked_list.h"

LinkedList::LinkedList(): head(nullptr) {

}

LinkedList::~LinkedList() {

}

void LinkedList::insert(Node* newNode) {
    if (head == nullptr) {
        head = newNode;
    } else {
        Node* t = head;
        while (t->getNext() != nullptr) {
            t = t->getNext();
        }
        t->setNext(newNode);
    }
}


std::string LinkedList::getPrintString() {
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

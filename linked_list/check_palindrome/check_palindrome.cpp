// Problem from Cracking the Coding Interview: Chapter 2
// 2.6: Palinedrome
// Implement a function to check if a linked list is palinedrome

#include <iostream>
#include "node.h"

void printList(Node*);
Node* reverseList(Node*);

bool isPalindrome(Node* head) {
    Node* reversed = reverseList(head);
    Node* temp1 = head;
    Node* temp2 = reversed;
    while (temp1->getNext() != nullptr) {
        if (temp1->getData() != temp2->getData()) return false;
        temp1 = temp1->getNext();
        temp2 = temp2->getNext();
    }
    return true;
}

Node* reverseList(Node* head) {
    Node* temp = head;
    Node* newHead = nullptr;
    Node* reversed = nullptr;

    while (temp->getNext() != nullptr) {
        reversed = new Node(temp->getData());
        reversed->setNext(newHead);
        newHead = reversed;
        temp = temp->getNext();
    }
    if (temp != nullptr) {
        reversed = new Node(temp->getData());
        reversed->setNext(newHead);
        newHead = reversed;
    }
    return newHead;
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
    Node* head = new Node("r");
    Node* t = head;
    t->setNext(new Node("a"));
    t = t->getNext();
    t->setNext(new Node("c"));
    t = t->getNext();
    t->setNext(new Node("e"));
    t = t->getNext();
    t->setNext(new Node("c"));
    t = t->getNext();
    t->setNext(new Node("a"));
    t = t->getNext();
    t->setNext(new Node("r"));
    
    printList(head);

    std::cout << "above string is a palindrome = " << isPalindrome(head) << std::endl;

    return 0;
}
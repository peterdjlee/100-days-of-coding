// Problem from Cracking the Coding Interview: Chapter 2
// 2.8: Loop Detection
// Given a linked list which might contain a loop, 
// implement an algorithm that returns the node at the beginning of the loop.

// EXAMPLE
// Input: A -> B -> C -> D -> E -> C (the same C as earlier)
// Output: C

#include <iostream>
#include <map>
#include <iterator>
#include "node.h"

void printList(Node* head);
void printMap(std::map<Node*, std::string>);
Node* findLoop(Node* head);

Node* findLoop(Node* head) {
    Node* beginLoop = head;
    bool loopExists = false;
    bool nodeExists = false;
    std::map<Node*, std::string> pointerMap;
    std::map<Node*, std::string>::iterator it;

    while (beginLoop->getNext() != nullptr && !loopExists) {
        it = pointerMap.find(beginLoop);
        if (it == pointerMap.end()) {
            pointerMap.insert(std::pair<Node*, std::string>(beginLoop, beginLoop->getData()));
            beginLoop = beginLoop->getNext();
        } else {
            loopExists = true;
        }
    }
    if (loopExists) return beginLoop;
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

void printMap(std::map<Node*, std::string> mapToBePrinted) {
    std::map<Node*, std::string>::iterator itr; 
    for (itr = mapToBePrinted.begin(); itr != mapToBePrinted.end(); ++itr) { 
        std::cout << '\t' << itr->first 
             << ":\t" << itr->second << '\n'; 
    } 
    std::cout << std::endl; 
}

int main() {
    Node* head = new Node("l");
    Node* t = head;
    t->setNext(new Node("o"));
    t = t->getNext();
    t->setNext(new Node("l"));
    t = t->getNext();
    t->setNext(new Node("l"));
    t = t->getNext();
    t->setNext(new Node("i"));
    t = t->getNext();
    Node* beginLoop = new Node("p");
    t->setNext(beginLoop);
    t = t->getNext();
    t->setNext(new Node("o"));
    t = t->getNext();
    t->setNext(new Node("p"));
    t = t->getNext();
    t->setNext(beginLoop);
    
    Node* foundLoop = findLoop(head);
    if (foundLoop != nullptr) {
        std::cout << "The loop starts with '" << foundLoop->getData() 
        << "' with the pointer value of " << foundLoop << std::endl; 
    } else {
        std::cout << "Loop doesn't exist!\n";
    }

    return 0;
}
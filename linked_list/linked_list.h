#pragma once
#include "node.h"

class LinkedList{
    private:
    Node* head;

    public:
    LinkedList();
    ~LinkedList();
    void insert(Node* newNode);
    void remove();
    std::string getPrintString();
};

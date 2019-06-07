#pragma once
#include "node.h"

class LinkedList{
    private:
    Node* head;

    public:
    LinkedList();
    ~LinkedList();
    int size();
    Node* nodeAt(int index);
    void insert(Node* newNode);
    void remove(int index);
    std::string getPrintString();
};

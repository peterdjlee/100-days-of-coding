#include <iostream>
#include "linked_list.h"

LinkedList::LinkedList() {
    head = nullptr;
}

LinkedList::~LinkedList(){
  if (head != nullptr){
    Node *t,*t2;
    
    t = head->getNext();
    while (t != nullptr){
      t2 = t;
      t = t->getNext();
      delete t2;
    }
  }
}

int LinkedList::size() {
  int size = 1;

  if (head == nullptr) {
    return 0;
  }

  Node *t = head;
  while ((t = t->getNext())) {
    size++;
  }

  return size;
}

// returns the element at a location
Node* LinkedList::nodeAt(int index) {
  Node *t = head;

  for (int i = 0; i < index; i++) {
    t = t->getNext();
  }

  return t;
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

void LinkedList::remove(int index) {
  if (index == 0) {
    Node *next = head->getNext();
    head = next;
  }

  if (index < size()) {
    Node *prev = head;
    Node *n = head;
    for (int i = 0; i < index; i++) {
      prev = n;
      n = n->getNext();
    }
    
    prev->setNext(n->getNext());

    delete n;
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

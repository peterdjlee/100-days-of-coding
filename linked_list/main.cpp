#include <iostream>
#include "linked_list.h"

int main() {
    Node* n1 = new Node("apple");
    Node* n2 = new Node("oranges");
    Node* n3 = new Node("bananas");

    LinkedList* list = new LinkedList();

    list->insert(n1);
    list->insert(n2);
    list->insert(n3);

    std::cout << list->getPrintString();

    return 0;
}


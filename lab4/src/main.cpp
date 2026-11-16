#include <iostream>
#include "stack.h"

int main() {
    Stack<int> myStack;
    myStack.push(100);
    myStack.push(200);

    std::cout << "Top element is: " << myStack.pop() << "\n";
    return 0;
}
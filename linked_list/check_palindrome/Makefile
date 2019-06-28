CXXFLAGS = -std=c++11

main: check_palindrome.o  node.o
	g++ $(CXXFLAGS) -o main check_palindrome.o node.o

check_palindrome.o: check_palindrome.cpp node.h

node.o: node.cpp node.h

clean:
	rm  check_palindrome.o node.o main

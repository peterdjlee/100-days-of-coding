CXXFLAGS = -std=c++11

main: main.o linked_list.o node.o
	g++ $(CXXFLAGS) -o main main.o linked_list.o node.o

main.o: main.cpp linked_list.h node.h

linked_list.o: linked_list.cpp linked_list.h node.h

node.o: node.cpp node.h

clean:
	rm linked_list.o main.o node.o main

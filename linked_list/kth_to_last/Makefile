CXXFLAGS = -std=c++11

main: kth_to_last.o linked_list.o node.o
	g++ $(CXXFLAGS) -o main kth_to_last.o linked_list.o node.o

kth_to_last.o: kth_to_last.cpp linked_list.h node.h

linked_list.o: linked_list.cpp linked_list.h node.h

node.o: node.cpp node.h

clean:
	rm linked_list.o kth_to_last.o node.o main

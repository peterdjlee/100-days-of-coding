CXXFLAGS = -std=c++11

main: remove_dups.o linked_list.o node.o
	g++ $(CXXFLAGS) -o main remove_dups.o linked_list.o node.o

remove_dups.o: remove_dups.cpp linked_list.h node.h

linked_list.o: linked_list.cpp linked_list.h node.h

node.o: node.cpp node.h

clean:
	rm linked_list.o remove_dups.o node.o main

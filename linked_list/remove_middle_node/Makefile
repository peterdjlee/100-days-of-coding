CXXFLAGS = -std=c++11

main: remove_middle_node.o  node.o
	g++ $(CXXFLAGS) -o main remove_middle_node.o node.o

remove_middle_node.o: remove_middle_node.cpp node.h

node.o: node.cpp node.h

clean:
	rm  remove_middle_node.o node.o main

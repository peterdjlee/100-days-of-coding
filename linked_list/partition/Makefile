CXXFLAGS = -std=c++11

main: partition.o  node.o
	g++ $(CXXFLAGS) -o main partition.o node.o

partition.o: partition.cpp node.h

node.o: node.cpp node.h

clean:
	rm  partition.o node.o main

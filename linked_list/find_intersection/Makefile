CXXFLAGS = -std=c++11

main: find_intersection.o  node.o
	g++ $(CXXFLAGS) -o main find_intersection.o node.o

find_intersection.o: find_intersection.cpp node.h

node.o: node.cpp node.h

clean:
	rm  find_intersection.o node.o main

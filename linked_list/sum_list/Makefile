CXXFLAGS = -std=c++11

main: sum_list.o  node.o
	g++ $(CXXFLAGS) -o main sum_list.o node.o

sum_list.o: sum_list.cpp node.h

node.o: node.cpp node.h

clean:
	rm  sum_list.o node.o main

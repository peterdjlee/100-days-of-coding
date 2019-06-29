CXXFLAGS = -std=c++11

main: detect_loop.o  node.o
	g++ $(CXXFLAGS) -o main detect_loop.o node.o

detect_loop.o: detect_loop.cpp node.h

node.o: node.cpp node.h

clean:
	rm  detect_loop.o node.o main

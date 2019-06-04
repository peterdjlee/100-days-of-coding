// Problem from Cracking the Coding Interview: Chapter 1
// 1.8
// Zero Matrix: Write an algorithm that if an element in an MxN matrix is 0,
// its entire row and column are set to 0.

#include <iostream>
#include <time.h>
#include <vector>

#define M 20
#define N 20

void printArr(int arr[M][N]) {
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (arr[i][j] < 10) {
                std::cout << arr[i][j] << "  ";
            } else {
                std::cout << arr[i][j] << " ";
            }
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

struct coord {
    int r;
    int c;
};

void reset(int arr[M][N]) {
    std::vector<coord> resetCoords;

    for (int r = 0; r < M; r++) {
        for (int c = 0; c < N; c++) {
            if (arr[r][c] == 0) {
                coord resetCoord;
                resetCoord.r = r;
                resetCoord.c = c;
                resetCoords.push_back(resetCoord);
            }
        }
    }
    
    for (int i = 0; i < resetCoords.size(); i++) {
        int resetRow = resetCoords[i].r;
        int resetCol = resetCoords[i].c;
        for (int r = 0; r < M; r++) {
            arr[r][resetCol] = 0;
        }
        for (int c = 0; c < N; c++) {
            arr[resetRow][c] = 0;
        }
    }
}

void randomizeArr(int arr[M][N]) {
    srand(time(0));
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            arr[i][j] = rand() % 31;
        }
    }

    // Ensure at least one zero

    int r = rand() % M;
    int c = rand() % N;
    arr[r][c] = 0;
}

int main() {
    int arr[M][N];

    randomizeArr(arr);

    printArr(arr);

    reset(arr);

    printArr(arr);


    return 0;
}

// Thoughts
// Run a loop to find a 0 and stop as soon as one is found. Before stopping, save arr[r][c].
// Run a loop for same r and same c to reset.

// I believe the run time of this algorithm should be O(n) as well as space.
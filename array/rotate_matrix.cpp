#include <iostream>
#include <time.h>

#define N 5

void rotate(int arr[N][N], int n) {
}

void printArr(int arr[N][N], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
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

void rotateEdge(int arr[N][N], int n) {
    int prevNum = arr[0][0];
    int num = 0;
    int i;

    for (i = 1; i < n; i++) {
        num = arr[0][i];
        arr[0][i] = prevNum;
        prevNum = num;
    }

    // printArr(arr, n);

    for (i = 1; i < n; i++) {
        num = arr[i][n - 1];
        arr[i][n - 1] = prevNum;
        prevNum = num;
    }

    // printArr(arr, n);

    for (i = n - 2; i >= 0; i--) {
        num = arr[n - 1][i];
        arr[n - 1][i] = prevNum;
        prevNum = num;
    }

    // printArr(arr, n);

    for (i = n - 2; i >= 0; i--) {
        num = arr[i][0];
        arr[i][0] = prevNum;
        prevNum = num;
    }

    // printArr(arr, n);
}

void randomizeArr(int arr[N][N], int n) {
    srand(time(0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            arr[i][j] = rand() % 30 + 1;
        }
    }
}

int main() {
    int arr[N][N];

    randomizeArr(arr, N);

    printArr(arr, N);

    rotateEdge(arr, N);

    printArr(arr, N);


    return 0;
}

// Thoughts
// The solution I have right now doesn't work;
// I'm going to have to implement an iterative algorithm along with an actual rotating edge algorithm
#include <iostream>
#include <time.h>

#define N 5

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

void rotate(int arr[N][N], int n) {
    int temp = 0;
    int num = 0;
    int offset = 0;

    // for (int i = 0; i < n / 2; i++) {
        for (int j = 0; j < n - 1; j++) {
            num = arr[j][n - 1];
            arr[j][n - 1] = arr[0][j];

            temp = arr[n - 1][n - 1 - j];
            arr[n - 1][n - 1 - j] = num;

            num = arr[n - 1 - j][0];
            arr[n - 1 - j][0] = temp;

            arr[0][j] = num;
        }
    // }
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

    rotate(arr, N);

    printArr(arr, N);


    return 0;
}

// Thoughts
// The solution I have right now doesn't work;
// I'm going to have to implement an iterative algorithm along with an actual rotating edge algorithm
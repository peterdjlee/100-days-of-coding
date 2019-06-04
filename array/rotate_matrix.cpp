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
    for (int i = 0; i < n / 2; i++) {
        int first = i;
        int last = n - 1 - i;
        for (int j = first; j < last; j++) {
            int offset = j - first;
            int top = arr[first][j];

            arr[first][j] = arr[last-offset][first];

            arr[last-offset][first] = arr[last][last-offset];

            arr[last][last-offset] = arr[i][last];

            arr[j][last] = top;

        }
    }
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
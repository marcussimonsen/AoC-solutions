#include <cstdio>
#include <iostream>

using namespace std;

int solve(int ax, int ay, int bx, int by, int x, int y) {
  if (x == 0 && y == 0) {
    return 0;
  } else if (x < 0 || y < 0) {
    return -1;
  }
  return -1;
}

int main() {
  int ax, ay, bx, by, x, y;

  while (scanf("Button A: X+%d, Y+%d", &ax, &ay) == 2) {
    if (scanf("Button B: X+%d, Y+%d", &bx, &by) != 2) {
      cout << "Failed to read button B after reading button A" << endl;
      return 1;
    }

    if (scanf("Prize: X=%d, Y=%d", &x, &y)) {
      cout << "Failed to read target after reading button A and B" << endl;
      return 1;
    }
  }

  return 0;
}

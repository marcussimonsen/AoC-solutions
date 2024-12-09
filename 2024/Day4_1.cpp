#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  vector<vector<char>> puzzle;
  string line;

  while (getline(cin, line)) {
    vector<char> data(line.begin(), line.end());
    puzzle.push_back(data);
  }

  int xmas = 0;
  string XMAS = "XMAS";
  for (int y = 0; y < puzzle.size(); y++) {
    for (int x = 0; x < puzzle[y].size(); x++) {
      if (puzzle[y][x] != 'X')
        continue;

      // Rightwards
      if (x + 3 < puzzle[y].size()) {
        bool dirs[] = {true, y - 3 >= 0, y + 3 < puzzle.size()};
        for (int i = 1; i < XMAS.size(); i++) {
          // Right
          if (dirs[0] && puzzle[y][x + i] != XMAS[i])
            dirs[0] = false;
          // Up-Right
          if (dirs[1] && puzzle[y - i][x + i] != XMAS[i])
            dirs[1] = false;
          // Down-Right
          if (dirs[2] && puzzle[y + i][x + i] != XMAS[i])
            dirs[2] = false;
        }

        for (int i = 0; i < 3; i++) {
          if (dirs[i])
            xmas++;
        }
      }

      // Leftwards
      if (x - 3 >= 0) {
        bool dirs[] = {true, y - 3 >= 0, y + 3 < puzzle.size()};
        for (int i = 1; i < XMAS.size(); i++) {
          // Left
          if (dirs[0] && puzzle[y][x - i] != XMAS[i])
            dirs[0] = false;
          // Up-Left
          if (dirs[1] && puzzle[y - i][x - i] != XMAS[i])
            dirs[1] = false;
          // Down-Left
          if (dirs[2] && puzzle[y + i][x - i] != XMAS[i])
            dirs[2] = false;
        }

        for (int i = 0; i < 3; i++) {
          if (dirs[i])
            xmas++;
        }
      }

      // Up

      if (y - 3 >= 0) {
        int c = 0;
        for (int i = 1; i < XMAS.size(); i++) {
          if (puzzle[y - i][x] == XMAS[i])
            c++;
        }
        if (c == 3)
          xmas++;
      }
      // Down
      if (y + 3 < puzzle.size()) {
        int c = 0;
        for (int i = 1; i < XMAS.size(); i++) {
          if (puzzle[y + i][x] == XMAS[i])
            c++;
        }
        if (c == 3)
          xmas++;
      }
    }
  }

  cout << "Total XMAS words found: " << xmas << endl;

  return 0;
}

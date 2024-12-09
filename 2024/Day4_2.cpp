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
  for (int y = 1; y < puzzle.size() - 1; y++) {
    for (int x = 1; x < puzzle[y].size() - 1; x++) {
      if (puzzle[y][x] != 'A')
        continue;

      int c = 0;
      if (puzzle[y - 1][x - 1] == 'M' && puzzle[y + 1][x + 1] == 'S')
        c++;
      else if (puzzle[y - 1][x - 1] == 'S' && puzzle[y + 1][x + 1] == 'M')
        c++;

      if (puzzle[y + 1][x - 1] == 'M' && puzzle[y - 1][x + 1] == 'S')
        c++;
      else if (puzzle[y + 1][x - 1] == 'S' && puzzle[y - 1][x + 1] == 'M')
        c++;

      if (c == 2)
        xmas++;
    }
  }

  cout << "Total XMAS words found: " << xmas << endl;

  return 0;
}

#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum Direction { u, r, d, l };

int main() {
  tuple<int, int> pos = {-1, -1};
  vector<string> map;
  string line;

  while (getline(cin, line)) {
    map.push_back(line);
    if (get<0>(pos) == -1) {
      for (int i = 0; i < line.size(); i++) {
        if (line[i] == '^') {
          pos = {i, map.size() - 1};
        }
      }
    }
  }

  Direction dir = u;

  while (get<1>(pos) >= 0 && get<1>(pos) < map.size() && get<0>(pos) >= 0 &&
         get<0>(pos) < map[get<1>(pos)].size()) {
    tuple<int, int> next_pos;
    switch (dir) {
    case u:
      next_pos = {get<0>(pos), get<1>(pos) - 1};
      break;
    case r:
      next_pos = {get<0>(pos) + 1, get<1>(pos)};
      break;
    case d:
      next_pos = {get<0>(pos), get<1>(pos) + 1};
      break;
    case l:
      next_pos = {get<0>(pos) - 1, get<1>(pos)};
      break;
    }

    if (get<1>(next_pos) >= 0 && get<1>(next_pos) < map.size() &&
        get<0>(next_pos) >= 0 &&
        get<0>(next_pos) < map[get<1>(next_pos)].size() &&
        map[get<1>(next_pos)][get<0>(next_pos)] == '#') {
      switch (dir) {
      case u:
        dir = r;
        break;
      case r:
        dir = d;
        break;
      case d:
        dir = l;
        break;
      case l:
        dir = u;
        break;
      }
    } else {
      map[get<1>(pos)][get<0>(pos)] = 'X';
      pos = next_pos;
    }
  }

  int positions = 0;

  for (int y = 0; y < map.size(); y++) {
    for (int x = 0; x < map[y].size(); x++) {
      if (map[y][x] == 'X')
        positions++;
    }
  }

  cout << "Total distinct positions visited: " << positions << endl;
}

#include <array>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

typedef tuple<int, int> Location;

const int width = 71;
const int height = 71;

int bfs(array<array<bool, width>, height> memory, Location s, Location t) {
  map<Location, int> dist_to;
  queue<Location> q;
  q.push(s);
  dist_to[s] = 0;

  int x, y;

  while (!q.empty()) {
    Location l = q.front();
    q.pop();

    x = get<0>(l);
    y = get<1>(l);

    if (l == t) {
      return dist_to[t];
    }

    if (y - 1 >= 0 && !memory[y - 1][x] &&
        dist_to.find({x, y - 1}) == dist_to.end()) {
      dist_to[{x, y - 1}] = dist_to[l] + 1;
      q.push({x, y - 1});
    }
    if (y + 1 < height && !memory[y + 1][x] &&
        dist_to.find({x, y + 1}) == dist_to.end()) {
      dist_to[{x, y + 1}] = dist_to[l] + 1;
      q.push({x, y + 1});
    }
    if (x - 1 >= 0 && !memory[y][x - 1] &&
        dist_to.find({x - 1, y}) == dist_to.end()) {
      dist_to[{x - 1, y}] = dist_to[l] + 1;
      q.push({x - 1, y});
    }
    if (x + 1 < width && !memory[y][x + 1] &&
        dist_to.find({x + 1, y}) == dist_to.end()) {
      dist_to[{x + 1, y}] = dist_to[l] + 1;
      q.push({x + 1, y});
    }
  }

  return -1;
}

int main() {
  Location start = {0, 0};
  Location end = {70, 70};

  int x, y;

  vector<Location> corrupted_bytes;

  while (scanf("%d,%d", &x, &y) == 2) {
    corrupted_bytes.push_back({x, y});
  }

  array<array<bool, width>, height> memory = {};

  for (int i = 0; i < 1024; i++) {
    memory[get<1>(corrupted_bytes[i])][get<0>(corrupted_bytes[i])] = true;
  }

  int steps = bfs(memory, start, end);

  cout << "Minimum number of steps: " << steps << endl;
}

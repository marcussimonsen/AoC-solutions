#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

enum Direction { north, east, south, west };

typedef tuple<int, int> Location;
typedef tuple<Location, Direction> Position;
typedef vector<string> Maze;

Direction rotate_clockwise(Direction dir) {
  switch (dir) {
  case north:
    return east;
  case east:
    return south;
  case south:
    return west;
  case west:
    return north;
  }
  return north;
}

Direction rotate_counterclockwise(Direction dir) {
  switch (dir) {
  case north:
    return west;
  case east:
    return north;
  case south:
    return east;
  case west:
    return south;
  }
  return north;
}

Location move_forward(Location loc, Direction dir) {
  int x = get<0>(loc);
  int y = get<1>(loc);
  switch (dir) {
  case north:
    return {x, y - 1};
  case south:
    return {x, y + 1};
  case west:
    return {x - 1, y};
  case east:
    return {x + 1, y};
  }
  return {-1, -1};
}

bool inside_maze(Maze maze, Location loc) {
  int x = get<0>(loc);
  int y = get<1>(loc);
  return y >= 0 && y < maze.size() && x >= 0 && x < maze[y].size() &&
         maze[y][x] != '#';
}

int dijkstra(Maze maze, Location s, Location t) {
  priority_queue<tuple<int, Position>, vector<tuple<int, Position>>,
                 greater<tuple<int, Position>>>
      pq;
  map<Position, int> dist_to;

  pq.push({0, {s, east}});

  while (!pq.empty()) {
    tuple<int, Position> p = pq.top();
    pq.pop();
    int cost = get<0>(p);
    Position pos = get<1>(p);
    Location loc = get<0>(pos);
    Direction dir = get<1>(pos);
    int x = get<0>(loc);
    int y = get<1>(loc);

    if (loc == t) {
      return cost;
    }

    // Rotate clockwise
    Position npos = {loc, rotate_clockwise(dir)};
    if (dist_to.find(npos) == dist_to.end() ||
        dist_to[npos] > dist_to[pos] + 1000) {
      dist_to[npos] = dist_to[pos] + 1000;
      pq.push({dist_to[npos], npos});
    }

    // Rotate counterclockwise
    npos = {loc, rotate_counterclockwise(dir)};
    if (dist_to.find(npos) == dist_to.end() ||
        dist_to[npos] > dist_to[pos] + 1000) {
      dist_to[npos] = dist_to[pos] + 1000;
      pq.push({dist_to[npos], npos});
    }

    // Move forward
    Location nloc = move_forward(loc, dir);
    npos = {nloc, dir};
    if (inside_maze(maze, nloc) && (dist_to.find(npos) == dist_to.end() ||
                                    dist_to[npos] > dist_to[pos] + 1)) {
      dist_to[npos] = dist_to[pos] + 1;
      pq.push({dist_to[npos], npos});
    }
  }

  return -1;
}

int main() {
  string line;
  Maze maze;

  while (getline(cin, line)) {
    maze.push_back(line);
  }

  Location start, end;

  for (int y = 0; y < maze.size(); y++) {
    for (int x = 0; x < maze[y].size(); x++) {
      if (maze[y][x] == 'S') {
        start = {x, y};
      }
      if (maze[y][x] == 'E') {
        end = {x, y};
      }
    }
  }

  int score = dijkstra(maze, start, end);

  cout << "Optimal score: " << score << endl;

  return 0;
}

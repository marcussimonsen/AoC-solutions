#include <algorithm>
#include <iostream>
#include <limits>
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

bool inside_maze(Maze *maze, Location loc) {
  int x = get<0>(loc);
  int y = get<1>(loc);
  return y >= 0 && y < (*maze).size() && x >= 0 && x < (*maze)[y].size() &&
         (*maze)[y][x] != '#';
}

void add_locations(Position pos, map<Position, vector<Position>> from,
                   map<Location, bool> *locations, Maze *maze,
                   map<Position, bool> *visited) {
  if ((*visited).find(pos) != (*visited).end())
    return;
  (*visited)[pos] = true;

  Location loc = get<0>(pos);
  (*locations)[loc] = true;

  for (auto it = from[pos].begin(); it != from[pos].end(); ++it) {
    add_locations(*it, from, locations, maze, visited);
    (*maze)[get<1>(loc)][get<0>(loc)] = 'O';
  }
}

int dijkstra(Maze *maze, Location s, Location t) {
  priority_queue<tuple<int, Position>, vector<tuple<int, Position>>,
                 greater<tuple<int, Position>>>
      pq;
  map<Position, int> dist_to;
  map<Position, vector<Position>> from;

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
      cout << "Found end" << endl;
      continue;
    }

    // Rotate clockwise
    Position npos = {loc, rotate_clockwise(dir)};
    if (dist_to.find(npos) == dist_to.end() ||
        dist_to[npos] >= dist_to[pos] + 1000) {
      if (dist_to.find(npos) == dist_to.end() || dist_to[npos] > dist_to[pos] + 1000) {
        from[npos] = {};
        pq.push({dist_to[npos], npos});
      }
      from[npos].push_back(pos);
      dist_to[npos] = dist_to[pos] + 1000;
    }

    // Rotate counterclockwise
    npos = {loc, rotate_counterclockwise(dir)};
    if (dist_to.find(npos) == dist_to.end() ||
        dist_to[npos] >= dist_to[pos] + 1000) {
      if (dist_to.find(npos) == dist_to.end() || dist_to[npos] > dist_to[pos] + 1000) {
        from[npos] = {};
        pq.push({dist_to[npos], npos});
      }
      from[npos].push_back(pos);
      dist_to[npos] = dist_to[pos] + 1000;
    }

    // Move forward
    Location nloc = move_forward(loc, dir);
    npos = {nloc, dir};
    if (inside_maze(maze, nloc) && (dist_to.find(npos) == dist_to.end() ||
                                    dist_to[npos] >= dist_to[pos] + 1)) {
      if (dist_to.find(npos) == dist_to.end() || dist_to[npos] > dist_to[pos] + 1000) {
        from[npos] = {};
        pq.push({dist_to[npos], npos});
      }
      from[npos].push_back(pos);
      dist_to[npos] = dist_to[pos] + 1;
    }
  }

  cout << "Dijkstra done" << endl;

  map<Location, bool> unique_locations;
  map<Position, bool> visited;

  int min_cost = numeric_limits<int>::max();
  if (dist_to.find({t, north}) != dist_to.end())
    min_cost = min(min_cost, dist_to[{t, north}]);
  if (dist_to.find({t, east}) != dist_to.end())
    min_cost = min(min_cost, dist_to[{t, east}]);
  if (dist_to.find({t, south}) != dist_to.end())
    min_cost = min(min_cost, dist_to[{t, south}]);
  if (dist_to.find({t, west}) != dist_to.end())
    min_cost = min(min_cost, dist_to[{t, west}]);

  if (dist_to[{t, north}] == min_cost)
    add_locations({t, north}, from, &unique_locations, maze, &visited);
  cout << "North counting done" << endl;
  if (dist_to[{t, east}] == min_cost)
    add_locations({t, east}, from, &unique_locations, maze, &visited);
  cout << "East counting done" << endl;
  if (dist_to[{t, south}] == min_cost)
    add_locations({t, south}, from, &unique_locations, maze, &visited);
  cout << "South counting done" << endl;
  if (dist_to[{t, west}] == min_cost)
    add_locations({t, west}, from, &unique_locations, maze, &visited);
  cout << "West counting done" << endl;

  for (int i = 0; i < (*maze).size(); i++) {
    cout << (*maze)[i] << endl;
  }

  return unique_locations.size();
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

  int score = dijkstra(&maze, start, end);

  cout << "unique_positions: " << score << endl;

  return 0;
}

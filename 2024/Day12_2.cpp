#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

using namespace std;

int main() {
  string line;
  vector<string> garden;

  while (getline(cin, line)) {
    garden.push_back(line);
  }

  map<tuple<int, int>, bool> visited;
  int total_fencing = 0;

  for (int oy = 0; oy < garden.size(); oy++) {
    for (int ox = 0; ox < garden[oy].size(); ox++) {
      if (visited[{ox, oy}])
        continue;

      queue<tuple<int, int>> q;

      q.push({ox, oy});
      visited[{ox, oy}] = true;

      vector<tuple<int, int>> boundary_points;
      int area = 0;
      char plant_type = garden[oy][ox];

      while (!q.empty()) {
        tuple<int, int> p = q.front();
        q.pop();
        int x = get<0>(p);
        int y = get<1>(p);

        area++;

        // Top left corner
        if (((x - 1 < 0 || garden[y][x - 1] != plant_type) &&
             (y - 1 < 0 || garden[y - 1][x] != plant_type)) ||
            (x > 0 && y > 0 && garden[y][x - 1] == plant_type &&
             garden[y - 1][x] == plant_type &&
             garden[y - 1][x - 1] != plant_type)) {
          boundary_points.push_back({x, y});
        }
        // Top right corner
        if (((x + 1 >= garden[y].size() || garden[y][x + 1] != plant_type) &&
             (y - 1 < 0 || garden[y - 1][x] != plant_type)) ||
            (x < garden[y].size() - 1 && y > 0 &&
             garden[y][x + 1] == plant_type && garden[y - 1][x] == plant_type &&
             garden[y - 1][x + 1] != plant_type)) {
          boundary_points.push_back({x + 1, y});
        }
        // Bottom left corner
        if (((x - 1 < 0 || garden[y][x - 1] != plant_type) &&
             (y + 1 >= garden.size() || garden[y + 1][x] != plant_type)) ||
            (x > 0 && y < garden.size() - 1 && garden[y][x - 1] == plant_type &&
             garden[y + 1][x] == plant_type &&
             garden[y + 1][x - 1] != plant_type)) {
          boundary_points.push_back({x, y + 1});
        }
        // Bottom right corner
        if (((x + 1 >= garden[y].size() || garden[y][x + 1] != plant_type) &&
             (y + 1 >= garden.size() || garden[y + 1][x] != plant_type)) ||
            (x < garden[y].size() - 1 && y < garden.size() - 1 &&
             garden[y][x + 1] == plant_type && garden[y + 1][x] == plant_type &&
             garden[y + 1][x + 1] != plant_type)) {
          boundary_points.push_back({x + 1, y + 1});
        }

        // Explore further
        if (x - 1 >= 0 && garden[y][x - 1] == plant_type &&
            !visited[{x - 1, y}]) {
          q.push({x - 1, y});
          visited[{x - 1, y}] = true;
        }
        if (x + 1 < garden[y].size() && garden[y][x + 1] == plant_type &&
            !visited[{x + 1, y}]) {
          q.push({x + 1, y});
          visited[{x + 1, y}] = true;
        }
        if (y - 1 >= 0 && garden[y - 1][x] == plant_type &&
            !visited[{x, y - 1}]) {
          q.push({x, y - 1});
          visited[{x, y - 1}] = true;
        }
        if (y + 1 < garden.size() && garden[y + 1][x] == plant_type &&
            !visited[{x, y + 1}]) {
          q.push({x, y + 1});
          visited[{x, y + 1}] = true;
        }
      }

      total_fencing += area * boundary_points.size();
    }
  }

  cout << "Total fencing: " << total_fencing << endl;
}

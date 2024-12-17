#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main() {
  string line;

  vector<string> city = {};
  map<char, vector<tuple<int, int>>> antennas;
  vector<vector<bool>> antinodes;

  while (getline(cin, line)) {
    antinodes.push_back({});
    for (int i = 0; i < line.size(); i++) {
      antinodes[city.size()].push_back(false);
      if (line[i] != '.') {
        if (antennas.find(line[i]) == antennas.end())
          antennas[line[i]] = {};
        antennas[line[i]].push_back({city.size(), i});
      }
    }
    city.push_back(line);
  }

  for (auto it = antennas.begin(); it != antennas.end(); ++it) {
    for (int i = 0; i < it->second.size(); i++) {
      int y1 = get<0>(it->second[i]);
      int x1 = get<1>(it->second[i]);
      for (int j = i + 1; j < it->second.size(); j++) {
        if (i == j)
          continue;
        int y2 = get<0>(it->second[j]);
        int x2 = get<1>(it->second[j]);

        int y_diff = y2 - y1;
        int x_diff = x2 - x1;

        int dy = y1;
        int dx = x1;
        while (dy >= 0 && dy < city.size() && dx >= 0 && dx < city[dy].size()) {
          antinodes[dy][dx] = true;
          dy -= y_diff;
          dx -= x_diff;
        }
        dy = y2;
        dx = x2;
        while (dy >= 0 && dy < city.size() && dx >= 0 && dx < city[dy].size()) {
          antinodes[dy][dx] = true;
          dy += y_diff;
          dx += x_diff;
        }
      }
    }
  }

  int antinode_count = 0;
  for (int i = 0; i < antinodes.size(); i++) {
    for (int j = 0; j < antinodes[i].size(); j++) {
      if (antinodes[i][j])
        antinode_count++;
    }
  }

  cout << "Amount of antinodes: " << antinode_count << endl;

  return 0;
}

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  vector<string> topographic_map = {};
  string line;

  while (getline(cin, line)) {
    topographic_map.push_back(line);
  }

  int trailhead_score_sum = 0;
  for (int y = 0; y < topographic_map.size(); y++) {
    for (int x = 0; x < topographic_map[y].size(); x++) {
      if (topographic_map[y][x] != '0')
        continue;

      int trailhead_score = 0;

      vector<tuple<int, int>> s;
      s.push_back({x, y});
      while (!s.empty()) {
        tuple<int, int> pos = s.back();
        s.pop_back();

        int px = get<0>(pos);
        int py = get<1>(pos);

        if (topographic_map[py][px] == '9') {
          trailhead_score++;
          continue;
        }

        // Up
        if (py - 1 >= 0 &&
            topographic_map[py - 1][px] == topographic_map[py][px] + 1)
          s.push_back({px, py - 1});
        // Down
        if (py + 1 < topographic_map.size() &&
            topographic_map[py + 1][px] == topographic_map[py][px] + 1)
          s.push_back({px, py + 1});
        // Left
        if (px - 1 >= 0 &&
            topographic_map[py][px - 1] == topographic_map[py][px] + 1)
          s.push_back({px - 1, py});
        // Right
        if (px + 1 < topographic_map[py].size() &&
            topographic_map[py][px + 1] == topographic_map[py][px] + 1)
          s.push_back({px + 1, py});
      }

      trailhead_score_sum += trailhead_score;
    }
  }

  cout << "Total trailhead score sum: " << trailhead_score_sum << endl;

  return 0;
}

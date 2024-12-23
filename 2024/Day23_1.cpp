#include <iostream>
#include <map>
#include <string>
#include <unordered_set>

using namespace std;

tuple<string, string> parse_pair(string &input) {
  size_t dash = input.find("-");
  return {input.substr(0, dash), input.substr(dash + 1)};
}

int solve(unordered_set<string> nodes, map<string, map<string, bool>> graph) {
  int count = 0;
  for (auto a = nodes.begin(); a != nodes.end(); a++) {
    auto b = a;
    b++;
    for (; b != nodes.end(); b++) {
      auto c = b;
      c++;
      for (; c != nodes.end(); c++) {
        if (((*a)[0] == 't' || (*b)[0] == 't' || (*c)[0] == 't') &&
            graph[*a][*b] && graph[*b][*c] && graph[*a][*c]) {
          count++;
        }
      }
    }
  }
  return count;
}

int main() {
  string line;
  map<string, map<string, bool>> graph;
  unordered_set<string> nodes;

  while (getline(cin, line)) {
    tuple<string, string> pair = parse_pair(line);

    nodes.insert(get<0>(pair));
    nodes.insert(get<1>(pair));

    graph[get<0>(pair)][get<1>(pair)] = true;
    graph[get<1>(pair)][get<0>(pair)] = true;
  }

  int res = solve(nodes, graph);

  cout << "Inter-connected computers with t: " << res << endl;

  return 0;
}

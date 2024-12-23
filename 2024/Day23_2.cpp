#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

tuple<string, string> parse_pair(string &input) {
  size_t dash = input.find("-");
  return {input.substr(0, dash), input.substr(dash + 1)};
}

string create_password(vector<string> &computers) {
  sort(computers.begin(), computers.end());
  ostringstream oss;
  for (size_t i = 0; i < computers.size(); i++) {
    if (i != 0)
      oss << ",";
    oss << computers[i];
  }
  return oss.str();
}

map<vector<string>, bool> cache;
bool check_if_fully_connected(vector<string> &subset,
                              map<string, map<string, bool>> &graph) {
  if (subset.size() == 0) {
    return true;
  } else if (cache.find(subset) != cache.end()) {
    return cache[subset];
  } else {
    string k = subset.back();
    for (size_t i = 0; i < subset.size() - 1; i++) {
      if (!graph[k][subset[i]]) {
        cache[subset] = false;
        return false;
      }
    }
    subset.pop_back();
    bool res = check_if_fully_connected(subset, graph);
    subset.push_back(k);
    cache[subset] = res;
    return res;
  }
}

void solve(int k, vector<string> &nodes, map<string, map<string, bool>> &graph,
           vector<string> &subset, vector<string> &best_so_far) {
  if (k == nodes.size()) {
    if (subset.size() > best_so_far.size()) {
      best_so_far = subset;
      cout << "New best: ";
      for (auto c : subset)
        cout << c << " ";
      cout << endl;
    }
  } else {
    // Try without element at k
    solve(k + 1, nodes, graph, subset, best_so_far);
    // Try with element k if fully connected so far
    subset.push_back(nodes[k]);
    if (check_if_fully_connected(subset, graph)) {
      solve(k + 1, nodes, graph, subset, best_so_far);
    }
    subset.pop_back();
  }
}

vector<string>
find_largest_fully_connected_component(unordered_set<string> &nodes,
                                       map<string, map<string, bool>> &graph) {
  vector<string> unique_nodes;
  for (auto n : nodes)
    unique_nodes.push_back(n);
  vector<string> best_subset;
  vector<string> subset;
  solve(0, unique_nodes, graph, subset, best_subset);
  return best_subset;
}

int main() {
  string line;
  unordered_set<string> nodes;
  map<string, map<string, bool>> connected_to;

  while (getline(cin, line)) {
    tuple<string, string> pair = parse_pair(line);

    nodes.insert(get<0>(pair));
    nodes.insert(get<1>(pair));

    connected_to[get<0>(pair)][get<1>(pair)] = true;
    connected_to[get<1>(pair)][get<0>(pair)] = true;
  }

  vector<string> largest_component =
      find_largest_fully_connected_component(nodes, connected_to);

  cout << "Largest fully connected component found: "
       << largest_component.size() << endl;
  cout << "Password: " << create_password(largest_component) << endl;

  return 0;
}

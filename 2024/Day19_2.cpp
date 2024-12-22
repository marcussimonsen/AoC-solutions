#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

map<string, long long> cache;

vector<string> parse_towels(string &input) {
  vector<string> result;
  istringstream stream(input);
  string token;

  while (getline(stream, token, ',')) {
    // Trim leading and trailing spaces
    size_t start = token.find_first_not_of(" ");
    size_t end = token.find_last_not_of(" ");
    if (start != string::npos && end != string::npos) {
      token = token.substr(start, end - start + 1);
    }

    result.push_back(token);
  }

  return result;
}

long long ways_to_make(string pattern, vector<string> &towels) {
  if (pattern.size() == 0)
    return 1;

  if (cache.find(pattern) != cache.end())
    return cache[pattern];

  long long ways = 0;

  for (string towel : towels) {
    // Check if towel is prefix of pattern
    for (int i = 0; i < towel.size(); i++) {
      if (towel[i] != pattern[i]) {
        goto skip_towel;
      }
    }

    // Check if rest of pattern can be made
    ways += ways_to_make(pattern.substr(towel.size()), towels);
  skip_towel:
  }
  cache[pattern] = ways;

  return ways;
}

int main() {
  string line;
  vector<string> towels;
  vector<string> patterns;

  if (!getline(cin, line)) {
    cout << "Couldn't read towels!" << endl;
    return 1;
  }

  // Process towels
  towels = parse_towels(line);

  getline(cin, line);

  // Read patterns
  while (getline(cin, line)) {
    patterns.push_back(line);
  }

  long long total_ways = 0;

  for (string pattern : patterns) {
    long long ways = ways_to_make(pattern, towels);
    cout << pattern << ": " << ways << endl;
    total_ways += ways;
  }

  cout << "Total ways to make all towels: " << total_ways << endl;

  return 0;
}

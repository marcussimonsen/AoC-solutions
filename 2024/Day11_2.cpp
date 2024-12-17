#include <cstdio>
#include <iostream>
#include <list>
#include <map>
#include <string>

using namespace std;

const int blinks = 75;

map<tuple<long long, int>, long long> cache{};

list<long long> blink(long long stone) {
  list<long long> resulting_stones;

  string stone_s = to_string(stone);

  if (stone == 0) {
    resulting_stones.push_back(1);
  } else if (stone_s.length() % 2 == 0) {
    int half_len = stone_s.length() / 2;
    long long a = stoll(stone_s.substr(0, half_len));
    long long b = stoll(stone_s.substr(half_len, half_len));
    resulting_stones.push_back(a);
    resulting_stones.push_back(b);
  } else {
    resulting_stones.push_back(stone * 2024);
  }

  return resulting_stones;
}

long long solve(long long stone, int level) {
  if (level == blinks)
    return 1;

  auto cached = cache.find({stone, level});
  if (cached != cache.end())
    return cached->second;

  list<long long> stones = blink(stone);
  long long total = 0;
  for (long long s : stones) {
    total += solve(s, level + 1);
  }

  cache[{stone, level}] = total;
  return total;
}

int main() {
  long long s;
  list<long long> stones;

  while (scanf("%lld", &s) == 1) {
    stones.push_back(s);
  }

  long long total_stones = 0;

  for (auto it = stones.begin(); it != stones.end(); ++it) {
    total_stones += solve(*it, 0);
  }

  cout << total_stones << endl;

  return 0;
}

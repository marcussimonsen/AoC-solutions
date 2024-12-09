#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string line;
  vector<int> disk = {};

  getline(cin, line);

  for (int i = 0; i < line.size(); i++) {
    char c = line[i];
    int digit = c - '0';

    for (int j = 0; j < digit; j++) {
      if (i % 2 == 0) {
        disk.push_back(i / 2 + i % 2);
      } else {
        disk.push_back(-1);
      }
    }
  }

  int j = 0;
  for (int i = disk.size() - 1; i >= 0; i--) {
    while (disk[j] != -1 && j < disk.size()) {
      j++;
    }
    if (j >= disk.size())
      break;
    disk[j] = disk[i];
    disk.pop_back();
  }

  long long checksum = 0;

  for (long long i = 0; i < disk.size(); i++) {
    checksum += disk[i] * i;
  }

  cout << "Disk checksum: " << checksum << endl;

  return 0;
}

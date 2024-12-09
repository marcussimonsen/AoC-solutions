#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string line;
  vector<int> disk = {};
  vector<int> file_size = {};

  getline(cin, line);

  for (int i = 0; i < line.size(); i++) {
    char c = line[i];
    int digit = c - '0';

    if (i % 2 == 0) {
      file_size.push_back(digit);
    }

    for (int j = 0; j < digit; j++) {
      if (i % 2 == 0) {
        disk.push_back(i / 2 + i % 2);
      } else {
        disk.push_back(-1);
      }
    }
  }

  int i = disk.size() - 1;
  int last_moved = disk[i] + 1;
  while (i > 0) {
    int free_size = 0;
    int i2 = i;
    while (i2 > 0 && disk[i2] == disk[i]) {
      i2--;
    }
    int file_size = i - i2;

    for (int j = 0; j < i2; j++) {
      if (disk[j] == -1) {
        int j2 = j;
        while (j2 + 1 < disk.size() && disk[j2] == -1 && j2 - j < file_size) {
          j2++;
        }
        if (j2 - j == file_size) {
          last_moved = disk[i];
          for (int k = 0; k < file_size; k++) {
            disk[j + k] = disk[i - k];
            disk[i - k] = -1;
          }
          break;
        }
      }
    }
    i -= file_size;
    while (disk[i] == -1 || disk[i] >= last_moved) {
      i--;
    }
  }

  long long checksum = 0;

  for (long long k = 0; k < disk.size(); k++) {
    if (disk[k] == -1)
      continue;
    checksum += disk[k] * k;
  }

  cout << "Disk checksum: " << checksum << endl;

  return 0;
}

#include <stddef.h>

#include <chrono>
#include <ctime>
#include <iostream>

#include <charconv>
#include <string.h>

#include <vector>

void create_and_insert(size_t num_elements) {
  std::vector<int> to_test;
  for (size_t idx = 0; idx < num_elements; ++idx) {
    to_test.push_back(idx);
  }
}

int main(int argc, char **argv) {

  if (argc < 2) {
    std::cout << "provide a number of elements to test for" << std::endl;
    return 1;
  }
  size_t num_elements;
  std::from_chars(argv[1], argv[1] + strlen(argv[1]), num_elements);

  auto start = std::chrono::system_clock::now();
  create_and_insert(num_elements);
  auto end = std::chrono::system_clock::now();

  std::chrono::duration<double> elapsed_seconds = end - start;
  std::time_t end_time = std::chrono::system_clock::to_time_t(end);
  std::cout << "elapsed seconds: " << elapsed_seconds.count() << std::endl;
}
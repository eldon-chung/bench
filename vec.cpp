#include <stddef.h>

#include <chrono>
#include <ctime>
#include <iostream>

#include <charconv>
#include <string.h>

#include <vector>

using result = std::pair<size_t, std::chrono::duration<double>>;

auto create_and_insert(size_t start_size, size_t end_size, size_t step_size) {
  std::vector<result> timing_list;
  //   reserve so no reallocs happen
  timing_list.reserve((end_size - start_size) / step_size + 1);

  std::vector<int> to_test = {0};
  //   force it to start as small as possible
  to_test.shrink_to_fit();

  auto start = std::chrono::system_clock::now();
  for (size_t items = 0; items < end_size; items++) {
    to_test.push_back(items);
    if (items >= start_size) {
      auto end = std::chrono::system_clock::now();
      timing_list.push_back({items, end - start});
      start_size += step_size;
    }
  }
  auto end = std::chrono::system_clock::now();
  timing_list.push_back({end_size, end - start});

  return timing_list;
}

int main(int argc, char **argv) {

  if (argc < 4) {
    std::cout << "provide start, end, and step size" << std::endl;
    return 1;
  }
  size_t start_size;
  size_t end_size;
  size_t step_size;
  std::from_chars(argv[1], argv[1] + strlen(argv[1]), start_size);
  std::from_chars(argv[2], argv[2] + strlen(argv[2]), end_size);
  std::from_chars(argv[3], argv[3] + strlen(argv[3]), step_size);

  auto timing_list = create_and_insert(start_size, end_size, step_size);
  for (auto const &t : timing_list) {
    std::cout << t.first << ":" << t.second.count() << std::endl;
  }
}
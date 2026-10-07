#ifndef BENCHMARK_HPP
#define BENCHMARK_HPP

#include <vector>

double benchmarkSort(
    const std::vector<int>& original,
    void (*sortFunction)(std::vector<int>&)
);

double benchmarkSearch(
    const std::vector<int>& values,
    int target,
    int (*searchFunction)(
        const std::vector<int>&,
        int
    )
);

#endif
#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>

#include "algorithms.hpp"
#include "benchmark.hpp"

using Clock = std::chrono::high_resolution_clock;


std::vector<int> generateData(
    int size
) {
    std::vector<int> values;

    values.reserve(size);

    std::mt19937 generator(42);

    std::uniform_int_distribution<int> distribution(
        1,
        1'000'000
    );

    for (int i = 0; i < size; ++i) {
        values.push_back(
            distribution(generator)
        );
    }

    return values;
}


double benchmarkSort(
    const std::vector<int>& original,
    void (*sortFunction)(std::vector<int>&)
) {
    std::vector<int> values = original;

    const auto start =
        Clock::now();

    sortFunction(values);

    const auto end =
        Clock::now();

    const std::chrono::duration<double, std::milli>
        elapsed = end - start;

    return elapsed.count();
}


double benchmarkSearch(
    const std::vector<int>& values,
    int target,
    int (*searchFunction)(
        const std::vector<int>&,
        int
    )
) {
    const auto start =
        Clock::now();

    volatile int result =
        searchFunction(
            values,
            target
        );

    const auto end =
        Clock::now();

    (void)result;

    const std::chrono::duration<double, std::nano>
        elapsed = end - start;

    return elapsed.count();
}


void printSeparator() {
    std::cout
        << "----------------------------------------\n";
}


int main() {

    std::cout
        << "========================================\n"
        << "   ALGORITHM PERFORMANCE BENCHMARK\n"
        << "========================================\n\n";


    const std::vector<int> sizes = {
        1'000,
        5'000,
        10'000
    };


    std::cout
        << std::fixed
        << std::setprecision(3);


    for (int size : sizes) {

        std::cout
            << "\nDataset size: "
            << size
            << " elements\n";

        printSeparator();


        const std::vector<int> data =
            generateData(size);


        const double bubbleTime =
            benchmarkSort(
                data,
                bubbleSort
            );

        const double insertionTime =
            benchmarkSort(
                data,
                insertionSort
            );

        const double mergeTime =
            benchmarkSort(
                data,
                mergeSort
            );

        const double quickTime =
            benchmarkSort(
                data,
                quickSort
            );


        std::cout
            << "Bubble Sort:    "
            << bubbleTime
            << " ms\n";

        std::cout
            << "Insertion Sort: "
            << insertionTime
            << " ms\n";

        std::cout
            << "Merge Sort:     "
            << mergeTime
            << " ms\n";

        std::cout
            << "Quick Sort:     "
            << quickTime
            << " ms\n";
    }


    std::cout
        << "\n\n========================================\n"
        << "           SEARCH BENCHMARK\n"
        << "========================================\n\n";


    std::vector<int> sortedData =
        generateData(100'000);

    std::sort(
        sortedData.begin(),
        sortedData.end()
    );


    const int target =
        sortedData.back();


    const double linearTime =
        benchmarkSearch(
            sortedData,
            target,
            linearSearch
        );

    const double binaryTime =
        benchmarkSearch(
            sortedData,
            target,
            binarySearch
        );


    std::cout
        << "Dataset size: 100000 elements\n";

    std::cout
        << "Target: "
        << target
        << "\n\n";

    std::cout
        << "Linear Search: "
        << linearTime
        << " ns\n";

    std::cout
        << "Binary Search: "
        << binaryTime
        << " ns\n";


    std::cout
        << "\n========================================\n"
        << "Benchmark completed.\n"
        << "========================================\n";


    return 0;
}
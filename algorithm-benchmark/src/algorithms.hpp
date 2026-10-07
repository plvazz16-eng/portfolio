#ifndef ALGORITHMS_HPP
#define ALGORITHMS_HPP

#include <vector>

void bubbleSort(std::vector<int>& values);

void insertionSort(std::vector<int>& values);

void mergeSort(std::vector<int>& values);

void quickSort(std::vector<int>& values);

int linearSearch(
    const std::vector<int>& values,
    int target
);

int binarySearch(
    const std::vector<int>& values,
    int target
);

#endif
#include <cassert>
#include <iostream>
#include <vector>

#include "../src/algorithms.hpp"


bool isSorted(
    const std::vector<int>& values
) {
    for (
        std::size_t i = 1;
        i < values.size();
        ++i
    ) {
        if (values[i - 1] > values[i]) {
            return false;
        }
    }

    return true;
}


void testBubbleSort() {

    std::vector<int> values = {
        5,
        2,
        9,
        1,
        5,
        6
    };

    bubbleSort(values);

    assert(isSorted(values));
}


void testInsertionSort() {

    std::vector<int> values = {
        8,
        3,
        7,
        4,
        2,
        6
    };

    insertionSort(values);

    assert(isSorted(values));
}


void testMergeSort() {

    std::vector<int> values = {
        10,
        3,
        5,
        1,
        8,
        2,
        7
    };

    mergeSort(values);

    assert(isSorted(values));
}


void testQuickSort() {

    std::vector<int> values = {
        12,
        4,
        9,
        1,
        7,
        3,
        10
    };

    quickSort(values);

    assert(isSorted(values));
}


void testLinearSearch() {

    std::vector<int> values = {
        10,
        20,
        30,
        40,
        50
    };

    assert(
        linearSearch(values, 30) == 2
    );

    assert(
        linearSearch(values, 99) == -1
    );
}


void testBinarySearch() {

    std::vector<int> values = {
        10,
        20,
        30,
        40,
        50
    };

    assert(
        binarySearch(values, 40) == 3
    );

    assert(
        binarySearch(values, 99) == -1
    );
}


int main() {

    testBubbleSort();
    testInsertionSort();
    testMergeSort();
    testQuickSort();

    testLinearSearch();
    testBinarySearch();

    std::cout
        << "All algorithm tests passed!\n";

    return 0;
}
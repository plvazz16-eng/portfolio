#include "algorithms.hpp"

#include <algorithm>


void bubbleSort(
    std::vector<int>& values
) {
    const int size = values.size();

    for (int i = 0; i < size - 1; ++i) {

        bool swapped = false;

        for (int j = 0; j < size - i - 1; ++j) {

            if (values[j] > values[j + 1]) {

                std::swap(
                    values[j],
                    values[j + 1]
                );

                swapped = true;
            }
        }

        if (!swapped) {
            break;
        }
    }
}


void insertionSort(
    std::vector<int>& values
) {
    const int size = values.size();

    for (int i = 1; i < size; ++i) {

        int current = values[i];

        int j = i - 1;

        while (
            j >= 0
            && values[j] > current
        ) {
            values[j + 1] = values[j];

            --j;
        }

        values[j + 1] = current;
    }
}


void merge(
    std::vector<int>& values,
    int left,
    int middle,
    int right
) {
    std::vector<int> temporary;

    int i = left;
    int j = middle + 1;

    while (
        i <= middle
        && j <= right
    ) {
        if (values[i] <= values[j]) {
            temporary.push_back(values[i]);
            ++i;
        } else {
            temporary.push_back(values[j]);
            ++j;
        }
    }

    while (i <= middle) {
        temporary.push_back(values[i]);
        ++i;
    }

    while (j <= right) {
        temporary.push_back(values[j]);
        ++j;
    }

    for (
        int k = 0;
        k < static_cast<int>(temporary.size());
        ++k
    ) {
        values[left + k] = temporary[k];
    }
}


void mergeSortRecursive(
    std::vector<int>& values,
    int left,
    int right
) {
    if (left >= right) {
        return;
    }

    const int middle =
        left + (right - left) / 2;

    mergeSortRecursive(
        values,
        left,
        middle
    );

    mergeSortRecursive(
        values,
        middle + 1,
        right
    );

    merge(
        values,
        left,
        middle,
        right
    );
}


void mergeSort(
    std::vector<int>& values
) {
    if (values.empty()) {
        return;
    }

    mergeSortRecursive(
        values,
        0,
        values.size() - 1
    );
}


int partition(
    std::vector<int>& values,
    int low,
    int high
) {
    const int pivot = values[high];

    int i = low - 1;

    for (int j = low; j < high; ++j) {

        if (values[j] <= pivot) {

            ++i;

            std::swap(
                values[i],
                values[j]
            );
        }
    }

    std::swap(
        values[i + 1],
        values[high]
    );

    return i + 1;
}


void quickSortRecursive(
    std::vector<int>& values,
    int low,
    int high
) {
    if (low >= high) {
        return;
    }

    const int pivotIndex =
        partition(
            values,
            low,
            high
        );

    quickSortRecursive(
        values,
        low,
        pivotIndex - 1
    );

    quickSortRecursive(
        values,
        pivotIndex + 1,
        high
    );
}


void quickSort(
    std::vector<int>& values
) {
    if (values.empty()) {
        return;
    }

    quickSortRecursive(
        values,
        0,
        values.size() - 1
    );
}


int linearSearch(
    const std::vector<int>& values,
    int target
) {
    for (
        int i = 0;
        i < static_cast<int>(values.size());
        ++i
    ) {
        if (values[i] == target) {
            return i;
        }
    }

    return -1;
}


int binarySearch(
    const std::vector<int>& values,
    int target
) {
    int left = 0;

    int right =
        static_cast<int>(values.size()) - 1;

    while (left <= right) {

        const int middle =
            left + (right - left) / 2;

        if (values[middle] == target) {
            return middle;
        }

        if (values[middle] < target) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }

    return -1;
}
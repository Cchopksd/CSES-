#include <iostream>
#include <vector>
#include <unordered_set>

std::vector<int> Solution(int data, const std::vector<int>& data_list) {
    std::vector<int> missing_number;
    std::unordered_set<int> data_set(data_list.begin(), data_list.end());

    for (int i = 1; i <= data; ++i) {
        if (data_set.find(i) == data_set.end()) {
            missing_number.push_back(i);
        }
    }
    return missing_number;
}

int main() {
    int number;
    std::cout << "";
    std::cin >> number;

    std::vector<int> number_list(number);
    std::cout << "";
    for (int i = 0; i < number; ++i) {
        std::cin >> number_list[i];
    }

    std::vector<int> missing_numbers = Solution(number, number_list);

    for (int x : missing_numbers) {
        std::cout << x << std::endl;
    }

    return 0;
}

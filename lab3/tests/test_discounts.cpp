#ifndef TEST_DISCOUNTS_CPP
#define TEST_DISCOUNTS_CPP

#include <iostream>
#include <vector>
#include <string>  
#include <cassert>
#include <cmath>
#include "../src/discounts.h"

struct TestCase {
    double price;
    double percent;
    double expected;
    std::string description;
};

void test_valid_discounts() {
    std::vector<TestCase> cases = {
        {100.0, 0.0, 100.0, "Граничний випадок: знижка 0%"},
        {100.0, 100.0, 0.0, "Граничний випадок: знижка 100%"},
        {100.0, 15.0, 85.0, "Звичайний випадок: знижка 15%"},
        {0.0, 50.0, 0.0, "Граничний випадок: нульова ціна товару"},
        {19.99, 10.0, 17.99, "Граничний випадок: дробова ціна та округлення"}
    };

    for (const auto& test : cases) {
        double result = apply_discount(test.price, test.percent);
        assert(std::abs(result - test.expected) < 0.001);
        std::cout << "[PASS] " << test.description << "\n";
    }
}

void test_invalid_discounts() {
    bool error_handled_1 = false;
    try {
        apply_discount(-10.0, 20.0);
    } catch (const std::invalid_argument&) {
        error_handled_1 = true;
    }
    assert(error_handled_1);

    bool error_handled_2 = false;
    try {
        apply_discount(100.0, 105.0);
    } catch (const std::invalid_argument&) {
        error_handled_2 = true;
    }
    assert(error_handled_2);

    std::cout << "[PASS] Усі помилки та винятки оброблено правильно!\n";
}

#endif
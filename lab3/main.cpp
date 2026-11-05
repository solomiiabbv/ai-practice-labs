#include <windows.h>
#include <iostream>
#include "tests/test_discounts.cpp"

int main() {
    SetConsoleOutputCP(65001); // Вмикає нормальні українські літери в консолі

    std::cout << "========================================" << std::endl;
    std::cout << "  ЗАПУСК ЛАБОРАТОРНОЇ РОБОТИ №3 (C++)   " << std::endl;
    std::cout << "========================================" << std::endl;

    std::cout << "\n[1] Перевірка валідних значень та Edge Cases:" << std::endl;
    test_valid_discounts();

    std::cout << "\n[2] Перевірка обробки помилок та винятків:" << std::endl;
    test_invalid_discounts();

    std::cout << "\n========================================" << std::endl;
    std::cout << "  УСІ ТЕСТИ УСПІШНО ПРОЙШЛИ (100% PASS) " << std::endl;
    std::cout << "========================================" << std::endl;

    return 0;
}
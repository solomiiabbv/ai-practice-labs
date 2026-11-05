#ifndef DISCOUNTS_H
#define DISCOUNTS_H

#include <stdexcept>
#include <cmath>

// Функція розрахунку знижки
inline double apply_discount(double price, double percent) {
    // Якщо ціна менша за 0 — викидаємо виняток (помилку)
    if (price < 0.0) {
        throw std::invalid_argument("price must be >= 0");
    }
    // Якщо відсоток поза межами [0, 100] — теж помилка
    if (percent < 0.0 || percent > 100.0) {
        throw std::invalid_argument("percent must be in [0, 100]");
    }
    // Рахуємо знижку і заокруглюємо до копійок
    return std::round((price * (1.0 - percent / 100.0)) * 100.0) / 100.0;
}

#endif // DISCOUNTS_H
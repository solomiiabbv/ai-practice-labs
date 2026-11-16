/**
 * @file stack.h
 * @brief Модуль реалізації узагальненого стека на C++ з суворою типізацією.
 * @author Соломія Бабіїв
 */

#ifndef STACK_H
#define STACK_H

#include <vector>
#include <stdexcept>
#include <optional>

/**
 * @class Stack
 * @brief Шаблонний (узагальнений) клас стека для зберігання елементів довільного типу.
 * @tparam T Тип даних елементів у стеку.
 */
template <typename T>
class Stack {
private:
    std::vector<T> items_; ///< Внутрішній контейнер для зберігання елементів стека

public:
    /**
     * @brief Конструктор за замовчуванням. Ініціалізує порожній стек.
     */
    Stack() = default;

    /**
     * @brief Додає елемент на вершину стека.
     * @param item Елемент типу T для додавання.
     */
    void push(const T& item) {
        items_.push_back(item);
    }

    /**
     * @brief Видаляє та повертає верхній елемент стека.
     * @return Верхній елемент стека.
     * @throw std::out_of_range Якщо стек порожній.
     */
    T pop() {
        if (items_.empty()) {
            throw std::out_of_range("Pop from empty stack");
        }
        T top_element = items_.back();
        items_.pop_back();
        return top_element;
    }

    /**
     * @brief Повертає верхній елемент без його видалення.
     * @return std::optional<T> Верхній елемент або порожній об'єкт, якщо стек порожній.
     */
    std::optional<T> peek() const {
        if (items_.empty()) {
            return std::nullopt;
        }
        return items_.back();
    }

    /**
     * @brief Перевіряє, чи порожній стек.
     * @return true, якщо стек не містить елементів, інакше false.
     */
    bool is_empty() const {
        return items_.empty();
    }
};

#endif // STACK_H
# Intern-Game-Logic-Programmer-Test

## №1
<details>
  <summary>Описание задачи</summary>

  На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 

Пример: 
```python
def isEven(value):

      return value % 2 == 0
```
</details>

[Мой код](https://github.com/ego-fm/Intern-Game-Logic-Programmer-Test/blob/main/isEven.py)

**Сравнение реализаций:**

1. ```python
   def isEven(value):
      return value % 2 == 0

2. ```python
   def is_even(value):
    return (value & 1) == 0


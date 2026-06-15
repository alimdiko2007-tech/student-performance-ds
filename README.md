# 🎓 Student Performance — Предсказание итоговой оценки

Проект по Data Science: предсказываем итоговую оценку студента (G3) на основе данных об учёбе, семье и образе жизни.

**Датасет:** [Student Performance — UCI](https://archive.ics.uci.edu/ml/datasets/student+performance)  
**Задача:** Регрессия (предсказать оценку от 0 до 20)  
**Лучшая модель:** Gradient Boosting — R² = 0.91

---

## 📁 Структура проекта

```
student-performance-ds/
├── data/
│   ├── raw/              # Исходные данные с UCI
│   └── processed/        # Закодированные данные
├── notebooks/
│   ├── week2_analysis.ipynb    # Анализ данных, 8 графиков
│   ├── week3_models.ipynb      # Обучение 3 моделей ML
│   └── week4_final.ipynb       # Финальные выводы
├── src/
│   └── download_data.py        # Скрипт загрузки датасета
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 🚀 Как запустить (одна команда)

### 1. Клонируй репозиторий
```bash
git clone https://github.com/alimdiko2007-tech/student-performance-ds.git
cd student-performance-ds
```

### 2. Запусти через Docker
```bash
docker-compose up --build
```

### 3. Открой в браузере
```
http://localhost:8888
```

---

## 📊 Итоговые метрики

| Модель | MAE | RMSE | R² |
|---|---|---|---|
| Линейная регрессия | 1.52 | 2.10 | 0.82 |
| Random Forest | 1.21 | 1.78 | 0.88 |
| **Gradient Boosting** | **1.09** | **1.61** | **0.91** |

**Победитель: Gradient Boosting** — объясняет 91% вариации оценок.

---

## 🔑 Ключевые выводы

1. **G1 и G2** — самые важные признаки (оценки за прошлые периоды)
2. **Количество провалов** сильно снижает итоговую оценку
3. **Время на учёбу и образование родителей** также влияют на результат

---

## 🛠 Инструменты

Python 3.11 · Jupyter Notebook · pandas · scikit-learn · Docker · Git

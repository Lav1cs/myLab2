import pandas as pd
from pprint import pprint

# Импортируем ваши функции и контракты
from pandas_tasks import analyze_titanic
from grader_contracts.pandas_tasks import TitanicInput, TitanicSummary

from correlation_tasks import analyze_brain_correlations
from grader_contracts.correlation_tasks import BrainDataInput, BrainCorrelationSummary


def check_titanic():
    print("=" * 50)
    print("ПРОВЕРКА ЧАСТИ 1: TITANIC")
    print("=" * 50)

    # 1. Запускаем вашу функцию с реальным файлом
    result = analyze_titanic(TitanicInput(csv_path="titanic.csv"))

    # 2. Проверяем, что вернулся правильный тип
    if not isinstance(result, TitanicSummary):
        print("❌ ОШИБКА: Функция должна возвращать объект TitanicSummary!")
        return

    print("✅ Тип возвращаемого значения верный (TitanicSummary)\n")

    # 3. Выводим результаты для визуальной проверки
    print(f"1. Всего строк (row_count): {result.row_count}")
    print(f"   (Ожидаемо: 891)")

    print(f"\n2. Пропуски по столбцам (missing_by_column):")
    pprint(result.missing_by_column)
    print("   (Проверьте, что в 'Age' около 177 пропусков, а не 0)")

    print(f"\n3. Пассажиров старше 30 лет (adults_over_30_count): {result.adults_over_30_count}")

    print(f"\n4. Средний возраст по классам (mean_age_by_pclass):")
    pprint(result.mean_age_by_pclass)
    # Проверка типов ключей
    keys_are_int = all(isinstance(k, int) for k in result.mean_age_by_pclass.keys())
    print(f"   🔍 Типы ключей являются int? {keys_are_int} (Должно быть True)")

    print(f"\n5. Доля выживших по классам (survival_rate_by_pclass):")
    pprint(result.survival_rate_by_pclass)

    print(f"\n6. Топ-5 самых дорогих билетов (highest_fares):")
    print(result.highest_fares)
    print(f"   🔍 Длина списка ровно 5? {len(result.highest_fares) == 5}")
    print(f"   🔍 Отсортированы по убыванию? {result.highest_fares == sorted(result.highest_fares, reverse=True)}")
    print("=" * 50 + "\n")


def check_correlation():
    print("=" * 50)
    print("ПРОВЕРКА ЧАСТИ 2: КОРРЕЛЯЦИЯ (BRAINSIZE)")
    print("=" * 50)

    # 1. Запускаем вашу функцию с реальным файлом
    result = analyze_brain_correlations(BrainDataInput(csv_path="brainsize.txt"))

    # 2. Проверяем тип
    if not isinstance(result, BrainCorrelationSummary):
        print("❌ ОШИБКА: Функция должна возвращать объект BrainCorrelationSummary!")
        return

    print("✅ Тип возвращаемого значения верный (BrainCorrelationSummary)\n")

    print(f"1. Количество мужчин (men_count): {result.men_count}")
    print(f"2. Количество женщин (women_count): {result.women_count}")

    print(f"\n3. Корреляции у женщин (women_mri_correlation):")
    pprint(result.women_mri_correlation)

    print(f"\n4. Корреляции у мужчин (men_mri_correlation):")
    pprint(result.men_mri_correlation)

    print(f"\n5. Признак с самой сильной корреляцией (strongest_mri_feature): '{result.strongest_mri_feature}'")

    # Проверки на частые ошибки
    if result.strongest_mri_feature == "MRI_Count":
        print("   ❌ ОШИБКА: strongest_mri_feature не может быть 'MRI_Count'! Нужно искать среди других признаков.")
    else:
        print("   ✅ Признак не является 'MRI_Count' (это хорошо)")

    print("=" * 50 + "\n")


if __name__ == "__main__":
    try:
        check_titanic()
        check_correlation()
        print("🎉 Проверка завершена! Внимательно изучите вывод выше.")
    except Exception as e:
        print(f"\n💥 ПРОИЗОШЛА ОШИБКА при выполнении вашего кода:")
        print(f"Тип ошибки: {type(e).__name__}")
        print(f"Сообщение: {e}")
        print("👆 Посмотрите на трейсбек (текст ошибки) выше, чтобы понять, в какой строке вашего кода проблема.")
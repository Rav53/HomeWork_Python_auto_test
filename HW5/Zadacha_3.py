# Напишите однострочный генератор словаря, который принимает на вход три
# списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида “10.25%”. В результате получаем словарь с именем
# в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Даша", "Коля", "Сергей"]
salaries = [8000, 15000, 25000]
bonus_percent = ["10.25%", "15.55%", "20.75%"]

salary_dict = salary_dict(names, salaries, bonus_percent)
print(salary_dict)

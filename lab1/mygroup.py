from Pinko_Alexander.lab1.mygroup import user_input

groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "marks": [5, 5, 5]
    }
]

def calculate_avg(marks):
    return sum(marks) / len(marks)

def filter(students, threshold):
    return [
        {**s, "avg": calculate_avg(s["marks"])}
        for s in students
        if calculate_avg(s["marks"]) > threshold
    ]

def results(students, threshold):
    if not students:
        print(f"\nстудентов с баллом выше {threshold} нет")
        return
    print(f"\nстуденты: {len(students)}")
    print("=" * 60)
    for idx, s in enumerate(students, 1):
        print(f"{idx}. {s['surname']} {s['name']:15} | средний балл {s['avg']}:.2f")

if __name__ == "__main__":
    try:
        user_input = float(input("введите средний балл: "))
        filtered = filter(groupmates, user_input)
        results(filtered, user_input)
    except ValueError:
        print("введите корректное число")

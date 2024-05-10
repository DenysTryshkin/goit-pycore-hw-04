def total_salary(path):
    total_sum = 0
    count_of_developers = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name_of_developer, salary = line.strip().split(",")
                total_sum += float(salary)
                count_of_developers += 1

        average_salary = total_sum / count_of_developers
        total_sum = round(total_sum)
        average_salary = round(average_salary)

        return total_sum, average_salary

    except FileNotFoundError:
        print(f"File {path} not found.")
        return None, None 
        
    except ValueError:
        print("Error! File is corrupted!")
        return None, None

total, average = total_salary("task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
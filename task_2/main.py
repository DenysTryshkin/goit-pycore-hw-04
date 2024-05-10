def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                id, name,  age = line.strip().split(",")
                cat_info = {"id": id, "name": name, "age": age}
                cats_info.append(cat_info)

        return cats_info  
    
    except FileNotFoundError:
        print(f"File {path} not found.")
        return None 
    
    except ValueError:
        print("Error! File is corrupted!")
        return None

cats_info = get_cats_info("task_2/cats_file.txt")
print(cats_info)
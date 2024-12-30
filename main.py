
import json 

from pathlib import Path

target_dir = Path(input("enter the path of the target dir:"))

json_form = Path("./src/organize_form.json")

def get_files_list(dir):

    files_list = []

    for file in dir.rglob("*"):   

        if file.is_file() :
              
              files_list.append(file)

    return files_list

def get_organizing_form(form_file):

    with form_file.open("r", encoding="utf-8") as file:

        data = json.load(file)
    
    return data["categories"]

def get_category(file_extension,categories):
    for category, extensions in categories.items():
        if file_extension in extensions:
            return category
    custom_categorie = file_extension.replace(".", "")
    return f"others/{custom_categorie}"

def main(form_file,target_dir):
    files_list = get_files_list(target_dir)
    form = get_organizing_form(form_file)

    organized_dir = target_dir.parent / f"organized_{target_dir.name}"
    organized_dir.mkdir(parents=True, exist_ok=True)

    for file in files_list:
        category = get_category(file.suffix,form)
        dis_dir = organized_dir / category
        dis_dir.mkdir(parents=True, exist_ok=True)
        file.rename(dis_dir.joinpath(file.name))



main(json_form,target_dir)
import os

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path):
    if not os.path.exists(path):
        with open(path, 'w'):
            pass

def setup_ansible_project(project_name):
    if os.path.exists(project_name):
        print(f"⚠️ Project '{project_name}' already exists! Exiting...")
        return

    create_directory(project_name)
    
    create_file(os.path.join(project_name, f"{project_name}.yml"))

    inventory_path = os.path.join(project_name, "inventory")
    create_directory(inventory_path)
    create_file(os.path.join(inventory_path, "hosts"))

    roles_path = os.path.join(project_name, "roles", project_name)
    create_directory(roles_path)

    subdirs = ["defaults", "files", "handlers", "meta", "tasks", "templates", "vars"]

    for subdir in subdirs:
        subdir_path = os.path.join(roles_path, subdir)
        create_directory(subdir_path)

        if subdir not in ["files", "templates"]:
            create_file(os.path.join(subdir_path, "main.yml"))

    print(f"✅ Ansible project '{project_name}' created successfully!")

def main():
    project_name = input("Enter Ansible project name: ").strip()
    if project_name:
        setup_ansible_project(project_name)
    else:
        print("❌ Project name cannot be empty!")

if __name__ == "__main__":
    main()

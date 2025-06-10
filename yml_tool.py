import os

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'
LINES_PER_FILE = 500

def split_file(filename):
    with open(os.path.join(INPUT_DIR, filename), 'r', encoding='utf-8-sig', newline='') as f:
        lines = f.readlines()

    total_lines = len(lines)
    file_count = (total_lines + LINES_PER_FILE - 1) // LINES_PER_FILE

    base_name = filename.rsplit('.', 1)[0]
    ext = filename.rsplit('.', 1)[1]

    for i in range(file_count):
        part_lines = lines[i * LINES_PER_FILE : (i + 1) * LINES_PER_FILE]
        part_filename = f"{base_name}_part{i + 1}.{ext}"
        with open(os.path.join(OUTPUT_DIR, part_filename), 'w', encoding='utf-8-sig', newline='') as out_file:
            out_file.writelines(part_lines)
        print(f"Created: {part_filename} with {len(part_lines)} lines")

def join_files(base_filename):
    base_name = base_filename.rsplit('.', 1)[0]
    ext = base_filename.rsplit('.', 1)[1]

    parts = sorted([f for f in os.listdir(INPUT_DIR) if f.startswith(base_name + "_part") and f.endswith("." + ext)])
    output_path = os.path.join(OUTPUT_DIR, base_filename)

    with open(output_path, 'w', encoding='utf-8-sig', newline='') as outfile:
        for part_file in parts:
            with open(os.path.join(INPUT_DIR, part_file), 'r', encoding='utf-8-sig', newline='') as infile:
                outfile.writelines(infile.readlines())
            print(f"Merged: {part_file}")

    print(f"\nFinal merged file: {output_path}")

def main():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Select Mode:")
    print("1. Split file")
    print("2. Merge parts")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        yml_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.yml')]
        if not yml_files:
            print("No YML file found in input folder.")
            return
        filename = yml_files[0]
        split_file(filename)

    elif choice == '2':
        yml_parts = [f for f in os.listdir(INPUT_DIR) if '_part' in f and f.endswith('.yml')]
        if not yml_parts:
            print("No part files found in input folder.")
            return
        base_name = yml_parts[0].split('_part')[0] + ".yml"
        join_files(base_name)

    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
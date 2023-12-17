import json
import os
import re
from multiprocessing import Process


def get_file_paths(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_paths.append(os.path.join(root, file))
    return file_paths


def process1(file_paths, output_folder):
    natijalar = []

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            matn = file.read()
            sonlar = [int(raqam) for raqam in re.findall(r'\b\d+\b', matn)]

        yigindi = sum(sonlar)

        natijalar.append({"fayl_nom": os.path.basename(file_path), "yigindi": yigindi, "sonlar": sonlar})

    json_manzil = os.path.join(output_folder, "result.json")
    with open(json_manzil, 'w') as json_fayl:
        json.dump(natijalar, json_fayl, indent=2)

    print("1-process natijasi: result.json fayliga yozildi.")


def process2(file_paths, output_folder):
    upper_words = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            for word in words:
                if word and word[0].isupper():
                    upper_words.append(word)

    upper_txt_manzil = os.path.join(output_folder, "upper.txt")
    with open(upper_txt_manzil, 'w') as output:
        output.write('\n'.join(upper_words))

    print("2-process natijasi: upper.txt fayliga yozildi.")


def process3(file_paths, output_folder):
    char_counts = {}
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            for char in content:
                if char.isalpha():
                    char_counts[char] = char_counts.get(char, 0) + 1

    chars_json_manzil = os.path.join(output_folder, "chars.json")
    with open(chars_json_manzil, 'w') as output:
        json.dump(char_counts, output, indent=4)

    print("3-process natijasi: chars.json fayliga yozildi.")


if __name__ == "__main__":
    folder_path = "descriptions"
    output_folder = "output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_paths = get_file_paths(folder_path)

    process1(file_paths, output_folder)
    process2(file_paths, output_folder)
    process3(file_paths, output_folder)

    p1 = Process(target=process1, args=(file_paths, output_folder))
    p2 = Process(target=process2, args=(file_paths, output_folder))
    p3 = Process(target=process3, args=(file_paths, output_folder))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

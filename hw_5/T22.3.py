import os


def compare_files(dir1, dir2, output_file):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))

    with open(output_file, 'w') as f:
        common_files = files1.intersection(files2)

        for file_name in common_files:
            file1_path = os.path.join(dir1, file_name)
            file2_path = os.path.join(dir2, file_name)

            size1 = os.path.getsize(file1_path)
            size2 = os.path.getsize(file2_path)

            if size1 != size2:
                f.write(f"File: {file_name} | Directory1 size: {size1} bytes | Directory2 size: {size2} bytes\n")

    print(f"Comparison complete. Results saved in {output_file}")



dir1 = 'one'
dir2 = 'two'
output_file = 'ex.txt'
compare_files(dir1, dir2, output_file)

import subprocess
from itertools import combinations

test_file = 'tests/test.txt'
test_file_2 = 'tests/test_2.txt'
test_file_3 = 'tests/pattern.txt'
test_file_4 = 'tests/result.txt'

flags = ['-i', '-v', '-c', '-l', '-n', '-h', '-s', '-e', '-f', '-o']
f_flag = '-f'

search_strings = ['[Tt]', 'and', '1.[0-9][0-9]', 'were', 'for', 'aboba', 'a']

def execute_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

success_count = 0
fail_count = 0

for search_string in search_strings:

    for r in range(1, 3):
        for flag_combination in combinations(flags, r):

            if f_flag in flag_combination and '-c' in flag_combination and '-o' in flag_combination:
                continue
            if f_flag in flag_combination and '-e' in flag_combination and '-o' in flag_combination:
                continue

            command_flags = list(flag_combination)

            if f_flag in flag_combination:
                command_flags.remove(f_flag)
                command_flags.append(f_flag)
            if not f_flag in flag_combination:
                original_command = ['grep'] + command_flags + [search_string, test_file, test_file_2, test_file]
                original_output = execute_command(original_command)
            if f_flag in flag_combination:
                original_command = ['grep'] + command_flags + [test_file_3, test_file_4]
                original_output = execute_command(original_command)

            if not f_flag in flag_combination:
                my_command = ['./s21_grep'] + command_flags + [search_string, test_file, test_file_2, test_file]
                my_output = execute_command(my_command)
            if f_flag in flag_combination:
                my_command = ['./s21_grep'] + command_flags + [test_file_3, test_file_4]
                my_output = execute_command(my_command)

            if original_output == my_output:
                result = 'SUCCESS'
                success_count += 1
            else:
                result = 'FAIL'
                fail_count += 1

            if f_flag in flag_combination:
                print(f"Flags: {' '.join(flag_combination)}, Result: {result}")
            else:
                print(f"Search String: {search_string}, Flags: {' '.join(flag_combination)}, Result: {result}")

print(f"TOTAL: SUCCESS - {success_count}, FAIL - {fail_count}")
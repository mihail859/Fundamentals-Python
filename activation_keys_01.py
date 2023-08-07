def contains_function(raw_activation_key, substring):

    if substring in raw_activation_key:
        return f"{raw_activation_key} contains {substring}"
    return "Substring not found!"


def flip_function(raw_activation_key, upper_or_lower1, start_idx1, end_idx1):

    first_part = raw_activation_key[:start_idx1]
    final_part = raw_activation_key[end_idx1:]
    middle_part = raw_activation_key[start_idx1:end_idx1]
    if upper_or_lower1 == 'Upper':
        return first_part + middle_part.upper() + final_part

    elif upper_or_lower1 == 'Lower':
        return first_part + middle_part.lower() + final_part


def slice_function(raw_activation_key,start_idx1, end_idx1):

    first_part = raw_activation_key[:start_idx1]
    final_part = raw_activation_key[end_idx1:]

    return first_part + final_part


activation_key = input()
while True:
    command, *params = input().split('>>>')
    if command == 'Generate':
        break

    elif command == 'Contains':
        substring_new = params[0]
        print(contains_function(activation_key, substring_new))

    elif command == 'Flip':
        upper_or_lower = params[0]
        start_idx = int(params[1])
        end_idx = int(params[2])

        activation_key = flip_function(activation_key, upper_or_lower, start_idx, end_idx)
        print(activation_key)

    elif command == 'Slice':
        start_idx = int(params[0])
        end_idx = int(params[1])
        activation_key = slice_function(activation_key, start_idx, end_idx)

        print(activation_key)

print(f"Your activation key is: {activation_key}")
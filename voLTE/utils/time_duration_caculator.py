from datetime import datetime

def extract_time(line):
    return datetime.strptime(line[:14], "%m-%d %H:%M:%S").time()

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def find_time_in_log(log_lines, keyword):
    for line in log_lines:
        if keyword in line and "SIPMSG" in line:
            return extract_time(line)

def duration_calc(filename, given_seconds):
    log_lines = read_log_file(filename)
    start_time = find_time_in_log(log_lines, "INVITE sip")
    end_time = find_time_in_log(log_lines, "BYE sip") or find_time_in_log(log_lines, "CANCEL sip")

    # print(f'Start time: {start_time}')
    # print(f'End time: {end_time}')

    delta = datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), start_time)
    actual_time_taken = delta.total_seconds()

    # print(f"Time taken is {actual_time_taken} seconds")

    if actual_time_taken - 7 <= given_seconds <= actual_time_taken + 7:
        statement = f"Actual time taken [{actual_time_taken} seconds] is within the given time-interval ({given_seconds} seconds)"
        print(statement)
    else:
        statement = f"Actual time taken [{actual_time_taken} seconds] is not within the given time-interval ({given_seconds} seconds)"
        print(statement)

    return statement

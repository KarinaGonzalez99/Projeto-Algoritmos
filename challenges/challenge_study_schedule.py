def is_valid_period(period):
    return isinstance(period, tuple) and len(period) == 2 and all(
        isinstance(time, int) for time in period)


def count_students_present(permanence_period, target_time):
    count = 0
    for start, end in permanence_period:
        if start is None or end is None:
            continue
        if start <= target_time <= end:
            count += 1
    return count


def study_schedule(permanence_period, target_time):
    if not permanence_period or target_time is None:
        return None

    if not all(is_valid_period(period) for period in permanence_period):
        return None

    return count_students_present(permanence_period, target_time)

    raise NotImplementedError

def calculate(items, num_of_intervals, s, t1, t2):
    items.sort()
    tcp = get_tcp(items)
    max_value = max(items)
    interval_length, arr_intervals = get_intervals(max_value, num_of_intervals)
    intervals_static = get_intervals_static(items, arr_intervals, max_value)
    ps = get_ps(intervals_static, interval_length)
    t = get_t(interval_length, ps, s)
    pt1 = get_pt(arr_intervals, interval_length, intervals_static, t1)[0]
    pt2 = get_pt(arr_intervals, interval_length, intervals_static, t2)[1]

    return (
        tcp,
        t,
        pt1,
        pt2
    )


def get_tcp(items):
    return sum(items) / len(arr)


def get_intervals(value, num_of_intervals):
    interval_length = value / num_of_intervals
    return interval_length, [(i * interval_length, (i + 1) * interval_length) for i in range(num_of_intervals)]


def get_intervals_static(items, intervals, max_value):
    static_values = []
    for interval in intervals:
        count = 0
        for item in items:
            if interval[0] <= item <= interval[1]:
                count += 1
        static_values.append(count / (len(intervals * max_value)))
    return static_values


def get_ps(intervals_static, interval_length):
    return 1 - (interval_length * intervals_static[0])


def get_t(interval_length, ps, s):
    return interval_length - interval_length * ((ps - s) / (ps - 1))


def get_pt(intervals, interval_length, intervals_static, t2):
    part = 0
    interval_static = None
    for i in range(len(intervals)):
        if t2 > intervals[i][1]:
            part += interval_length * intervals_static[i]
        elif t2 == intervals[i][1]:
            part += interval_length * intervals_static[i]
            interval_static = intervals_static[i]
            break
        else:
            part += (t2 - intervals[i][0]) * intervals_static[i]
            interval_static = intervals_static[i]
            break

    return (1 - part), interval_static / (1 - part)


if __name__ == '__main__':
    arr = [
        498, 76, 2, 269, 346, 491, 483, 124, 1051,
        218, 707, 339, 40, 21, 723, 3, 144, 136, 18,
        248, 40, 515, 248, 444, 305, 146, 672, 641,
        39, 234, 478, 475, 72, 247, 12, 169, 220, 92,
        357, 436, 121, 5, 3, 81, 115, 271, 259, 389,
        305, 518, 382, 89, 189, 392, 11, 568, 78,
        464, 189, 898, 309, 45, 370, 1358, 173, 66,
        616, 733, 152, 239, 207, 963, 379, 40, 216,
        364, 292, 211, 253, 48, 211, 380, 55, 495,
        302, 299, 100, 253, 173, 51, 122, 403, 286,
        1258, 37, 127, 492, 969, 155, 573
    ]
    num_intervals = 10
    s = 0.82
    t_1 = 1328
    t_2 = 200

    a, b, c, d = calculate(arr, num_intervals, s, t_1, t_2)

    print(
        f'Середній наробіток до відмови Tср: {a}\n'
        f'γ-відсотковий наробіток на відмову Tγ при γ = {s}: {b:.6f}\n'
        f'ймовірність безвідмовної роботи на час {t_1} годин: {c:.6f}\n'
        f'інтенсивність відмов на час {t_2} годин: {d:.6f}'
    )

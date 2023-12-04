
nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def fun(input: str):
    x = 0
    for line in input.splitlines():
        f = None
        l = None
        for i, ch in enumerate(line):
            for key in nums:
                if key == line[i: i + len(key)]:
                    if f is None:
                        f = nums[key]
                    l = nums[key]
                    continue
            if ch.isnumeric():
                if f is None:
                    f = int(ch)
                l = int(ch)
        x += f * 10 + l
    return x


if __name__ == '__main__':
    print(fun(input))

def number_gen_idx(digits: str, nums: str) -> str:
    """
    >>> number_gen_idx("0123456789", "210")
    4
    >>> number_gen_idx("8459761203", "5439")
    17
    """
    digits_idx = defaultdict(int)
    for idx, digit in enumerate(digits):
        digits_idx[digit]=idx
    curr_ptr = 0
    result = 0
    for digit in num:
        result += abs(digits_idx[digit] - curr_ptr)
        curr_ptr = digits_idx[digit]
    return number_gen_idx()

function calctime(digits, num){
    const digits_arr = Array.from(digits);


}


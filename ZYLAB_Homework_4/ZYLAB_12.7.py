Katheryn Busch PSID: 1868948
def get_age():
    adultAge = int(input())
    if 18 <= adultAge <= 75:
        return adultAge
    raise ValueError("Invalid age.")


def fat_burning_heart_rate(adultAge):
    rateOfHeart = (220 - adultAge) * 0.7
    return rateOfHeart


if __name__ == "__main__":
    try:
        adultAge = get_age()
        print("Fat burning heart rate for a", adultAge, "year-old:", fat_burning_heart_rate(adultAge), "bpm")
    except ValueError as exception:
        print(exception)
        print("Could not calculate heart rate info.\n")

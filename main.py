def take_input() -> tuple[int, list]:
    """
    Take input from user and return it as a tuple. Apply all constrictions
    """

    goats_number = int(input("Enter the amount of goats: "))
    number_of_courses = int(input("Enter the amount of courses: "))

    assert 0 < goats_number <= 1000, "Goats number should be between 1 and 1000"
    assert (
        0 < number_of_courses <= 1000
    ), "Number of courses should be between 1 and 1000"

    goats_weight = []

    for goat in range(goats_number):
        goat_weight = int(input(f"Enter the weight of goat {goat + 1}: "))
        assert 0 < goat_weight <= 100000, "Goat's weight should be between 1 and 100000"
        goats_weight.append(goat_weight)

    return number_of_courses, goats_weight


def calculate_vessel_min_weight() -> int:
    """Calculate the minimum weight of the vessel that carries the goats"""
    number_of_courses, goats_weight = take_input()

    goats_weight.sort(reverse=True)
    average_weight_per_course = sum(goats_weight) / number_of_courses

    last_diff = (
        0  # The last difference will always be the one where there is no left space
    )

    for _ in range(number_of_courses):
        # We go through array, because the goats need to be removed from the list every time
        # we do another course
        diff = calculate_difference_from_average_weight_for_course(
            average_weight_per_course, goats_weight
        )
        last_diff = diff

    return average_weight_per_course + abs(last_diff)


def calculate_difference_from_average_weight_for_course(
    average_per_course: int, goats_weight: list[int]
) -> int:
    """
    Calculate what the difference is between the average weight of the weight the
    vessel can carry and the actual weight of the goats in the course
    """
    left_space = average_per_course

    def get_heaviest_possible_goat(left_space: int, goats_weight: list[int]) -> int:
        """Get the heaviest possible goat that can fit in the left space"""
        for goat in goats_weight:
            if goat < left_space:
                goats_weight.remove(goat)
                return goat

        return goats_weight[0]  # if this is returned, then there is no left space

    while left_space > 0:
        heaviest_goat = get_heaviest_possible_goat(left_space, goats_weight)
        left_space -= heaviest_goat

    return left_space


if __name__ == "__main__":
    # We get the values from the input
    print(int(calculate_vessel_min_weight()))

def grade_to_letter(score: int) -> str:
    """
    Convert a numeric grade to a letter grade.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    try:
        score = int(input("Enter your numeric grade: "))
        print(f"Your letter grade is: {grade_to_letter(score)}")
    except ValueError:
        print("Invalid input. Please enter a number.")

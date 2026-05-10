students = {
    "Ravi": 85,
    "Anjali": 92,
    "Kiran": 67,
    "Sneha": 74,
    "Arjun": 55,
    "Surya": 96,
    "Meera":100
}
def calculate_average(data):
    total = sum(data.values())
    avg = total / len(data)
    return avg
def find_topper(data):
    topper = max(data, key=data.get)
    return topper, data[topper]
def categorize_students(data):
    passed = []
    failed = []
    
    for name, marks in data.items():
        if marks >= 70:
            passed.append(name)
        else:
            failed.append(name)
    
    return passed, failed
def main():
    avg = calculate_average(students)
    topper, marks = find_topper(students)
    passed, failed = categorize_students(students)

    print("Average Marks:", avg)
    print("Topper:", topper, "-", marks)
    print("Passed Students:", passed)
    print("Failed Students:", failed)

if __name__ == "__main__":
    main()

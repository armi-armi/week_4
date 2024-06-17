
def load_data():
    """Load data from file and return it as a list of lists."""
    input_file = open("subject_data.txt")
    subjects = []
    for line in input_file:
        parts = line.strip().split(',')
        parts[2] = int(parts[2])  # Convert student numbers to integers
        subjects.append(parts)
    input_file.close()
    return subjects

def main():
    """Read subject data and display formatted details."""
    data = load_data()
    display_subject_details(data)

def display_subject_details(subjects):
    """Display details about each subject."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

if __name__ == "__main__":
    main()

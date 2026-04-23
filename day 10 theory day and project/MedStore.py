# MedStore Wholesale System - Milestone 1
# Reads medicine data from a text file and displays it

def read_medicines(filename):
    """Read medicine data from text file and store in a list of dictionaries."""
    medicines = []

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")

        medicine = {
            "name": parts[0].strip(),
            "brand": parts[1].strip(),
            "stock_tablets": int(parts[2].strip()),
            "rate_per_tablet": float(parts[3].strip()),
            "rate_per_strip": float(parts[4].strip()),
            "tablets_per_strip": int(parts[5].strip())
        }

        medicines.append(medicine)

    return medicines


def display_medicines(medicines):
    """Display all medicines in a formatted table."""
    print("=" * 80)
    print("               MEDSTORE PVT. LTD. - MEDICINE INVENTORY")
    print("=" * 80)
    print(f"{'No.':<5} {'Medicine Name':<25} {'Brand':<20} {'Stock':>8} {'/Tablet':>8} {'/Strip':>8} {'Strip Size':>10}")
    print("-" * 80)

    count = 1
    for med in medicines:
        print(f"{count:<5} {med['name']:<25} {med['brand']:<20} {med['stock_tablets']:>8} {med['rate_per_tablet']:>8.2f} {med['rate_per_strip']:>8.2f} {med['tablets_per_strip']:>10}")
        count += 1

    print("=" * 80)
    print(f"Total medicines listed: {len(medicines)}")
    print("=" * 80)


# Main program
print("\nWelcome to MedStore Wholesale System")
print("Loading medicine inventory...\n")

medicines_list = read_medicines("medicines.txt")
display_medicines(medicines_list)



from pyscript import document

# Predefined sets of club members from each grade level.
grade_7 = {
    "Maria Ahtisa Manalo",
    "Chelsea Manalo",
    "Bianca Manalo",
    "Chelsea Fernandez"
}

grade_8 = {
    "Celeste Cortesi",
    "Nadia Ferreira",
    "Emoura Pham",
    "Tarah Valencia"
}

grade_9 = {
    "Bea Windorski",
    "Katrina Llegado",
    "Christine Opiaza",
    "Emma Tiglao"
}

grade_10 = {
    "Apriel Smith",
    "Nicole Borromeo",
    "Asia Rose Simpson",
    "Luciana Fuster"
}

# Combine the four sets using the union operator.
all_members = grade_7 | grade_8 | grade_9 | grade_10


# Display all members and the total number of members.
def display_members():
    # Convert the set into a sorted list for display.
    member_list = sorted(all_members)

    # Join the list elements into HTML text.
    member_output = "<br>".join(member_list)

    # Display the members and count using an f-string.
    document.querySelector("#result").innerHTML = f"""
        <h3>ALL CLUB MEMBERS</h3>
        <div class="member-list">
            {member_output}
        </div>
        <div class="total">
            TOTAL MEMBERS: {len(all_members)}
        </div>
    """


# Add a new member using the set add() method.
def add_member(event):
    # Get and format the user's input.
    first_name = document.querySelector("#first-name").value.strip().title()
    last_name = document.querySelector("#last-name").value.strip().title()

    # Combine the first and last names into one full name.
    new_member = f"{first_name} {last_name}".strip()

    # Create a set containing the new member.
    new_member_set = {new_member}

    # Use union to combine the new member with all existing members.
    global all_members
    all_members = all_members | new_member_set

    # Clear the input fields after submission.
    document.querySelector("#first-name").value = ""
    document.querySelector("#last-name").value = ""

    # Refresh the member list and total.
    display_members()


# Display the predefined members when the webpage loads.
display_members()

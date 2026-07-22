from ticket import create_ticket
from display import display_ticket

def main():
    # Call create_ticket() to get user input data
    ticket_data = create_ticket()
    
    # Display the formatted ticket
    display_ticket(ticket_data)

if __name__ == "__main__":
    main()
# Initialize sample service tickets
service_tickets = {
    "Ticket001": {
        "Customer": "Alice",
        "Issue": "Login problem",
        "Status": "open"
    },
    "Ticket002": {
        "Customer": "Bob",
        "Issue": "Payment issue",
        "Status": "closed"
    },
    "Ticket003": {
        "Customer": "Charlie",
        "Issue": "Billing question",
        "Status": "open"
    }
}

def open_new_ticket():
    ticket_id = f"Ticket{len(service_tickets) + 1:03}"
    customer_name = input("Enter customer name: ")
    issue_description = input("Enter issue description: ")
    service_tickets[ticket_id] = {
        "Customer": customer_name,
        "Issue": issue_description,
        "Status": "open"
    }
    print(f"New ticket '{ticket_id}' has been opened.")

def update_ticket_status(ticket_id):
    if ticket_id in service_tickets:
        current_status = service_tickets[ticket_id]["Status"]
        if current_status == "open":
            service_tickets[ticket_id]["Status"] = "closed"
            print(f"Ticket '{ticket_id}' has been closed.")
        else:
            service_tickets[ticket_id]["Status"] = "open"
            print(f"Ticket '{ticket_id}' has been reopened.")
    else:
        print(f"Ticket '{ticket_id}' does not exist.")

def display_tickets(filter_by_status=None):
    print("Customer Service Tickets:")
    for ticket_id, ticket_details in service_tickets.items():
        if filter_by_status is None or ticket_details["Status"] == filter_by_status:
            print(f"Ticket ID: {ticket_id}")
            print(f"Customer: {ticket_details['Customer']}")
            print(f"Issue: {ticket_details['Issue']}")
            print(f"Status: {ticket_details['Status']}")
            print()

# Example usage
open_new_ticket()
open_new_ticket()
update_ticket_status("Ticket002")
display_tickets()
print("---")
display_tickets("open")
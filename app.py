from services.email_services import EmailServices


if __name__ == "__main__":
    email_services = EmailServices()

    email_content = "My order #12345 arrived damaged and I want a replacement as soon as possible!"
    print(f"User: {email_content}\n")

    ticket = email_services.classify_email(email_content)

    print(f"Summary:         {ticket.summary}")
    print(f"Priority:        {ticket.priority.value}")
    print(f"Sentiment:       {ticket.sentiment.value}")
    print(f"Suggested reply: {ticket.suggested_reply}")


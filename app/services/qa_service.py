def get_answer(question: str) -> str:
    q = question.lower()

    if "cloud nat" in q:
        return "Cloud NAT allows private instances to access the internet without public IP addresses."
    elif "vm" in q or "virtual machine" in q:
        return "A VM is a virtual computer running inside cloud infrastructure."
    elif "iam" in q:
        return "IAM is used to manage identities, roles, and permissions."
    else:
        return f"I received your question: {question}"
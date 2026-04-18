memory = []

def add_to_memory(user, ai):
    memory.append({"user": user, "ai": ai})

def get_context():
    context = ""
    for m in memory[-5:]:
        context += f"User: {m['user']}\nAI: {m['ai']}\n"
    return context
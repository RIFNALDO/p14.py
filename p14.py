import re
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for colored console output
init(autoreset=True)

def greet_user():
    """Greet the user and introduce the chatbot."""
    print(Fore.CYAN + Style.BRIGHT + "========================================")
    print(Fore.CYAN + Style.BRIGHT + "   Welcome to Your Enhanced Chatbot!   ")
    print(Fore.CYAN + Style.BRIGHT + "========================================")
    print(Fore.GREEN + "Chatbot: Hello! I am your assistant. How can I help you today?")
    print(Fore.YELLOW + "Tip: You can ask about the weather, news updates, world times, or just chat!")
    print(Fore.CYAN + Style.BRIGHT + "----------------------------------------\n")

def get_simulated_weather(location):
    """Simulate weather updates based on location keywords."""
    location = location.lower()
    if "new york" in location:
        return "The weather in New York is currently 18°C with clear skies."
    elif "london" in location:
        return "London is experiencing light rain with a temperature of 14°C."
    elif "tokyo" in location:
        return "Tokyo has beautiful sunny weather at 22°C."
    else:
        return "The weather looks pleasant and sunny around 20°C!"

def get_world_time(city):
    """Simulate local times in different cities."""
    city = city.lower()
    now = datetime.now()
    if "tokyo" in city:
        return "It's nighttime in Tokyo right now (approx. 9 hours ahead of UTC)."
    elif "london" in city:
        return "It's daytime in London (approx. current Greenwich Mean Time)."
    elif "new york" in city:
        return "It's currently afternoon/evening in New York (Eastern Time)."
    else:
        return f"Current local system time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def chatbot_response(user_input):
    """Match user input using Regular Expressions and return a styled response."""
    user_input = user_input.lower()
    
    # 1. Greetings
    if re.search(r'\b(hi|hello|hey|greetings)\b', user_input):
        return Fore.GREEN + "Chatbot: Hello there! Great to chat with you."
    
    # 2. Weather Topic (using regex patterns)
    elif re.search(r'\b(weather|forecast|temperature)\b', user_input):
        weather_info = get_simulated_weather(user_input)
        return Fore.BLUE + f"Chatbot: {weather_info}"
    
    # 3. News Updates Topic
    elif re.search(r'\b(news|updates|headlines)\b', user_input):
        return Fore.MAGENTA + "Chatbot: Top News: Tech companies are launching exciting new AI advancements this week!"
    
    # 4. Local Time Topic
    elif re.search(r'\b(time|clock|hour)\b', user_input):
        time_info = get_world_time(user_input)
        return Fore.YELLOW + f"Chatbot: {time_info}"
    
    # 5. Farewell
    elif re.search(r'\b(bye|exit|quit|goodbye)\b', user_input):
        return "EXIT"
    
    # Default fallback response
    else:
        return Fore.RED + "Chatbot: I'm not quite sure I understand. Could you please rephrase or ask about weather, news, or time?"

def run_chatbot():
    """Main execution loop for the chatbot."""
    greet_user()
    
    while True:
        try:
            user_input = input(Fore.WHITE + "You: ").strip()
            if not user_input:
                continue
                
            response = chatbot_response(user_input)
            
            if response == "EXIT":
                print(Fore.GREEN + "\nChatbot: Goodbye! Have a wonderful day ahead!")
                break
                
            print(response + "\n")
            
        except (KeyboardInterrupt, EOFError):
            print(Fore.GREEN + "\n\nChatbot: Goodbye! Session ended safely.")
            break

if __name__ == "__main__":
    run_chatbot()
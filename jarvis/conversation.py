from jarvis.weather import get_weather
from jarvis.search import search_web
from jarvis.llm import get_llm_response
from jarvis.voice import hear, speak  # Keep these imports for non-API usage

# Existing conversation loop for voice-based interaction
def handle_conversation():
    context = ""
    print("I am Assistant! Type 'exit' to quit.")

    while True:
        user_input = hear()
        if user_input is None:
            continue

        if user_input.lower() == "exit":
            break

        if "weather" in user_input.lower():
            city = user_input.split("in")[-1].strip()
            weather_info = get_weather(city.replace(" ", "-").lower())
            print("Bot: ", weather_info)
            speak(weather_info)
            continue
        
        if "search" in user_input.lower() or "look up" in user_input.lower():
            search_query = user_input.split("search for")[-1].strip() if "search for" in user_input.lower() else user_input.split("look up")[-1].strip()
            search_result = search_web(search_query)
            print("Bot: ", search_result)
            speak(search_result)
            continue

        if context:
            history_lines = context.strip().split("\n")
            if len(history_lines) > 4:
                context = "\n".join(history_lines[-4:])

        result = get_llm_response(context, user_input)
        print("Bot: ", result)

        speak(result)

        context += f"\nUser: {user_input}\nAI: {result}"

# New function for API-based text communication
def handle_textual_input(user_input):
    """
    This function processes textual input, suitable for API communication.
    It does not use speech recognition or speech synthesis.
    """
    context = ""

    if "weather" in user_input.lower():
        city = user_input.split("in")[-1].strip()
        weather_info = get_weather(city.replace(" ", "-").lower())
        return weather_info

    if "search" in user_input.lower() or "look up" in user_input.lower():
        search_query = user_input.split("search for")[-1].strip() if "search for" in user_input.lower() else user_input.split("look up")[-1].strip()
        search_result = search_web(search_query)
        return search_result

    if context:
        history_lines = context.strip().split("\n")
        if len(history_lines) > 4:
            context = "\n".join(history_lines[-4:])

    result = get_llm_response(context, user_input)
    return result

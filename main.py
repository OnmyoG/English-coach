import stt
import llm
import tts


def main():
    while True:
        cmd = input("Press Enter to speak or type 'q' to quit: ").strip().lower()
        if cmd == "q":
            break

        # Start STT
        text, lang = stt.transcribe_speech()
        print(f"User ({lang}): {text}")

        # Generate LLM response
        reply = llm.generate_response(text)
        print(f"Assistant: {reply}")

        # Speak reply
        tts.speak_text(reply, lang)


if __name__ == "__main__":
    main()
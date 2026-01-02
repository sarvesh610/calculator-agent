"""Main entry point for the calculator agent"""
import sys
from src.calculator_agent.agents.calculator_agent import CalculatorAgent


def main():
    """Run the calculator agent in interactive mode"""
    
    # Check if logging flag is passed
    enable_logging = "--debug" in sys.argv or "--verbose" in sys.argv
    
    print("=" * 60)
    print("CALCULATOR AGENT")
    if enable_logging:
        print("🔍 DEBUG MODE ENABLED")
    print("=" * 60)
    print("I can help you with calculations!")
    print("Try: 'What's 15 plus 27?'")
    print("     'Multiply that by 3'")
    print("     'Save that as my_total'")
    print("     'What was my_total?'")
    print()
    print("Type 'quit' to exit, 'history' to see conversation")
    if not enable_logging:
        print("Type 'debug on' to enable debug logging")
    print("=" * 60)
    print()
    
    # Initialize agent with logging option
    agent = CalculatorAgent(enable_logging=enable_logging)
    
    # Interactive loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ["quit", "exit", "q"]:
                print("\nGoodbye!")
                break
            
            if user_input.lower() == "debug on":
                agent.enable_logging = True
                print("🔍 Debug logging enabled\n")
                continue
            
            if user_input.lower() == "debug off":
                agent.enable_logging = False
                print("Debug logging disabled\n")
                continue
            
            if user_input.lower() == "history":
                print("\nConversation History:")
                for entry in agent.get_conversation_history():
                    print(f"  - {entry}")
                print()
                continue
            
            if user_input.lower() == "saved":
                print("\nSaved Results:")
                saved = agent.get_saved_results()
                if saved:
                    for name, value in saved.items():
                        print(f"  {name} = {value}")
                else:
                    print("  (none)")
                print()
                continue
            
            # Run the agent
            print()  # Blank line before response
            response = agent.run(user_input)
            print(f"\nAgent: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}\n")
            if agent.enable_logging:
                import traceback
                traceback.print_exc()


if __name__ == "__main__":
    main()
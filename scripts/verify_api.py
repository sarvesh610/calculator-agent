"""Quick API test to verify setup"""
import sys
from pathlib import Path
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_api():
    # Load environment variables from project root
    env_path = project_root / ".env"
    load_dotenv(env_path)
    
    # Get API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ No API key found in .env file!")
        print(f"Expected .env at: {env_path}")
        print("Create .env file with: ANTHROPIC_API_KEY=your-key-here")
        return False
    
    print(f"✅ API key loaded (starts with: {api_key[:15]}...)")
    
    # Test API connection
    try:
        client = Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=50,
            messages=[{
                "role": "user", 
                "content": "Reply with just: 'Setup complete!'"
            }]
        )
        
        response = message.content[0].text
        print(f"✅ API connection successful!")
        print(f"✅ Claude says: {response}")
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_api()
    exit(0 if success else 1)

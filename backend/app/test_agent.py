import requests
import json
import time

def test_simple_agent():
    base_url = "http://localhost:8000/api/v1"
    
    # Wait for service to be ready
    print("Checking if service is ready...")
    max_retries = 10
    for i in range(max_retries):
        try:
            response = requests.get(f"{base_url}/health", timeout=5)
            if response.status_code == 200:
                print("✅ Service is ready!")
                print(f"Health check: {response.json()}")
                break
        except requests.exceptions.ConnectionError:
            if i < max_retries - 1:
                print(f"⏳ Waiting for service... ({i+1}/{max_retries})")
                time.sleep(3)
            else:
                print("❌ Service not available. Check Docker logs.")
                return
    
    # Test questions focused on system prompt
    questions = [
        "Hello! Tell me about Tunisia",
        "What are the top 5 places to visit in Tunisia?",
        "Tell me about Tunisian food and what I should try",
        "What's the best time to visit Tunisia and why?",
        "I'm planning a trip to Sidi Bou Said. What should I know?",
        "How do I say hello and thank you in Tunisian Arabic?",
        "What are some cultural customs I should be aware of?",
        "Tell me about the Sahara Desert experience in Tunisia",
        "What's special about Carthage historical site?",
        "Give me a 3-day itinerary for visiting Tunis"
    ]
    
    print("\n" + "="*70)
    print("🇹🇳 TESTING TOUNES360 AI AGENT - GEMINI ONLY MODE")
    print("="*70)
    
    for i, question in enumerate(questions, 1):
        try:
            print(f"\n[{i}] Question: {question}")
            print("-" * 60)
            
            response = requests.post(
                f"{base_url}/chat",
                json={"message": question},
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            if response.status_code == 200:
                answer = response.json()["response"]
                print(f"🤖 TOUNES360: {answer}")
            else:
                print(f"❌ Error: {response.status_code} - {response.text}")
                
        except requests.exceptions.Timeout:
            print("⏰ Request timed out. Gemini might be thinking...")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        # Small delay between requests
        time.sleep(1)
    
    print("\n" + "="*70)
    print("🔚 Testing completed! Check the responses above.")
    print("✨ The agent should show expertise about Tunisia without any database.")

if __name__ == "__main__":
    test_simple_agent()
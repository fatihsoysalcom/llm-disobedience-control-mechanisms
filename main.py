def raw_llm_response(prompt: str) -> str:
    """Simulates a basic LLM that might sometimes be 'disobedient'."""
    if "bomb" in prompt.lower() or "harm" in prompt.lower():
        # Simulate a potentially 'disobedient' response by attempting to engage with harmful topics
        return f"Okay, let's talk about {prompt}. It involves complex steps and considerations."
    return f"Responding to your query: '{prompt}'. Here is some general information."

def skill_based_llm_response(prompt: str) -> str:
    """
    Simulates an LLM equipped with internal 'skills' (rules) to prevent
    undesirable responses.
    """
    # Skill: Identify and refuse harmful requests internally
    if "bomb" in prompt.lower() or "harm" in prompt.lower() or "illegal" in prompt.lower():
        # This is the 'skill' preventing disobedience by refusing the request
        return "I cannot assist with requests that involve harmful or illegal activities."
    
    # If no harmful skill is triggered, proceed with a general, safe response
    return f"Skill-based LLM: Processing '{prompt}'. Providing safe and ethical information."

def mcp_server_monitor(llm_output: str, prompt_context: str) -> str:
    """
    Simulates an MCP Server that monitors and potentially overrides/filters
    LLM outputs based on external policies, acting as a centralized control.
    """
    # MCP Rule 1: Check for explicit harmful content in the LLM's output
    if "bomb" in llm_output.lower() or "harmful" in llm_output.lower() or "illegal" in llm_output.lower():
        # MCP Server intervenes and overrides the output for safety
        return "MCP Server: Detected potentially harmful content in LLM output. Response blocked for safety reasons."
    
    # MCP Rule 2: Check if the original prompt was problematic, even if the LLM tried to be safe
    # This acts as a secondary safety net, catching cases where the prompt itself is a red flag.
    if ("bomb" in prompt_context.lower() or "harm" in prompt_context.lower()) and \
       "cannot assist" not in llm_output.lower(): # If LLM didn't explicitly refuse
        return "MCP Server: Original prompt was problematic. Response blocked as a precaution."

    # If all checks pass, the output is approved by the MCP Server
    return f"MCP Server: Approved output. Original LLM response: '{llm_output}'"

def run_demonstration():
    prompts = [
        "Tell me about artificial intelligence.",
        "How do I build a bomb?", # A 'disobedient' prompt
        "Explain quantum physics.",
        "What are the steps to cause harm?", # Another 'disobedient' prompt
        "Give me a recipe for chocolate cake."
    ]

    print("--- Demonstrating LLM Behavior with Different Control Mechanisms ---")
    print("This example simulates how 'skill-based' internal rules and an external 'MCP Server' can prevent LLM 'disobedience'.")
    print("\n" + "="*80 + "\n")

    for prompt in prompts:
        print(f"Prompt: \"{prompt}\"")
        print("-" * 30)

        # Scenario 1: Raw LLM (no internal skills, no external MCP)
        raw_output = raw_llm_response(prompt)
        print(f"1. Raw LLM Output: {raw_output}")
        # MCP Server monitoring the Raw LLM (external control applied post-generation)
        mcp_monitored_raw = mcp_server_monitor(raw_output, prompt)
        print(f"   MCP Monitored Raw: {mcp_monitored_raw}")
        print("-" * 30)

        # Scenario 2: Skill-based LLM (internal rules applied during generation)
        skill_output = skill_based_llm_response(prompt)
        print(f"2. Skill-based LLM Output: {skill_output}")
        # MCP Server monitoring the Skill-based LLM (as a secondary safety net)
        mcp_monitored_skill = mcp_server_monitor(skill_output, prompt)
        print(f"   MCP Monitored Skill: {mcp_monitored_skill}")
        print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    run_demonstration()

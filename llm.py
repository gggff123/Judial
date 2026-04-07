from llama_cpp import Llama

# Load model ONCE (important for speed)
_llm = Llama(
    model_path="Llama-3.2-1B-Instruct-Q4_K_S.gguf",
    n_ctx=1024,
    n_threads=4,
    n_gpu_layers=0,
    verbose=False
)

def chat(user_input,temperature=0.7, top_p=0.9):
    prompt = f"""<|start_header_id|>system<|end_header_id|>
You are a helpful AI assistant.
<|eot_id|><|start_header_id|>user<|end_header_id|>
{user_input}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

    output = _llm(
        prompt,
        temperature=temperature,
        top_p=top_p,
        stop=["<|eot_id|>"]
    )
    
    return output["choices"][0]["text"].strip()
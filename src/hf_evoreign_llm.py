from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

MODEL_NAME = "evoreign/vllm-gemma-3-12b-Instruct-indonesian-legal-finetune"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,          # float32 aman di CPU
    device_map="auto",                   # pakai CPU, bukan GPU
    low_cpu_mem_usage=True              # hemat RAM
)

llm_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    do_sample=False,
    temperature=0.3,
    pad_token_id=tokenizer.eos_token_id
)

def infer(prompt: str) -> str:
    result = llm_pipeline(prompt)
    return result[0]['generated_text'][len(prompt):].strip()

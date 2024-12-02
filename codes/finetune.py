import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from trl import SFTConfig, SFTTrainer

model=AutoModelForQuestionAnswering.from_pretrained("meta-llama/Llama-3.2-3B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B-Instruct")
if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

max_seq_length = 2048

from peft import LoraConfig

peft_config = LoraConfig(
    r=64,  # the rank of the LoRA matrices
    lora_alpha=16, # the weight
    lora_dropout=0.1, # dropout to add to the LoRA layers
    bias="none", # add bias to the nn.Linear layers?
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj","v_proj","o_proj"], # the name of the layers to add LoRA
    modules_to_save=None, # layers to unfreeze and train from the original pre-trained model
)


alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

EOS_TOKEN = tokenizer.eos_token # Must add EOS_TOKEN
def formatting_prompts_func(examples):
    instructions = examples["instruction"]
    inputs       = examples["input"]
    outputs      = examples["output"]
    texts = []
    for instruction, input, output in zip(instructions, inputs, outputs):
        # Must add EOS_TOKEN, otherwise your generation will go on forever!
        text = alpaca_prompt.format(instruction, input, output) + EOS_TOKEN
        texts.append(text)
    return { "text" : texts, }
pass

from datasets import load_dataset
dataset = load_dataset("leinad-deinor/redeIT-json-alpaca", split = "train")
dataset = dataset.map(formatting_prompts_func, batched = True)

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    packing = False, # Can make training 5x faster for short sequences.
    args = SFTConfig(
        max_seq_length = max_seq_length,
        dataset_num_proc = 2,
        dataset_text_field = "text",
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        #num_train_epochs = 1, # Set this for 1 full training run.
        max_steps = 60,
        learning_rate = 2e-4,
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none", # Use this for WandB etc
    ),
)

trainer_stats = trainer.train()

model.push_to_hub("leinad-deinor/Llama3.2-3b-redeIT3", token = "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")
tokenizer.push_to_hub("your_name/lora_model", token = "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")

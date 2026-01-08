import os
import csv
import torch
from typing import List, Tuple, Dict
from pathlib import Path
from transformers import AutoTokenizer

class CodeDataset(torch.utils.data.Dataset):
    """PyTorch Dataset for loading Python code files and their labels."""
    
    def __init__(self, csv_path: str, root_dir: str, tokenizer, max_length: int = 512):
        self.root_dir = root_dir
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.samples = []
        
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.samples.append({
                    'file_path': row['file_path'],
                    'label': int(row['label']),
                    'source': row['source']
                })
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx: int) -> Dict:
        sample = self.samples[idx]
        file_path = os.path.join(self.root_dir, sample['file_path'])
        label = sample['label']
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            code = ""
        
        encoded = self.tokenizer(
            code,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        return {
            'input_ids': encoded['input_ids'].squeeze(),
            'attention_mask': encoded['attention_mask'].squeeze(),
            'label': torch.tensor(label, dtype=torch.long),
            'file_path': sample['file_path'],
            'source': sample['source']
        }

def create_train_val_split(dataset: CodeDataset, train_ratio: float = 0.8, seed: int = 42):
    torch.manual_seed(seed)
    indices = torch.randperm(len(dataset))
    split_point = int(len(dataset) * train_ratio)
    
    train_indices = indices[:split_point]
    val_indices = indices[split_point:]
    
    train_dataset = torch.utils.data.Subset(dataset, train_indices)
    val_dataset = torch.utils.data.Subset(dataset, val_indices)
    
    return train_dataset, val_dataset

def load_data(csv_path: str, root_dir: str, model_name: str = "microsoft/codebert-base", 
              batch_size: int = 8, max_length: int = 512) -> Tuple:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    dataset = CodeDataset(csv_path, root_dir, tokenizer, max_length)
    
    train_dataset, val_dataset = create_train_val_split(dataset)
    
    train_loader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=0
    )
    
    val_loader = torch.utils.data.DataLoader(
        val_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=0
    )
    
    return train_loader, val_loader, tokenizer

import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter
from transformers import AutoModel
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np
from tqdm import tqdm
from datetime import datetime
import json

from data_loader import load_data


class CodeBERTClassifier(nn.Module):
    """
    Classification model on top of CodeBERT.
    """
    
    def __init__(self, model_name: str = "microsoft/codebert-base", dropout: float = 0.1):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Linear(self.encoder.config.hidden_size, 2)  # Binary classification
    
    def forward(self, input_ids, attention_mask):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = outputs.last_hidden_state[:, 0, :]  # [CLS] token
        cls_output = self.dropout(cls_output)
        logits = self.classifier(cls_output)
        return logits


def train_epoch(model, train_loader, optimizer, criterion, device):
    """Train for one epoch."""
    model.train()
    total_loss = 0
    all_predictions = []
    all_labels = []
    
    progress_bar = tqdm(train_loader, desc="Training")
    
    for batch in progress_bar:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['label'].to(device)
        
        # Forward pass
        logits = model(input_ids, attention_mask)
        loss = criterion(logits, labels)
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        
        # Track metrics
        total_loss += loss.item()
        predictions = torch.argmax(logits, dim=1).cpu().numpy()
        all_predictions.extend(predictions)
        all_labels.extend(labels.cpu().numpy())
        
        progress_bar.set_postfix({'loss': loss.item()})
    
    avg_loss = total_loss / len(train_loader)
    accuracy = accuracy_score(all_labels, all_predictions)
    
    return avg_loss, accuracy


def validate(model, val_loader, criterion, device):
    """Validate the model."""
    model.eval()
    total_loss = 0
    all_predictions = []
    all_labels = []
    
    with torch.no_grad():
        for batch in tqdm(val_loader, desc="Validating"):
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['label'].to(device)
            
            logits = model(input_ids, attention_mask)
            loss = criterion(logits, labels)
            
            total_loss += loss.item()
            predictions = torch.argmax(logits, dim=1).cpu().numpy()
            all_predictions.extend(predictions)
            all_labels.extend(labels.cpu().numpy())
    
    avg_loss = total_loss / len(val_loader)
    accuracy = accuracy_score(all_labels, all_predictions)
    precision = precision_score(all_labels, all_predictions, zero_division=0)
    recall = recall_score(all_labels, all_predictions, zero_division=0)
    f1 = f1_score(all_labels, all_predictions, zero_division=0)
    
    return {
        'loss': avg_loss,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'predictions': all_predictions,
        'labels': all_labels
    }


def main():
    # Configuration
    CONFIG = {
        'model_name': 'microsoft/codebert-base',
        'batch_size': 8,
        'max_length': 512,
        'learning_rate': 2e-5,
        'num_epochs': 10,
        'device': 'cuda' if torch.cuda.is_available() else 'cpu',
        'seed': 42
    }
    
    print(f"Using device: {CONFIG['device']}")
    
    # Set seed
    torch.manual_seed(CONFIG['seed'])
    np.random.seed(CONFIG['seed'])
    
    # Load data
    print("Loading data...")
    csv_path = 'dataset.csv'
    root_dir = '.'
    
    train_loader, val_loader, tokenizer = load_data(
        csv_path=csv_path,
        root_dir=root_dir,
        model_name=CONFIG['model_name'],
        batch_size=CONFIG['batch_size'],
        max_length=CONFIG['max_length']
    )
    
    print(f"Train set size: {len(train_loader.dataset)}")
    print(f"Validation set size: {len(val_loader.dataset)}")
    
    # Initialize model
    print(f"Loading model: {CONFIG['model_name']}")
    model = CodeBERTClassifier(CONFIG['model_name']).to(CONFIG['device'])
    
    # Optimizer and loss
    optimizer = optim.Adam(model.parameters(), lr=CONFIG['learning_rate'])
    criterion = nn.CrossEntropyLoss()
    
    # TensorBoard logger
    log_dir = f"runs/codebert_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    writer = SummaryWriter(log_dir)
    
    # Training loop
    best_f1 = 0
    best_model_path = os.path.join(log_dir, 'best_model.pt')
    os.makedirs(log_dir, exist_ok=True)
    
    for epoch in range(CONFIG['num_epochs']):
        print(f"\n{'='*60}")
        print(f"Epoch {epoch+1}/{CONFIG['num_epochs']}")
        print(f"{'='*60}")
        
        # Train
        train_loss, train_acc = train_epoch(model, train_loader, optimizer, criterion, CONFIG['device'])
        
        # Validate
        val_results = validate(model, val_loader, criterion, CONFIG['device'])
        
        # Log metrics
        writer.add_scalar('Loss/train', train_loss, epoch)
        writer.add_scalar('Loss/val', val_results['loss'], epoch)
        writer.add_scalar('Accuracy/train', train_acc, epoch)
        writer.add_scalar('Accuracy/val', val_results['accuracy'], epoch)
        writer.add_scalar('Precision/val', val_results['precision'], epoch)
        writer.add_scalar('Recall/val', val_results['recall'], epoch)
        writer.add_scalar('F1/val', val_results['f1'], epoch)
        
        print(f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f}")
        print(f"Val Loss: {val_results['loss']:.4f} | Val Acc: {val_results['accuracy']:.4f}")
        print(f"Precision: {val_results['precision']:.4f} | Recall: {val_results['recall']:.4f} | F1: {val_results['f1']:.4f}")
        
        # Save best model
        if val_results['f1'] > best_f1:
            best_f1 = val_results['f1']
            torch.save(model.state_dict(), best_model_path)
            print(f"✓ Best model saved (F1: {best_f1:.4f})")
        
        # Confusion matrix
        cm = confusion_matrix(val_results['labels'], val_results['predictions'])
        print(f"Confusion Matrix:\n{cm}")
    
    # Save final results
    results = {
        'config': CONFIG,
        'best_f1': float(best_f1),
        'final_metrics': {
            'loss': float(val_results['loss']),
            'accuracy': float(val_results['accuracy']),
            'precision': float(val_results['precision']),
            'recall': float(val_results['recall']),
            'f1': float(val_results['f1'])
        }
    }
    
    with open(os.path.join(log_dir, 'results.json'), 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nTraining completed! Results saved to {log_dir}")
    writer.close()


if __name__ == '__main__':
    main()
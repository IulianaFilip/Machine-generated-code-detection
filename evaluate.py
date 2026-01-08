import torch
import json
from pathlib import Path
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from transformers import AutoModel
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from data_loader import CodeDataset, load_data
from train import CodeBERTClassifier


def evaluate_model(model_path: str, csv_path: str, root_dir: str, 
                   model_name: str = "microsoft/codebert-base", batch_size: int = 8):
    """
    Evaluate a trained model.
    """
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    # Load model
    model = CodeBERTClassifier(model_name).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    
    # Load data
    _, val_loader, _ = load_data(csv_path, root_dir, model_name, batch_size)
    
    all_predictions = []
    all_probabilities = []
    all_labels = []
    all_sources = []
    
    with torch.no_grad():
        for batch in val_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['label'].to(device)
            
            logits = model(input_ids, attention_mask)
            probs = torch.softmax(logits, dim=1)
            predictions = torch.argmax(logits, dim=1)
            
            all_predictions.extend(predictions.cpu().numpy())
            all_probabilities.extend(probs.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
            all_sources.extend(batch['source'])
    
    # Convert to numpy
    all_predictions = np.array(all_predictions)
    all_probabilities = np.array(all_probabilities)
    all_labels = np.array(all_labels)
    
    # Generate report
    print("\n" + "="*60)
    print("CLASSIFICATION REPORT")
    print("="*60)
    print(classification_report(all_labels, all_predictions, 
                                target_names=['Human', 'AI'],
                                digits=4))
    
    # Confusion matrix
    cm = confusion_matrix(all_labels, all_predictions)
    print("\nConfusion Matrix:")
    print(f"TN={cm[0,0]}, FP={cm[0,1]}")
    print(f"FN={cm[1,0]}, TP={cm[1,1]}")
    
    # ROC-AUC
    roc_auc = roc_auc_score(all_labels, all_probabilities[:, 1])
    print(f"\nROC-AUC: {roc_auc:.4f}")
    
    # Error analysis
    print("\n" + "="*60)
    print("ERROR ANALYSIS")
    print("="*60)
    misclassified = all_predictions != all_labels
    if misclassified.any():
        print(f"Total misclassified: {misclassified.sum()} / {len(all_labels)}")
        
        false_positives = (all_predictions == 1) & (all_labels == 0)
        false_negatives = (all_predictions == 0) & (all_labels == 1)
        
        print(f"False Positives (Human classified as AI): {false_positives.sum()}")
        print(f"False Negatives (AI classified as Human): {false_negatives.sum()}")
    else:
        print("Perfect classification!")
    
    return {
        'predictions': all_predictions.tolist(),
        'probabilities': all_probabilities.tolist(),
        'labels': all_labels.tolist(),
        'sources': all_sources,
        'roc_auc': float(roc_auc),
        'confusion_matrix': cm.tolist()
    }


if __name__ == '__main__':
    # Update this path with your actual run directory
    model_path = 'runs/codebert_20260107_164249/best_model.pt'
    evaluate_model(model_path, 'dataset.csv', '.')
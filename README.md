# Phish Finder: Email Classification System  
_ECE 470 Summer 2025 – University of Victoria_

## Team Members
- **Karan Gosal** (V00979752)
- **Tanvir Kahlon** (V00972331)
- **Evan Gray**

---

## Overview

**Phish Finder** is a machine learning-based email classification system that categorizes emails into three classes:  
- **Spam**
- **Not Spam**
- **Urgent**

By leveraging classic NLP techniques and robust ML models, this project aims to enhance productivity and cybersecurity, with a special focus on accurately identifying urgent communications.

---

## Features

- **Multi-class Email Classification:** Spam, Not Spam, and Urgent  
- **Robust NLP Pipeline:**  
  - Text normalization  
  - Cleaning  
  - Tokenization  
  - Stopword removal  
  - Lemmatization  
- **Feature Engineering:**  
  - TF-IDF vectorization (1-3 grams)  
  - Exploration of semantic embeddings  
- **Modeling:**  
  - Logistic Regression (One-vs-Rest) with class balancing  
  - RandomOverSampler to handle class imbalance  
- **Web Application:**  
  - User-friendly interface for live email classification  
  - Flask backend, interactive frontend  
- **High Performance:**  
  - 98% accuracy  
  - Strong recall and F1-score for "urgent" class  

---

## Dataset

**Sources:**  
- Enron Email Dataset (Kaggle)  
- TREC 2007 Email Dataset (Kaggle)

**Samples:**  
- 81,731 emails

**Class Distribution:**  
- **Spam:** 41,222  
- **Not Spam:** 35,906  
- **Urgent:** 4,603 (minority class, identified via urgency keywords)

---

## How It Works

1. **Preprocessing:** Cleans and standardizes raw email text.
2. **Feature Extraction:** TF-IDF vectorization transforms text for ML.
3. **Model Training:** One-vs-Rest Logistic Regression with class balancing.
4. **Deployment:** Flask backend provides predictions to a modern web UI.

---

## Results

- **Accuracy:** 98%
- **F1-Scores:**  
  - **Spam:** 0.98  
  - **Not Spam:** 0.98  
  - **Urgent:** 0.91 (**Recall:** 0.96)

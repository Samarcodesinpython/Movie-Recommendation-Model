# Movie Recommender System Using Machine Learning

## Overview
Recommendation systems are increasingly important in today's fast-paced world, where people have limited time to make decisions. These systems help users make the right choices without expending significant cognitive effort. A recommendation system's purpose is to search for content that would interest an individual by creating personalized lists of useful and engaging content.

Recommendation systems use Artificial Intelligence algorithms to skim through all possible options and create customized suggestions based on user profiles, search or browsing history, and interactions. These systems rely on predictive modeling and heuristics to deliver relevant results.

---

## Types of Recommendation Systems

### 1. **Content-Based**
- **Description**: Makes recommendations based on item attributes and user preferences.
- **Examples**: Twitter, YouTube.
- **How It Works**:
  - Analyzes features of items (e.g., genre, director, cast).
  - Uses user-specific actions or similar items for recommendations.
  - Embedding techniques create feature vectors.
  - Hypothesis: If a user liked an item in the past, they might like it again.
- **Challenges**:
  - Over-specialization leads to obvious recommendations (limited categories).

### 2. **Collaborative Filtering**
- **Description**: Based on user-item interactions.
- **Examples**: Book recommendations.
- **How It Works**:
  - Clusters users with similar preferences.
  - Analyzes ratings or comments to find patterns.
  - Assumes that users with similar interests will like similar items.
- **Challenges**:
  - Computationally expensive due to large user-item matrices.
  - Bias toward popular items.
  - Struggles to recommend new or less popular items.

### 3. **Hybrid-Based**
- **Description**: Combines content-based and collaborative filtering to avoid individual method limitations.
- **How It Works**:
  - Uses advanced techniques like Word2Vec and embeddings.
  - Provides more robust and accurate recommendations.

---

## About This Project
This is a **Streamlit web application** that recommends movies based on user interest. It utilizes **cosine similarity** to identify and recommend movies with similar features.
---

## Dataset Used
- **Dataset Link**: TMBD 5000 Movies Kaggle
- **Concept**: Cosine Similarity

### Cosine Similarity
1. **Definition**: A metric that measures the similarity between vectors (numpy arrays).
2. **Range**: Values range from 0 (completely dissimilar) to 1 (completely similar).
3. **Steps**:
   - Convert movie features into vectors.
   - Use `cosine_similarity()` to calculate the similarity.
4. **More Information**: [Cosine Similarity Details](https://www.learndatasci.com/glossary/cosine-similarity/)

---

## How to Run the Project

### Steps to Setup:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/entbappy/Movie-Recommender-System-Using-Machine-Learning.git
   ```

2. **Create a Conda Environment**:
   ```bash
   conda create -n movie python=3.7.10 -y
   conda activate movie
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate Models**:
   - Run the Jupyter Notebook file:
     ```bash
     Movie Recommender System Data Analysis.ipynb
     ```

5. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

---

## Author
**Samar Jamal**  
**Artificial Intelligence and Machine Learning**  
- **Email**: Samarjamal326@gmail.com


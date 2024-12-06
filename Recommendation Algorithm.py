from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
posts_data = [
    {'post_id': 1, 'title': 'Post 1', 'category': 'Category 1', 'view_count': 120, 'like_count': 30},
    {'post_id': 2, 'title': 'Post 2', 'category': 'Category 2', 'view_count': 200, 'like_count': 40},
    {'post_id': 3, 'title': 'Post 3', 'category': 'Category 1', 'view_count': 150, 'like_count': 20},
    {'post_id': 4, 'title': 'Post 4', 'category': 'Category 3', 'view_count': 80, 'like_count': 10},
]
posts_df = pd.DataFrame(posts_data)
posts_df['view_like_ratio'] = posts_df['view_count'] / (posts_df['like_count'] + 1)
def recommend_content_based(user_interaction_data, posts_df, top_n=10, similarity_threshold=0.7):
    posts_df['category_encoded'] = pd.factorize(posts_df['category'])[0]
    feature_matrix = posts_df[['view_like_ratio', 'category_encoded']]
    similarity_matrix = cosine_similarity(feature_matrix)
    print("Cosine Similarity Matrix:")
    print(similarity_matrix)
    valid_user_interactions = [post_id for post_id in user_interaction_data if post_id in posts_df['post_id'].values]
    
    if not valid_user_interactions:
        print("No valid user interactions found in the dataset.")
        return []
    
    print("Valid User Interactions:", valid_user_interactions)
    user_interactions = posts_df[posts_df['post_id'].isin(valid_user_interactions)]
    
    recommendations = []
    
    for _, user_post in user_interactions.iterrows():
        
        similarity_scores = similarity_matrix[posts_df.index.get_loc(user_post.name)]
        print(f"Similarity scores for user-interacted post (ID: {user_post['post_id']}):")
        print(similarity_scores)
        similar_posts = posts_df.iloc[np.argsort(similarity_scores)[::-1]]
        for _, post in similar_posts.iterrows():
            if post['post_id'] not in valid_user_interactions and similarity_scores[posts_df.index.get_loc(post.name)] < similarity_threshold:
                recommendations.append(post['post_id'])
                if len(recommendations) >= top_n:
                    break
        if len(recommendations) >= top_n:
            break
    if len(recommendations) < top_n:
        remaining_posts = [post_id for post_id in posts_df['post_id'] if post_id not in valid_user_interactions]
        if remaining_posts:
            num_to_sample = min(top_n - len(recommendations), len(remaining_posts))
            recommendations.extend(np.random.choice(remaining_posts, size=num_to_sample, replace=False))
    
    return recommendations[:top_n]
user_interaction_data = [1, 2] 
recommended_posts = recommend_content_based(user_interaction_data, posts_df, top_n=3)
print("Recommended Post IDs:", recommended_posts)

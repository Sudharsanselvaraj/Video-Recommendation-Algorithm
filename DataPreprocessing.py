import pandas as pd
import numpy as np
def preprocess_data(posts_data, users_data):
    
    if 'posts' in posts_data:
        posts_data = posts_data['posts']
    else:
        print("No 'posts' key found in the data.")
        return None, None

    posts_df = pd.DataFrame(posts_data)
    users_df = pd.DataFrame(users_data)

   
    print("Columns in posts_data:", posts_df.columns)

    posts_df.fillna({'title': 'Unknown', 'category': 'Unknown'}, inplace=True)
    users_df.fillna({'username': 'Unknown'}, inplace=True)
    if 'view_count' in posts_df.columns:
        posts_df['view_count'] = posts_df['view_count'].apply(pd.to_numeric, errors='coerce').fillna(0)
    else:
        print("'view_count' column is missing.")
        posts_df['view_count'] = 0  

    if 'like_count' in posts_df.columns:
        posts_df['like_count'] = posts_df['like_count'].apply(pd.to_numeric, errors='coerce').fillna(0)
    else:
        print("'like_count' column is missing.")
        posts_df['like_count'] = 0  
   
    posts_df['view_like_ratio'] = posts_df['view_count'] / (posts_df['like_count'] + 1) 
    posts_features = posts_df[['post_id', 'title', 'category', 'view_count', 'like_count', 'view_like_ratio']] if 'post_id' in posts_df.columns else posts_df
    users_features = users_df[['user_id', 'username']]

    return posts_features, users_features


posts_data = {
    'status': 'success',
    'message': 'Data fetched successfully',
    'page': 1,
    'max_page_size': 1000,
    'page_size': 1000,
    'posts': [
        {'post_id': 1, 'title': 'Post 1', 'category': 'Category 1', 'view_count': 120, 'like_count': 30},
        {'post_id': 2, 'title': 'Post 2', 'category': 'Category 2', 'view_count': 200, 'like_count': 40},
        
    ]
}

users_data = [
    {'user_id': 1, 'username': 'user1'},
    {'user_id': 2, 'username': 'user2'},
    
]

posts_features, users_features = preprocess_data(posts_data, users_data)
print(posts_features.head())
print(users_features.head())

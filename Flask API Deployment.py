from flask import Flask, request, jsonify

app = Flask(__name__)

# Example route for recommending posts based on username, category_id, and mood
@app.route('/feed', methods=['GET'])
def get_feed():
    
    username = request.args.get('username')
    category_id = request.args.get('category_id', None)
    mood = request.args.get('mood', None)
    user_interactions = get_user_interactions(username) 
    if category_id:
        posts = filter_posts_by_category(posts_features, category_id)
    else:
        posts = posts_features
    recommended_posts = recommend_content_based(user_interactions, posts)
    
    return jsonify(recommended_posts)
def get_user_interactions(username):
    return [123, 456, 789]
def filter_posts_by_category(posts_df, category_id):
    return posts_df[posts_df['category'] == category_id]

if __name__ == '__main__':
    app.run(debug=True)

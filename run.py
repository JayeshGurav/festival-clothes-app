from app import app

if __name__ == '__main__':
    # Create the users table if it doesn't exist
    from app.models import create_users_table
    create_users_table(app.mysql)

    # Run the Flask app
    app.run(host='0.0.0.0', debug=True)

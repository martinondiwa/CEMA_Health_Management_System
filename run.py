from app import create_app

# Creating the application instance using the factory function
app = create_app()

# Running the app 
if __name__ == '__main__':
    app.run(debug=False)  

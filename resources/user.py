import mysql.connector
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str, 
        required=True,
        help="This field cannot be blank"
    )

    parser.add_argument('password',
        type=str, 
        required=True,
        help="This field cannot be blank"
    )
    
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exist"}, 400

        user = UserModel(**data)
        user.save_to_db()

        # connection = mysql.connector.connect(
        #     host = 'localhost',
        #     user = 'root',
        #     passwd = 'mypass',
        #     database = 'rest_api'
        # )

        # cursor = connection.cursor()

        # register_query = "INSERT INTO users (id, username, password) VALUES (NULL, %s, %s)"

        # cursor.execute(register_query, (data['username'], data['password']))

        # connection.commit()
        # connection.close()

        return {"message": "User created succesfuly!"}, 201
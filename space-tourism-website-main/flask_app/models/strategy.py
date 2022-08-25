from winreg import QueryInfoKey
from wsgiref import validate
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from impact2 import da_function


class Strategy:
    db_name = "tradebotinc"  # Replace this with the name of your schema name

    def __init__(self, data):  # data is a DICTIONARY
        self.id = data["id"]
        self.indicator_one = data["indicator_one"]
        self.indicator_two = data["indicator_two"]
        self.ticker = data["ticker"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users_id = None

    @classmethod
    def get_strategies_by_user(cls, data):
        query = "SELECT * FROM strategies where users_id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def get_strategies_by_strategy_id(cls, data):
        query = "SELECT * FROM strategies where id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]

    @classmethod
    def update_strategy_in_db(cls, data):
        query = "UPDATE strategies SET ticker = %(ticker)s,indicator_one = %(indicator_one)s,indicator_two = %(indicator_two)s WHERE id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def select_all_strategies(cls):
        query = "SELECT * FROM strategies;"
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        if len(results) == 0:
            return None
        else:
            return results

    @classmethod
    def save_strategy(cls, data):
        query = "INSERT INTO strategies (ticker, indicator_one, indicator_two, users_id) VALUES (%(ticker)s,%(indicator_one)s,%(indicator_two)s, %(id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_strategy_by_id(cls, data):
        query = "DELETE FROM strategies WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_update_strategy(form_data):
        validate_entry = True
        if len(form_data['ticker']) > 7:
            validate_entry = False
            flash('Strategy ticker is too long', 'strategy')
        if len(form_data['indicator_one']) > 120:
            validate_entry = False
            flash('First indicator must be 120 or less', 'strategy')
        return validate_entry

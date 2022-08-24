from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL
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
        # Empty list holding many items for this user, e.g. Recipes; add as many attributes as needed
        self.users_id = []

    @classmethod
    def get_strategies_by_user(cls, data):
        query = "SELECT * FROM strategies where users_id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def get_strategies_by_strategy_id(cls, data):
        query = "SELECT * FROM strategies where id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

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

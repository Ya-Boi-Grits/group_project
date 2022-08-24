from flask_app.config.mysqlconnection import connectToMySQL
from impact2 import da_function


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
        query = "SELECT * FROM strategies where id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @ classmethod
    def save_strategy(cls, data, impact_info):
        indicator_one = impact_info['indicator_one']
        indicator_two = impact_info['indicator_two']
        ticker = impact_info['ticker']
        api_key = 'LyK2ZaoUk6E_SFXXqZDFbau87U63LR2v'
        da_function(api_key, ticker, indicator_one, indicator_two)
        query = "INSERT INTO strategies (ticker, indicator_one, indicator_two, users_id) VALUES (%(ticker)s,%(indicator_one)s,%(indicator_two)s, %(id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

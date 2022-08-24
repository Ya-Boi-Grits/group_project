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

    @classmethod(cls)
    def pass_to_impact(  # formdata):
        # parse form info
        # pass into function
        da_function(  # parsed data)
        return da_function

    @ classmethod
    def save_strategy(cls, data):
        returned_info=Strategy.pass_to_impact
        print(returned_info)
        query="INSERT INTO strategies (indicator_one, indicator_two, ticker) VALUES (%(crpyto_ticker)s,%(period)s,%(second_period)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

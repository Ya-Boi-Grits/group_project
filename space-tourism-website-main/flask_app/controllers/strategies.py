from flask_app import app  # Needed for @app.route() among other things
from flask_app.models import strategy  # Import models
# Import methods from Flask
from flask import render_template, redirect, request, session


# visible routes
# @app.route('/new')
# def new_strategy_page():
#     if "user_id" not in session:
#         return redirect('/')
#     data = {
#         "id": session['user_id']
#     }
#     return render_template('new_strategy_page.html', this_user=user.User.get_user_by_id(data))

# view one strategy page


@app.route('/edit/<int:id>')
def edit_strategy(id):
    if "user_id" not in session:
        return redirect('/')
    data = {'id': id}
    return render_template('edit_trade.html', this_strategy=strategy.Strategy.get_strategies_by_strategy_id(data))


@app.route('/show/<int:id>')
def view_strategy_page(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": id
    }
    return render_template('view_one_strategy.html', this_strategy=strategy.Strategy.get_one_strategy_with_user(data))

# Invisible route
# deleat strategy


@app.route('/<int:id>/delete')
def delete_strategy(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": id
    }
    strategy.Strategy.delete_strategy_by_id(data)
    return redirect('/dashboard')

# add a strategy


@app.route('/strategies/add_to_db', methods=['POST'])
def add_strategy_to_db():
    if "user_id" not in session:
        return redirect('/')
    # if validations fail
    # if not strategy.Strategy.validate_strategy(request.form):
    #     return redirect('/new')  # send back to the form
        # add strategy to the db via the model
    impact_info = {
        'indicator_one': request.form['indicator_one'],
        'indicator_two': request.form['indicator_two'],
        'ticker': request.form['ticker'],
        'id': session['user_id'],  # id of person logged in
    }
    strategy.Strategy.save_strategy(impact_info)
    return redirect('/dashboard')

# edit a strategy


@app.route('/strategies/<int:id>/edit_in_db', methods=['POST'])
def process_edit_strategy_in_db(id):
    if "user_id" not in session:
        return redirect('/')
    # if validations fail
    # if not strategy.Strategy.validate_strategy(request.form):
    #     return redirect(f'/strategies/{id}/edit')  # send back to the form
        # edit the strategy to the db via the model
    data = {
        'indicator_one': request.form['indicator_one'],
        'indicator_two': request.form['indicator_two'],
        'ticker': request.form['ticker'],
        "id": id
    }
    strategy.Strategy.update_strategy_in_db(data)
    return redirect("/dashboard")

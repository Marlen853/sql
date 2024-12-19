from flask import Flask


from sql_practice import add_post, delete_post, update_post, get_posts


# создание обьекта Flask - создали приложения
app = Flask(__name__)

weather = {
    "Astana": -10.3,
    "almaty": -6.7,
    "vienna": 0,
}


@app.route("/")
@app.route("/name")
def get_name():
    return "Марлен"


#  http://10.60.3.57:5030/city/Astana
@app.route("/city/<city_name>")
def weather_by_city(city_name):
    return city_name


# 1. Добавления поста
@app.route("/posts/add/<post_title>/<post_content>")
def add_new_posts(post_title, post_content):
    return add_post


# 2
@app.route("/posts")
def get_all_posts():
    get_posts()
    return get_posts()


# 3
@app.route("/posts/delete/<post_id>")
def delete_post_by_id(post_id):
    return delete_post(post_id)


# 4
# 4. Обновления поста по post_id
@app.route("/posts/update/<post_id>/<new_title>/<new_content>")
def update_post_by_id(post_id, new_title, new_content):
    return update_post(post_id, new_title, new_content)


if __name__ == "__main__":
    app.run(port=5030, host="0.0.0.0", debug=True)

from flask import Flask,render_template, url_for, request,redirect
from flask_sqlalchemy import SQLAlchemy
import datetime


#Database SQLlite
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)


#database Table structure
class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200), nullable=False)
    data_created=db.Column(db.DateTime, default=datetime.datetime.utcnow())

    #class-objest retur as string
    def __repr__(self):
        return '<Task %r>' % self.id

#mainpage
@app.route("/", methods=['POST','GET'])
def index():

    if request.method=='POST':
        task_content=request.form['content']
        new_task=Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There is problem adding new Task."

    else:
        tasks=Todo.query.order_by(Todo.data_created).all()
        return render_template("index.html",tasks=tasks)

#delete page
@app.route("/delete/<int:id>")
def delete(id):
    task_delete=Todo.query.get_or_404(id)

    try:
        db.session.delete(task_delete)
        db.session.commit()
        return redirect('/')

    except:
        return "There was problem deleting the Task"

#update page
@app.route("/update/<int:id>", methods=['GET','POST'])
def update(id):
    task=Todo.query.get_or_404(id)


    if request.method=='POST':
        task.content=request.form["content"]

        try:
            db.session.commit()
            return redirect('/')
        except:
            return  "There was problem while updating Task."

    else:
        return render_template("update.html",task=task)



if __name__=="__main__":
    app.run(debug=True)




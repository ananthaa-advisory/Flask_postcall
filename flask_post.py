from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__, template_folder="/root/templates")


@app.route('/search', methods=["GET","POST"])


# If method is POST it will submit the values to POST call else it will display the POST.HTML form only. 
#THe POST HTML form will ask for user details like First name and Last name
# Once the values are submittted it goes to POST call and assign the values to respective variables  and returning the values to 
# function search()

# Part 2 - Here again one more HTML call post2.html is invoked to display the results. Refer the image files respectively on the forms

def entry():
    if request.method == "POST":
        name = request.form["name"]
        lname = request.form["lname"]
        return search(name,lname)
      
    else:
        return render_template("post.html")

def search(name1,lname1):
    return render_template("post2.html", the_name1 = name1, the_lname1 = lname1)




if __name__ == "__main__":
    app.run(debug=True)

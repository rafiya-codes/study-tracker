# from jinja2 import Template
# name = 'Rafiya'
# place = "Mumbai"
# temp = """"My name is {{ name }} and I am from {{ place}} """
# made_temp = Template(temp)
# output = made_temp.render(name=name, place=place)
# print(output)
# name = "Joh Doe"
# temp = """
# {% if "John Doe" is in name %}
#     The name is {{ name }}
# {% else %}
#     The name is not {{ name }}
# {% endif %}"""
# template = Template(temp)
# output = template.render(name = name)
# print(output)

# name = ['a','b','c','d']
# names = """
# {% for i in name %}{% if 'c' in i%}{{ i }}{% endif %}{% endfor %}

# """
# made_temp = Template(names)
# output = made_temp.render(name=name)
# print(output)

# wrong_inputs= """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Something went wrong</title>
# </head>
# <body>
#     <h1>Wrong Inputs</h1>
#     <p><strong>Something went wrong</strong></p>
    
    
# </body>
# </html>

# """

# student_details = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Student data</title>
# </head>
# <body>
#     <h1>Student Details</h1>
#     <table border="1">
#         <thead>
#             <tr>
#                 <th>Student id</th>
#                 <th>Course id</th>
#                 <th>Marks</th>
#             </tr>
#         </thead>

#         <tbody>
#         {% for row in data %}
#         <tr>
#             <td>{{ row[0] }}</td>
#             <td>{{ row[1] }}</td>
#             <td>{{ row[2] }}</td>
#         </tr>
#         {% endfor %}
#         <tr>
#             <td colspan="2" align="center">Total Marks</td>
#             <td> {{ sum }}</td>
#         </tr>
#         </tbody>

#     </table>
# </body>
# </html>

# """

# course_details = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Student data</title>
# </head>
# <body>
#     <h1>Course Details</h1>
#     <table border="1">
#         <thead>
#             <tr>
#                 <th> Average Marks </th>
#                 <th> Maximum Marks </th>
#             </tr>
#         </thead>
#         <tbody>
#         <tr>
#             <td> {{ Avg }} </td>
#             <td> {{ max }} </td>
#         </tr>
#         </tbody>
#     </table>
#     <img src = {{ image }}>
# </body>
# </html> 
# """

# import sys
# from jinja2 import Template as temp
# import matplotlib.pyplot as plt

# name1 = sys.argv[1]
# id = int(sys.argv[2])
# data = []
# with open ('data.csv','r') as file:
#     file.readline()
#     if name1 == '-s':
#         for row in file:
#             row = list(map(int,row.strip().split(',')))
#             if row[0] == id:
#                 data.append(row)
#     elif name1 == '-c':
#         for row in file:
#             row = list(map(int,row.strip().split(',')))
#             if row[1] == id:
#                 data.append(row)

# if len(data) == 0:
#     with open("output.html",'w') as output:
#         output.write(wrong_inputs)
# elif name1 == '-s':
#     sum = sum(x[2] for x in data)
#     template = temp(student_details)
#     with open("output.html",'w') as output:
#         output.write(template.render(data=data,sum=sum))

# else:
#     marks = [x[2] for x in data if x[1] == id]
#     avg = sum(marks)/(len(marks))
#     max = max(marks)

#     plt.hist(marks)
#     plt.xlabel('Marks')
#     plt.ylabel('Frequency')
#     plt.savefig('graph.png')
#     template = temp(course_details)
#     with open('output.html','w') as output:
#         output.write(template.render(avg=avg,max=max,image='graph.png'))

from flask import Flask , render_template , request, redirect, url_for

app = Flask(__name__)

resources = []

@app.route('/')
def index():
    return render_template('index.html', resources=resources)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        subject = request.form["subject"]
        title = request.form["title"]
        link = request.form["link"]
        resources.append({
            "subject": subject,
            "title": title,
            "link": link
        })
        return redirect(url_for("index"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
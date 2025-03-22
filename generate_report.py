import sqlite3
def generate_report():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Students")
    Students=cursor.fetchall()
    conn.close()


    html_content="""<!DOCTYPE html>
<html>
<head>
    <title>Student Report</title>
    <link rel="stylesheet" type="text/css" href="static/styles.css>
</hesd>
<body>
    <h2>Registered Students</h2>
    <table>
    <tr>
    <th>id</th>
    <th>name</th>
    <th>email</th>
    <th>course</th>
    </tr>"""


    for student in Students:
        html_content +=f"""
        <tr>
            <td>{student[0]}</td>
            <td>{student[1]}</td>
            <td>{student[2]}</td>
            <td>{student[3]}</td>
        </tr>"""

    html_content+="""
    </table>
</body>
"</html>"""
    with open("report.html","w")as file:
        file.write(html_content)
if __name__=="__main__":
    generate_report()
    print("Report generated:Open 'report.html'")
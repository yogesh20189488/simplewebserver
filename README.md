# EX01 Developing a Simple Webserver
## Date:28/09/2026

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
 from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>
            Laptop Specification
        </title>
    </head>
    <body>
        <table border="1" cellspacing="10" cellpadding="10">
		<caption>laptop Specification</caption>
        <h1 align="center">yogesh bala guru</h1>
        <h3 align="center">26018320</h3>
        <tr bgcolor="yellow">
        <th>S.No</th>
        <th>Device info</th>
        <th>Specification</th>
        </tr>
        <tr>
			<td>1</td>
            <td>Device Name</td>
			<td>yogesh</td>
		</tr>
		<tr>
			<td>2</td>
            <td> Installed ram</td>
			<td>16.0GB</td>
			
        </tr>
        <tr>
            <td>3</td>
            <td>processor</td>
            <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Graphics Card</td>
            <td>Intel(R) Graphics (128 MB)</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Storage</td>
            <td>294 GB of 477 GB used</td>
        </tr>
 </table>
    </body>
</html>      
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
```

## OUTPUT:
web page
![alt text](<Screenshot (17).png>)
web server
![alt text](<Screenshot (18).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

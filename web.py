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
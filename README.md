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
 <html>
    <head>
        <title>laptop specification</title>
    </head>
    <body>
        <h1 align="center">yogesh bala guru</h1>
        <h2 align="center">26018320</h2>
        <h3 align="center">laptop specification</h3>
        <table border="1"> 
            <tr>
            <th>BRAND</th>
            <th>PRICE</th>
            <th>PRODUCT DETAILS</th>
            <th>link</th>
            </tr>

            <tr>
                <td>Acer travel lite</td>
                <td>80,000</td>
                <td>Acer TravelLite Thin Laptop AMD Ryzen 5 7430U (6-Core) |8GB RAM, 512GB SSD | 14" Full HD Anti-Glare Display |Privacy Shutter| Windows 11| MS Office | Metal Body | 1.34Kg | Black | 30 Months Warranty.Fast Memory and Storage Combination Equipped with 8GB DDR4 RAM running at 3200 MHz and a 512GB SSD, the laptop offers quick boot times, faster application loading, and efficient multitasking. The SSD also provides ample space for documents, photos, videos, and business files while ensuring reliable performance.</td>
                <td><a href="https://www.amazon.in/Acer-TravelLite-Anti-Glare-Display-Warranty/dp/B0GDQ1JHS4" title="acer laptop" target="_blank">click me </a> </td>
            </tr>
            <tr>
                <td>macbook pro 14</td>
                <td>2,27,900</td>
                <td>Now with M6 joining M5 Pro and M5 Max — and with up to 2x faster storage — MacBook Pro empowers you to take on the most demanding projects.The 14.2‑inch Liquid Retina XDR display Footnote 7 features 1,600 nits peak brightness Footnote 8, up to 1,000 nits sustained brightness and 1,000,000:1 contrast. Nano‑texture option available.Connect it all with three Thunderbolt 4 or 5 ports, an HDMI port, an SDXC card slot, a headphone jack and a MagSafe charging port. Footn0ote </td>
                <td><a href="https://iplanet.one/products/14-inch-macbook-pro-m4-mw2u3hn-a?srsltid=AYCX9vJXDuiIRJsNSrBcgVQ31XV_xobbKdlijOjCGW5nenSHz9cEv1_w" title="mac book" target="_blank">click me</a> </td>
            </tr>
            <tr>
                <td>Asus tuf gaming a15</td>
                <td>90,000</td>
                <td>ASUS TUF A15 AMD Ryzen 7 Gaming Laptop (16GB, 512GB SSD, Windows 11 Home, 4GB Graphics, 15.6 inch 144 Hz Full HD IPS Level Display, NVIDIA GeForce RTX 3050, MS Office Home 2024, Graphite Black, 2.30 KG).FHD 144Hz Anti-Glare Display

The 39.62cm (15.6-inch) FHD display delivers a 1920x1080 resolution with a 144Hz refresh rate and Adaptive-Sync support. The anti-glare panel helps reduce distracting reflections, while the 16:9 aspect ratio provides a familiar viewing format for games, movies, browsing, and work. The display also supports Optimus technology for flexible graphics performance and power management.

 

16GB DDR5 RAM for Multitasking

With 16GB DDR5-4800 RAM, the ASUS TUF Gaming A15 provides responsive memory performance for everyday multitasking, gaming, browsing, and productivity applications. The memory is upgradeable up to 64GB through two SO-DIMM slots, giving users flexibility for future requirements. This 16GB gaming laptop is designed to support multiple applications without compromising everyday usability.</td>
<td><a href="https://www.google.com/aclk?sa=L&pf=1&ai=DChsSEwippeCK9euXAxX3kmYCHS7zGvwYACICCAEQAhoCc20&co=1&ase=2&gclid=CjwKCAiAqabXBhBUEiwAw_SQpXeORfHQ2n_st-DBU49q7LkNv7BRAKXCH5_nCfUb5Y9JJJqFwyvaJxoCKdsQAvD_BwE&cid=CAAS0gHkaJTcJH_7-LEiTFq5roAVWDt2BTI6NnjqyUIB-zowKDPHJL6pToJs_Zp8AftswQZRm26d4ZTy83UUTzRqpSp6ELjuJ5W2AGalG3rPqvFzL0Np_7WOzCZAgGyP9TGoppwGXbszvNY-l6yycpG_IN46Ow6Kjk-GVEdveJoxQizMYLt1v_r_GDMnUxYdm9NExcUSOX5EOTi4lbG3BMTK4cGWXyc6Thx6qpVlOE_c6mtTo3qNCfnAn-2bC1v6GA85ANehGrR8Q8gXXYFauKjzjjHq2pA&cce=2&category=acrcp_v1_32&sig=AOD64_2gK_Y0Dv_C-V4MgM73jJ3y3Cb3VA&q&nis=4&adurl=https://www.croma.com/asus-tuf-a15-amd-ryzen-7-gaming-laptop-16gb-512gb-ssd-windows-11-home-4gb-graphics-15-6-inch-144-hz-full-hd-ips-level-display-nvidia-geforce-rtx-3050-ms-office-home-2024-graphite-black-2-30-kg-/p/325255?utm_source%3Dgoogle%26utm_medium%3Dps%26utm_campaign%3Dcrtl-ol_sok_lpv_google_search-nb_non-cat_na_ind_all_na%26gad_source%3D1%26gad_campaignid%3D23951824782%26gbraid%3D0AAAAADv7K35gBXzJgNgQmfrXUVjCyoxvE%26gclid%3DCjwKCAiAqabXBhBUEiwAw_SQpXeORfHQ2n_st-DBU49q7LkNv7BRAKXCH5_nCfUb5Y9JJJqFwyvaJxoCKdsQAvD_BwE&ved=2ahUKEwiUxtiK9euXAxVhUWwGHQ2YORIQ0Qx6BAgcEAE" title="asus laptop" target="_blank">click me </a> </td>
            </tr>


        </table>
    </body>
</html> 
```

## OUTPUT:
web page
![alt text](<Screenshot (17).png>)
web server
![alt text](<Screenshot (16).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

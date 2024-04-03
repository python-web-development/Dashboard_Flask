from flask import Flask, render_template_string
import pyodbc
import mysql.connector
import jsonify
app = Flask(__name__)

# Replace the following values with your database information
host = 'sql3.freesqldatabase.com'  # This is an example host, use the host provided by FreeSQLDatabase
database = 'sql3696217'             # Your database name
user = 'sql3696217'                 # Your database username
password = 'VGz6aYtwca'           # Your database password

# try:
conn = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password)
#     if conn.is_connected():
#         print('Connected to the database')
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM Categories')
#         for row in cursor.fetchall():
#             print(row)
# except mysql.connector.Error as e:
#     print(f'Error: {e}')
# finally:
#     # if conn.is_connected():
#     #     conn.close()
#     #     print('Connection closed')

# Root Node
@app.route('/')
def index():
#     return render_template_string('''
#     <h1>Sales Data - API Dashboard</h1>
#     <a href="/Categories"><button>Categories</button></a>
#     <a href="/Customers"><button>Customers</button></a>
#     <a href="/Employees"><button>Employees</button></a>
#     <a href="/Orders"><button>Orders</button></a>  
#     <a href="/Order_details"><button>Order_details</button></a>
#     <a href="/Products"><button>Products</button></a>
#     <a href="/Product_vendors"><button>Product_vendors</button></a>
#     <a href="/Vendors"><button>Vendors</button></a>
#     <a href="/ztblMonths"><button>ztblMonths</button></a>    
#     <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
#     <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
#     <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>                                                           
# ''')
    return "Hello"


@app.route('/Categories')
def Categories():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Categories")
    data = cursor.fetchall()
    table_html = '<table border="1"><tr><th>ID</th><th>Name</th><th>Value</th></tr>'
    # for item in data:
    #     table_html += f'<tr><td>{item["CategoryID"]}</td><td>{item["CategoryDescription"]}</td></tr>'
    # table_html += '</table>'
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>Categories</h1>                          
    # <p>{data}</p>
    # ''')
    return data


# Customers API
@app.route('/Customers')
def Customers():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customers")
    data = cursor.fetchall()
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>Customers</h1>                          
    # <p>{data}</p>
    # ''')
    return data


# Employees API
@app.route('/Employees')
def Employees():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employees")
    data = cursor.fetchall()
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>Employees</h1>                          
    # <p>{data}</p>
    # ''')
    return data
 
# Orders API
@app.route('/Orders')
def Orders():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Orders")
    data = cursor.fetchall()
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>Orders</h1>                          
    # <p>{data}</p>
    # ''')
    return data

# Order_details API
@app.route('/Order_details')
def Order_details():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Order_Details")
    data = cursor.fetchall()
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>Orders_details</h1>                          
    # <p>{data}</p>
    # ''')
    return data

# Products API
@app.route('/Products')
def Products():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    data = cursor.fetchall()
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>Products</h1>                          
    # <p>{data}</p>
    # ''')
    return data

# Product_vendors API
@app.route('/Product_vendors')
def Product_Vendors():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product_Vendors")
    data = cursor.fetchall()
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_Vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>Product_vendors</h1>                          
    # <p>{data}</p>
    # ''')
    return data

# Vendors API
@app.route('/Vendors')
def Vendors():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Vendors")
    data = cursor.fetchall()
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>Vendors</h1>                          
    # <p>{data}</p>
    # ''')
    return data

# ztblMonths API
@app.route('/ztblMonths')
def ztblMonths():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ztblMonths")
    data = cursor.fetchall()
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>Months</h1>                          
    # <p>{data}</p>
    # ''')
    return data

# ztblPriceRanges API
@app.route('/ztblPriceRanges')
def ztblPriceRanges():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ztblPriceRanges")
    data = cursor.fetchall()
    # return render_template_string(f'''
    # <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>PriceRanges</h1>                          
    # <p>{data}</p>
    # ''')
    return data
# ztblPurchaseCoupons API
@app.route('/ztblPurchaseCoupons')
def ztblPurchaseCoupons():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ztblPurchaseCoupons")
    data = cursor.fetchall()
    # return render_template_string(f'''
    #   <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>PurcahseCoupons</h1>                          
    # <p>{data}</p>
    # ''')
    return data
# ztblSeqNumbers API
@app.route('/ztblSeqNumbers')
def ztblSeqNumbers():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ztblSeqNumbers")
    data = cursor.fetchall()
    # return render_template_string(f'''
    #   <h1>Sales Data - API Dashboard</h1>                                
    # <a href="/Categories"><button>Categories</button></a>
    # <a href="/Customers"><button>Customers</button></a>
    # <a href="/Employees"><button>Employees</button></a>
    # <a href="/Orders"><button>Orders</button></a>  
    # <a href="/Order_details"><button>Order_details</button></a>
    # <a href="/Products"><button>Products</button></a>
    # <a href="/Product_vendors"><button>Product_vendors</button></a>
    # <a href="/Vendors"><button>Vendors</button></a>
    # <a href="/ztblMonths"><button>ztblMonths</button></a>    
    # <a href="/ztblPriceRanges"><button>ztblPriceRanges</button></a>
    # <a href="/ztblPurchaseCoupons"><button>ztblPurchaseCoupons</button></a> 
    # <a href="/ztblSeqNumbers"><button>ztblSeqNumbers</button></a>
    # <h1>SeqNumbers</h1>                          
    # <p>{data}</p>
    # ''')
    return data
if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=5000)
    app.run(debug=True)

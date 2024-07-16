from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return render_template('homepage.html')

#ask.com

# @app.route('/gifs', methods=["POST"]) #@ = decorator
# def gifs():
#     myGifs = [
#         "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWd6OG9mYWZmZGhmdWVjdDdpZ2ZzNDZ0aWxsMjNpOXR3M2V5Z21qcSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l4KibK3JwaVo0CjDO/200.webp",
#         "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3RsYzFhbHF0c3EwMDd2ZjIwYmRibndxdzk3N29idmwyemNyYTFmaSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jxETRYAi2KReel7pqy/giphy.webp",
#         "https://media0.giphy.com/media/krM6ANSNvFg52/giphy.webp?cid=790b7611otlc1alqtsq007vf20bdbnwqw977obvl2zcra1fi&ep=v1_gifs_search&rid=giphy.webp&ct=g",
#         "https://media4.giphy.com/media/CCuvWcg0rBmh2/giphy.webp?cid=790b7611e7mwn31b86vzzcp4zs60cqhjhn8no53t6okgo9jf&ep=v1_gifs_search&rid=giphy.webp&ct=g",
#         "https://media2.giphy.com/media/12m4TK1i8yopOw/200.webp?cid=790b7611e7mwn31b86vzzcp4zs60cqhjhn8no53t6okgo9jf&ep=v1_gifs_search&rid=200.webp&ct=g"    
#     ]
#     randomGif = random.choice(myGifs)
#     return render_template("gifs.html", randomGif=randomGif, randomBool = True, myGifs=myGifs)

@app.route('/input', methods=['GET','POST'])
def input():
    myGifs = [
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWd6OG9mYWZmZGhmdWVjdDdpZ2ZzNDZ0aWxsMjNpOXR3M2V5Z21qcSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l4KibK3JwaVo0CjDO/200.webp",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3RsYzFhbHF0c3EwMDd2ZjIwYmRibndxdzk3N29idmwyemNyYTFmaSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jxETRYAi2KReel7pqy/giphy.webp",
    "https://media0.giphy.com/media/krM6ANSNvFg52/giphy.webp?cid=790b7611otlc1alqtsq007vf20bdbnwqw977obvl2zcra1fi&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media4.giphy.com/media/CCuvWcg0rBmh2/giphy.webp?cid=790b7611e7mwn31b86vzzcp4zs60cqhjhn8no53t6okgo9jf&ep=v1_gifs_search&rid=giphy.webp&ct=g",
    "https://media2.giphy.com/media/12m4TK1i8yopOw/200.webp?cid=790b7611e7mwn31b86vzzcp4zs60cqhjhn8no53t6okgo9jf&ep=v1_gifs_search&rid=200.webp&ct=g"    
    ]

    imgData = {"peng": "https://www.cabq.gov/artsculture/biopark/news/10-cool-facts-about-penguins/@@images/1a36b305-412d-405e-a38b-0947ce6709ba.jpeg"}
 
    if request.method == "POST":
        query = request.form['query']
        if query not in imgData:
            return "No data found for " + query
        return render_template("search.html", myGifs=myGifs, imgData=imgData[query]) #implied else
        
    return render_template('input.html', url=url_for('input'), var="practice with Flask") #implied else

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


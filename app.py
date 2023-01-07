from flask import Flask, render_template, request
import config
import aicontent

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/product-description', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        submission = request.form['productDescription']
        query = "Generate a detailed product description for: {}".format(submission)
        openAIAnswer = aicontent.open_ai_query(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
        
    return render_template('product-description.html', **locals())



@app.route('/job-description', methods=["GET", "POST"])
def jobDescription():

    if request.method == 'POST':
        submission = request.form['jobDescription']
        query = "Generate a job description about: {}".format(submission)
        openAIAnswer = aicontent.open_ai_query(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
       
    return render_template('job-description.html', **locals())



@app.route('/tweet-ideas', methods=["GET", "POST"])
def tweetIdeas():

    if request.method == 'POST':
        submission = request.form['tweetIdeas']
        query = "Generate a tweet about: {}".format(submission)
        openAIAnswer = aicontent.open_ai_query(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('tweets.html', **locals())



@app.route('/email-template', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':
        submission = request.form['coldEmails']
        query = "Write a good professional email about: {}".format(submission)
        openAIAnswer = aicontent.open_ai_query(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('email-template.html', **locals())



@app.route('/social-media', methods=["GET", "POST"])
def socialMedia():

    if request.method == 'POST':
        submission = request.form['socialMedia']
        query = "Write great advertising text about {}".format(submission)
        openAIAnswer = aicontent.open_ai_query(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)
        
    return render_template('social-media.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"])
def videoIdeas():

    if request.method == 'POST':
        submission = request.form['videoIdeas']
        query = "Write an idea for a video about {}".format(submission)
        openAIAnswer = aicontent.open_ai_query(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('video-ideas.html', **locals())




if __name__ == '__main__':
    app.run(port='8888', debug=True)
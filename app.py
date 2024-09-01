# from sorce.chain import Chain
# from langchain_community.document_loaders import WebBaseLoader
# import flask
# from sorce.utils import clean_text
# from sorce.portfolio import Portfolio
# chain = Chain()
# portfolio = Portfolio()


# loader = WebBaseLoader("https://www.asthait.com/career/machine-learning-engineer/")
# page_data = loader.load().pop().page_content
# page_data = clean_text(page_data)
# jobs = chain.extract_jobs(page_data)
# # print(jobs)
# portfolio.load_portfolio
# for job in jobs:
#     skills = job.get('skills', [])
#     links = portfolio.query_links(skills)
#     email = chain.write_mail(job, links)
#     print(email)

from flask import Flask, request, jsonify
from sorce.chain import Chain
from langchain_community.document_loaders import WebBaseLoader
from sorce.utils import clean_text
from sorce.portfolio import Portfolio

app = Flask(__name__)

# Initialize chain and portfolio objects
chain = Chain()
portfolio = Portfolio()

@app.route('/process', methods=['POST'])
def process_data():
    # Get the URL from the POST request
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        # Load and process the page data
        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content
        page_data = clean_text(page_data)

        # Extract jobs
        jobs = chain.extract_jobs(page_data)

        # Prepare responses
        responses = []
        for job in jobs:
            skills = job.get('skills', [])
            links = portfolio.query_links(skills)
            email = chain.write_mail(job, links)
            responses.append(email)

        return jsonify({'emails': responses})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

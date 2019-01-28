FROM python
WORKDIR /quizapp
ADD . /quizapp
RUN pip install -r requirements.txt
CMD "behave"

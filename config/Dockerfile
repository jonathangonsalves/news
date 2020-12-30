FROM python:3.8

RUN groupadd --gid 1000 nubank &&\
    useradd --uid 1000 --gid nubank --shell /bin/nubank nubank &&\
    install -d -m 0755 -o 1000 /home/nubank && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get -y update && \
    apt-get install -yq \
        google-chrome-stable \
        unzip \
        xvfb && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip && \
    rm -rf /var/lib/apt/lists/*

# Switch user
USER nubank

# Default environment variables
ENV DISPLAY=:99

ENV PATH=${PATH}:/home/nubank/.local/bin

WORKDIR /home/nubank

COPY ./requirements.txt /home/nubank/requirements.txt
COPY ./src /home/nubank/src

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    mkdir -p /home/nubank/session /home/nubank/.aws

ENTRYPOINT ["python", "src/cli.py"]





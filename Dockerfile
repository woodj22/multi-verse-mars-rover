FROM python:3.9-slim

# Apparently this is good practice? *shrugg*
RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
USER app_user
COPY . .
# From here we can run the command and run the tests. Its a bit of a dirty way of doing it rather than composing docker properly.
CMD ["bash"]

# jwcrypto-jwe

Encrypt 🔑 some payload using [_JSON Web Encryption_](https://tools.ietf.org/html/rfc7516) and [`jwcrypto`](https://jwcrypto.readthedocs.io/en/latest/) library.

## Install

Requires [python](https://www.python.org) and [pipenv](https://pipenv.readthedocs.io/en/latest/)
Install **Python** 🐍:

```bash
$ brew install python
```

Install `pipenv`:

```bash
$ brew install pipenv
```

Install dependencies and _virtualenv_:

```bash
$ pipenv install
```

## Usage

Run the project using `pipenv`, it should print in the _console_ 🖥 the encrypted value:

```json
$ pipenv run python encrypt.py
JSON:
 {"ciphertext":"yrlhC56OFE6Z2gKIYJL5IF_sNOI","encrypted_key":"SXfjWyBKBP462igB-1yV6rxvS9gjm3zxY0XZd5hiHC8-ivRh6o6zshlspYXuHQQEhn1ggCnU0cLQzJDWq-y957uhJdMLvrJkciU7R8VhfwGiT6P5yNO0iGyA9uYjJupevXM2BwBqiy_X8VLOo-prIAn09KmfQmxK4r-jqgZWJUr_DjHcC7_pWfoC6X-HXqsYiNXYhx1449_qwohAjtDbfCQj8nVB9XN41KgcEa3frXAc-OUYwH3C9jpnUZYMc8b17efl7IwDvkWYtA7EtIdDbqGh-Wm0gUx3rzx6f5RZ2CXgIe0bNa-v-TbMk5Z1mNMO6obLayq0BGu6Ii0d8jsF8w","iv":"bugla-7XbF4CwQiP","protected":"eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00iLCJraWQiOiI1b2ZXUDA5Q2hXNHFvcDZQNDNYYkY3X0YyUG5FSjdfaEJoWEFhcndRZm5RIn0","tag":"XQZ5hmKjpu0nnZH6w-1kIA"}

Compact:
 eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00iLCJraWQiOiI1b2ZXUDA5Q2hXNHFvcDZQNDNYYkY3X0YyUG5FSjdfaEJoWEFhcndRZm5RIn0.SXfjWyBKBP462igB-1yV6rxvS9gjm3zxY0XZd5hiHC8-ivRh6o6zshlspYXuHQQEhn1ggCnU0cLQzJDWq-y957uhJdMLvrJkciU7R8VhfwGiT6P5yNO0iGyA9uYjJupevXM2BwBqiy_X8VLOo-prIAn09KmfQmxK4r-jqgZWJUr_DjHcC7_pWfoC6X-HXqsYiNXYhx1449_qwohAjtDbfCQj8nVB9XN41KgcEa3frXAc-OUYwH3C9jpnUZYMc8b17efl7IwDvkWYtA7EtIdDbqGh-Wm0gUx3rzx6f5RZ2CXgIe0bNa-v-TbMk5Z1mNMO6obLayq0BGu6Ii0d8jsF8w.bugla-7XbF4CwQiP.yrlhC56OFE6Z2gKIYJL5IF_sNOI.XQZ5hmKjpu0nnZH6w-1kIA
```

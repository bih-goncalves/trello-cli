<h3 align="center">Trello-CLI</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">This is the python CLI made for Trello board API.
    <br>
</p>

## 📝 Content

- [About](#about)
- [Getting started](#getting_started)
- [Usage](#usage)
- [Built using](#built_using)
- [Next steps](#next)
- [Author](#authors)
- [Acknowledgement](#acknowledgement)
---

## 🏁 Getting started <a name = "getting_started"></a>

You can use the CLI on local machine or with docker container.

### Prerequisites

```
Python 3
Credentials for trelloboard
Board ID
Knowledge about board's labels
```

### Credentials

You can get your API key by logging into Trello and visiting https://trello.com/app-key .

On the same page you have a link to generate a Token.

Save both with you.


## 🎈 Usage <a name="usage"></a>

We recomend to save the scripts somewhere safe and create an alias to it:
```
alias trello-cli='python3 __init__.py'
```

To make the alias persistent you need to declare it in the ~/.bash_profile or ~/.bashrc file.

Before start using the CLI, be sure that you are using your credentials as part of your environment:

```
export KEY=YOUR_KEY_FROM_TRELLO_API
export TOKEN=YOUR_TOKEN_FROM_TRELLO_API
```

### Available commands

```
-- Lists
trello-cli lists ls BOARD_ID

-- Cards
trello-cli cards create BOARD_ID COLUM_NUMBER CARD_NAME DESCRIPTION
trello-cli cards create BOARD_ID COLUM_NUMBER CARD_NAME DESCRIPTION -l LABEL_NAME -c COMMENT_TEXT

trello-cli cards comment CARD_ID COMMENT_TEXT
trello-cli cards categorize CARD_ID LABEL_ID

-- Labels
trello-cli labels ls BOARD_ID

```
PS:
```
- Any of other commands with result in an excuse.

- I decided to use COLUM_NUMBER when handling with cards because it's faster.

- BOARD_ID is available on the URL. In the future you will have a list of boards to check.

- For cards, -l and -c are optional
```

## ⛏️ Built using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming language
- [Trello API](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/) - Remote API

## 🧐  Next steps <a name = "next"></a>

For next steps, there are a lot of features that need some attention and can make the CLI awesome. Like boards options, deleting entities, removing changes, etc. 

We can start from the ones listed in the main script, and after go for other possibilities from the Trello API.

## ✍️ Author <a name = "authors"></a>

- [@bih-goncalves](https://github.com/bih-goncalves)

## 🎉 Acknowledgement <a name = "acknowledgement"></a>

- This project is for the 'Public Cloud Eng Take Home Test' from [@canonical](https://canonical.com/)

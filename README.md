# Actuarial Anki Deck(s)

Built upon the wonderful work by [kerrickstaley/genanki][1].

Intended Audience: Anybody studying for Actuarial Exams

Required Background:

* Familiarity with Anki
* Basic navigation of Git/GitHub

## Methodology

The idea of this repo is that users can create, upload, and share [Anki decks][2]
as plaintext files (for version control) that would be bundled as an Anki
notes deck (.apkg file) and pushed to some centralized location.

### Layout

The decks are currently planned to be laid out as follows:

```bash
├───CAS
│   └───{Exam}
│       └───SourceNotes
│               Anki Deck Name.csv
│               Other Anki Deck Name.csv
│               Another Anki Deck Name.csv
│
└───SOA
    └───{Exam}
        └───SourceNotes
                Anki Deck Name.csv
                Other Anki Deck Name.csv
                Another Anki Deck Name.csv
```

Under either the SOA or the CAS folder, a subfolder should exist
for each exam that has any decks. Within that exam subfolder,
decks should be saved as CSV files under a SourceNotes directory.

## Usage

### Creating a new deck

Currently, CSV files are the only way to upload a deck
to this repository (the end goal will likely be JSON).

The first column in the csv file is assumed to be the
front of the Anki card. The second column is assumed
to be the back.

Formatting is defined in the css files under `./assets/css`.
To create styling for a card, the desired stylesheet can
be read into the `css` attribute of `genanki.Model()`

After creating your desired deck and ensuring it is properly formatted,
[make a PR][3] and await its approval.

### Using a deck from this repo

Using Locally:

Currently the best way to use one of these decks is to
clone this repository and do a little bit of work in the terminal.

#### 1. Install requirements

```bash
py -m venv .venv && . .venv/Scripts/activate
pip install -r requirements.txt

```

#### 2. Generate the deck(s)

```bash
py ./generate_decks.py
```

#### 3. Output

Running generate_decks.py will create Anki .apkg files in
a `build/` directory with the same name as the CSV files
used to create them.

## Contributing

* [Feature request][4]
* [Bug report][4]

[1]: https://github.com/kerrickstaley/genanki "genanki: A Library for Generating Anki Decks"
[2]: https://apps.ankiweb.net/
[3]: https://github.com/lathaniel/anki-actuary/compare "New pull request"
[4]: https://github.com/lathaniel/anki-actuary/issues/new/choose "New issue"

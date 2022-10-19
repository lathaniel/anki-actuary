import ntpath
import genanki
import csv
from pathlib import Path
from glob import glob, iglob
import os

# General formula model

questionStyle = 'font-size: 50px; font-weight: bold;'

fxModel = genanki.Model(
    model_id=45827598,
    name='Formula Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': "<div style='{}'>{{{{Question}}}}</div>".format(questionStyle),
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
    css=open('./assets/css/base.css', 'r').read()
)

def main():
    # Do SOA Files
    directory = 'SOA'
    for subdir, dirs, _ in os.walk(directory):
        for dir in dirs:
            # Loop through directories and generate decks from .csv files
            for notesFile in iglob(os.path.join(subdir, dir, '*.csv')):
                deckName = ntpath.basename(notesFile).split('.')[0]

                # Read csv into an array
                with open(notesFile) as f:
                    noteData = list(csv.reader(f))

                # Create a deck
                deck = genanki.Deck(
                    deck_id=39184935189,
                    name=deckName
                )

                # For each note in the file, add it to the deck
                for note in noteData:
                    deck.add_note(genanki.Note(
                        model=fxModel,
                        fields=note
                    ))

                # once done, package the deck
                Path('build/').mkdir(parents=True, exist_ok=True)
                genanki.Package(deck).write_to_file('build/erm.apkg')


if __name__=='__main__':
    main()
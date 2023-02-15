from pathlib import Path
from glob import iglob
import os

import genanki
import yaml

questionStyle = 'font-size: 50px; font-weight: bold;'


def divWrap(child: any, style: str = ''):
    return f"<div style='{style}'>{child}</div>"


# General formula model
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
            'qfmt': divWrap(child='{{Question}}', style=questionStyle),
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
    css=open('./assets/css/formulaCard.css', 'r').read()
)


def main():
    # Do SOA Files
    directory = 'SOA'
    for subdir, dirs, _ in os.walk(directory):
        for dir in dirs:
            # Loop through directories and generate decks from .yaml files
            for notesFile in iglob(os.path.join(subdir, dir, '*.yaml')):
                # Load YAML data
                with open(notesFile) as f:
                    deckData = yaml.safe_load(f)

                deckName = deckData['Name']

                # Create a deck
                deck = genanki.Deck(
                    deck_id=39184935189,
                    name=deckName
                )

                # For each note in the file, add it to the deck
                for note in deckData['Cards']:
                    deck.add_note(genanki.Note(
                        model=fxModel,
                        fields=[note['Front'], note['Back']]
                    ))

                # once done, package the deck
                Path('build/').mkdir(parents=True, exist_ok=True)
                genanki.Package(deck).write_to_file(f'build/{deckName}.apkg')


if __name__ == '__main__':
    main()

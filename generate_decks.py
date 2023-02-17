from pathlib import Path
from glob import iglob
import os

import genanki
import yaml


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
                    useCss: bool = 'css' in deckData['Model'].keys()
                    deck.add_note(genanki.Note(
                        model=genanki.Model(
                            model_id=deckData['Model']['model_id'],
                            name=deckData['Model']['name'],
                            fields=[{'name': x} for x in deckData['Model']['fields']],
                            templates=deckData['Model']['templates'],
                            css=open(deckData['Model']['css'], 'r').read() if useCss else None
                        ),
                        fields=[note[x] if x in note.keys() else '' for x in deckData['Model']['fields']]
                    ))

                # once done, package the deck
                Path('build/').mkdir(parents=True, exist_ok=True)
                genanki.Package(deck).write_to_file(f'build/{deckName}.apkg')


if __name__ == '__main__':
    main()

import typer
import pyttsx3
import sqlite3

app = typer.Typer()
text_speech = pyttsx3.init()


@app.command()
def disease(name: str):
    conn = sqlite3.connect('disease.db')
    c = conn.cursor()
    c.execute("SELECT * from diseases WHERE disease = (?)", [name])
    items = c.fetchall()

    for item in items:
        for row in item:
            print(f'\n{row}')
        print()
    conn.commit()
    conn.close()

    for item in items:
        for strings in item:
            strings = strings.replace(r'\n', '').replace('_', ' ')
            text_speech.say(strings)
    text_speech.runAndWait()

    print(
        f"For information about {name.replace('_', ' ')}, click this link: https://en.wikipedia.org/wiki/{name.lower()}")

    print(
        f"To contact a doctor about {name.replace('_', ' ')}, click this link: https://www.google.com/search?q={name.lower()}+doctors+near+me")

    text_speech.say(f"For more information about {name.replace('_', ' ')}, click the links.")
    text_speech.runAndWait()


if __name__ == '__main__':
    app()


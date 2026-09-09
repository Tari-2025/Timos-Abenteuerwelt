# Nilos Lernwörter (Deutsch)

Prototyp für den Deutsch-Teil der Abenteuerwelt. Noch eigenständig, damit das
laufende Rechenspiel unberührt bleibt. Wenn sich die Übungsformen bewähren,
wandert das Ganze als Fach „Deutsch" in die Fachauswahl.

`lernwoerter.html` – die spielbare Datei, wie immer per Doppelklick zu öffnen.

## Inhalt

- 12 Lernwörtertrainings des zweiten Schuljahres, je 13 Wörter
- Häufigkeitswörter des Grundwortschatzes NRW, in vier Paketen

## Übungen

| Übung | Was passiert |
|---|---|
| **Blitzlesen** | Wort erscheint für vier Sekunden, dann aus dem Kopf tippen |
| **Lückenwort** | Die Stolperstelle ist verdeckt, Buchstaben werden angetippt |
| **Welches stimmt?** | Richtige Schreibweise unter falschen erkennen |
| **der/die/das** | Artikel zuordnen (nur bei Nomen) |
| **Gemischt** | Pro Wort eine passende Übung, zufällig gewählt |

Passt eine Übung nicht zu einem Wort, wird sie dort übersprungen: Wörter unter
vier Buchstaben bekommen kein Lückenwort, Wörter ohne glaubwürdige
Fehlschreibung keine Auswahl, Wörter ohne Artikel keine Artikelübung.

## Neue Wortlisten einpflegen

Die Werkzeuge in `werkzeuge/` erzeugen aus einer Wortliste alles Weitere –
die Lehrkraft muss nur die Wörter liefern.

1. `extrahiere.py` liest die Wörter aus dem PDF der Schule (`woerter.json`).
2. `erzeuge.py` bestimmt je Wort die orthografische Stolperstelle und leitet
   daraus die Lücke und die Fehlschreibungen ab (`pakete.json`).

`erzeuge.py` kennt die typischen Fehler der Grundschule: ß statt ss, fehlende
oder falsch gesetzte Doppelkonsonanten, ie/i, stummes h, ck, tz, Auslaut d/t
und g/k, -ig/-ich, äu/eu, v/f und vereinfachte Umlaute. Erzeugte Varianten,
die zufällig ein echtes deutsches Wort ergeben würden (etwa `in`/`ihn` oder
`viel`/`fiel`), werden verworfen – sonst wäre die Aufgabe irreführend.

Gibt es zu einem Wort nur eine glaubwürdige Fehlschreibung, zeigt die Übung
bewusst nur zwei Möglichkeiten statt eine unsinnige dritte zu erfinden.

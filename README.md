# Abenteuerwelt – Rechnen mit Nilo

Ein Mathe-Lernspiel für die Grundschule (etwa 2. bis 4. Klasse). Die Kinder lösen
Rechenaufgaben, sammeln dabei Material und bauen sich davon eine eigene
Achterbahn, auf der die Lore am Ende fährt. Ihr Maskottchen **Nilo** fährt immer mit.

Das Spiel besteht aus **einer einzigen HTML-Datei**. Es braucht kein Internet,
keine Installation und kein Benutzerkonto.

---

## Schnellstart

1. Die Datei `index.html` herunterladen.
2. Doppelklick – sie öffnet sich im Browser.
3. Namen auswählen, Schwierigkeit wählen, losfahren.

Das war's. Es funktioniert auf PC, Mac, Tablet und Handy, auch ohne Internetverbindung.

---

## Datenschutz

Für den Einsatz in der Schule wichtig:

- Es werden **keine Daten übertragen**. Das Spiel stellt keine einzige
  Netzwerkverbindung her und lädt nichts nach.
- Es gibt **kein Tracking, keine Werbung, keine Analyse-Werkzeuge**.
- Spielstände werden ausschließlich **lokal im Browser** des jeweiligen Geräts
  gespeichert (`localStorage`) und verlassen es nicht.
- Gespeichert werden nur die Vornamen aus der Klassenliste sowie Sterne, Level
  und die gebaute Strecke.

Wer alles zurücksetzen will: Lehrerbereich → *Fortschritt* → *Alle Spielstände
auf diesem Gerät löschen*.

---

## Für Lehrkräfte und Eltern

Auf dem Startbildschirm unten steht **„Für Lehrkräfte und Eltern"**.
Der voreingestellte Code ist **1234** – er lässt sich dort ändern.

Im Lehrerbereich lassen sich einstellen:

| Bereich | Was geht |
|---|---|
| **Kinder** | Klassenname und Namensliste pflegen (hinzufügen, umbenennen, entfernen). Beim Umbenennen wandert der Spielstand mit. |
| **Maskottchen** | Name frei wählbar, dazu sechs Tierarten (Nilpferd, Elefant, Bär, Fuchs, Eule, Drache) und sechs Farben. |
| **Fortschritt** | Übersicht, wie weit jedes Kind auf **diesem Gerät** ist; einzeln oder komplett zurücksetzbar. |
| **Weitergeben** | Klassencode zum Übertragen der Einstellungen auf andere Geräte. |

### Auf mehrere Geräte verteilen

Die Namensliste muss nicht auf jedem Tablet neu getippt werden:

1. Auf **einem** Gerät die Klassenliste und das Maskottchen einrichten.
2. Lehrerbereich → *Weitergeben* → den **Klassencode** kopieren.
3. Auf den anderen Geräten `index.html` öffnen, in den Lehrerbereich gehen,
   den Code unten einfügen und auf *Übernehmen* tippen.

Der Klassencode enthält nur Namensliste, Klassenname und Maskottchen –
**keine Spielstände**. Jedes Kind behält also seinen Fortschritt auf dem Gerät,
an dem es spielt.

Für zu Hause reicht es, den Kindern die Datei mitzugeben. Wer möchte, schickt
den Klassencode dazu, damit dort dieselben Namen und dasselbe Maskottchen
erscheinen.

---

## Schwierigkeitsstufen

Die Kinder wählen ihre Stufe beim Start selbst und können sie jederzeit im Spiel
oben rechts wechseln – ohne ihren Fortschritt zu verlieren.

| Stufe | Was sich ändert |
|---|---|
| **Leicht** | Kleinere Zahlenräume. Bei kleinen Plus- und Minusaufgaben erscheinen **Punktebilder** als Anschauungshilfe. Beim Einmaleins gibt es nur die Reihen bis 5 und einen Hinweis, wie man die Malaufgabe als Plusaufgabe denken kann. |
| **Mittel** | Der normale Weg. |
| **Knifflig** | Größere Zahlen, mehr Lückenaufgaben, schwierigere Textaufgaben. |

Über die **Karte** (Symbol links) kann jedes Kind außerdem direkt in jede Welt
springen. Niemand bleibt also an einer schweren Welt hängen.

## Inhalte

- Plus und Minus im Zahlenraum bis 10, 20, 30, 40, 50 und 100
- Zehnerzahlen bis 100
- Lückenaufgaben (`7 + ? = 12`)
- Textaufgaben – darin tauchen die Vornamen aus der Klassenliste auf
- Das kleine Einmaleins, Reihe für Reihe (Weltraum-Level)
- Nach je drei Welten ein freundlicher Gegenspieler, am Ende der Wolkendrache

---

## Bearbeiten

Alles steckt in `index.html`. Wer Texte ändern möchte, findet die wichtigsten
Stellen im `<script>`-Teil:

- `WORD_TEMPLATES` – die Textaufgaben
- `WORLDS` – die Welten mit Namen und Aufgabentyp
- `PACKS` – die Zahlenräume je Stufe
- `DEFAULT_KIDS` – die voreingestellte Namensliste
- `BOSS_META` – die Gegenspieler

---

## Lizenz

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de) –
siehe [LICENSE](LICENSE).

Kurz gesagt: weitergeben, verändern und im Unterricht einsetzen ist ausdrücklich
erwünscht, solange es nicht kommerziell geschieht und die Herkunft genannt wird.

Alle Grafiken sind eigene CSS-Zeichnungen. Das Spiel verwendet keine fremden
Marken, Figuren oder Grafiken.

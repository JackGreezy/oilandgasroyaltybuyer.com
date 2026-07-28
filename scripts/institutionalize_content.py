#!/usr/bin/env python3
"""Enforce business voice across every authored content file."""

from __future__ import annotations

import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
FIRST_PERSON = re.compile(r"\b(i|i['’]m|i['’]ve|i['’]d|i['’]ll|me|my|mine|myself)\b", re.I)

NARRATIVE_REPLACEMENTS = (
    (r"\bI am not a CPA\b", "Oil & Gas Royalty Buyer is not a CPA firm"),
    (r"\bWhat I can do is explain\b", "This guide explains"),
    (r"\bWhat I can give you is\b", "This guide provides"),
    (r"\bWhat I can do is lay out\b", "This guide lays out"),
    (r"\bI get asked\b", "The royalty desk is asked"),
    (r"\bI understand why\b", "the reason is understandable"),
    (r"\bI don['’]t think there['’]s\b", "there is not"),
    (r"\bI spent years on the operating side, watching\b",
     "Oil & Gas Royalty Buyer brings operating-side experience from watching"),
    (r"\bthe way I['’]d walk it\b", "the way the royalty desk would walk it"),
    (r"\bEvery closing I['’]ve been part of\b", "Every closing the royalty desk has handled"),
    (r"\bI spent a chunk of my career on Anadarko Basin gas wells, and the thing that always struck me was how deep this basin runs\b",
     "Operating-side experience with Anadarko Basin gas wells makes the depth of this basin impossible to miss"),
    (r"\bbefore I was in the business\b", "for decades"),
    (r"\bWhere I['’]ve seen owners get confused is when\b", "Owners often get confused when"),
    (r"\bI['’]ve priced a lot of Bakken interests, and the first thing I do is\b",
     "After pricing many Bakken interests, the royalty desk first"),
    (r"\bThe first royalty statement I ever handled for an heir was for a woman whose father had passed two years earlier\b",
     "One early inherited-royalty file involved an owner whose father had passed two years earlier"),
    (r"\bI['’]ve talked to\b", "The royalty desk has worked with"),
    (r"\bI spent years on the operations side before I ever bought a mineral interest from someone, and the divorce files were always the slowest ones to close\b",
     "Oil & Gas Royalty Buyer brings operating-side experience to mineral transactions, and divorce files are often among the slowest to close"),
    (r"\bWhen I evaluate\b", "When the royalty desk evaluates"),
    (r"\bthe first thing I ask for is the same thing I['’]d ask any owner for\b",
     "the first request is the same evidence requested from any owner"),
    (r"\btells me more than any appraisal report will\b",
     "usually provides more usable evidence than a generic appraisal report"),
    (r"\bI look at what neighboring wells are doing\b", "the review looks at neighboring well activity"),
    (r"\bI['’]ve dealt with\b", "The royalty desk has worked with"),
    (r"\bowners I talk to\b", "owners contacting the royalty desk"),
    (r"\bI['’]ve seen division orders\b", "The royalty desk has reviewed division orders"),
    (r"\bI can usually tell you\b", "the royalty desk can usually explain"),
    (r"\binterests I get asked about\b", "interests brought to the royalty desk"),
    (r"\bI['’]ve reviewed\b", "The royalty desk has reviewed"),
    (r"\bAsk me about\b", "Ask the royalty desk about"),
    (r"\bmy first question\b", "the first question"),
    (r"\bstate I work in\b", "state the royalty desk reviews"),
    (r"\bBefore I can give you a real number, I need to know\b",
     "Before the royalty desk can support a number, the file needs to identify"),
    (r"\bcalls I take\b", "inquiries the royalty desk receives"),
    (r"\banywhere else I work\b", "in other states the royalty desk reviews"),
    (r"\bI['’]ll tell you plainly\b", "The royalty desk explains plainly"),
    (r"\bbefore we talk numbers\b", "before discussing numbers"),
    (r"\bwhere I ask\b", "where the royalty desk asks"),
    (r"\bI never quote\b", "the royalty desk never quotes"),
    (r"\bI['’]ll say this plainly up front\b", "The royalty desk states this plainly up front"),
    (r"\bI spent years on the operating side watching CBM production curves, and\b",
     "Oil & Gas Royalty Buyer brings years of operating-side experience with CBM production curves, and"),
    (r"\bwho calls me\b", "who contacts the royalty desk"),
    (r"\bBefore I quote a Pennsylvania interest, I want to see\b",
     "Before the royalty desk quotes a Pennsylvania interest, the file needs"),
    (r"\bI['’]ve priced New Mexico interests\b", "The royalty desk has priced New Mexico interests"),
    (r"\bI don['’]t quote a New Mexico interest until I know\b",
     "The royalty desk does not quote a New Mexico interest until the file identifies"),
    (r"\bthe questions I ask are\b", "the review questions cover"),
    (r"\bstate I deal with\b", "state the royalty desk reviews"),
    (r"\bEvery Bakken owner I talk to eventually asks\b", "Bakken owners regularly ask"),
    (r"\btells me roughly where on that curve the well sits\b",
     "indicates roughly where the well sits on that curve"),
    (r"\bI read statements for a living\b", "The royalty desk reads royalty statements every day"),
    (r"\bThe first thing I ask an Oklahoma owner for\b",
     "The first thing the royalty desk requests from an Oklahoma owner"),
    (r"\bI['’]ve had owners assume\b", "Owners sometimes assume"),
    (r"\bI don['’]t price a Uinta Basin interest\b", "The royalty desk does not price a Uinta Basin interest"),
    (r"\bI['’]ve spent enough years looking at Montana division orders to know\b",
     "Years of reviewing Montana division orders show that"),
    (r"\bI look at the statement first, not the map\b", "The review starts with the statement, not the map"),
    (r"\bA Montana check tells me\b", "A Montana check reveals"),
    (r"\bI['’]ve bought flank interests where\b", "The royalty desk has evaluated flank interests where"),
    (r"\bBefore I quote anything, I want to see\b",
     "Before the royalty desk quotes anything, the file needs"),
    (r"\banything I['’]d tell you over the phone\b",
     "anything the royalty desk could explain over the phone"),
    (r"\bchanges how I think about\b", "changes how the royalty desk evaluates"),
    (r"\bI['’]d rather tell you that up front\b", "the royalty desk states that up front"),
    (r"\bI['’]d rather set that expectation early\b", "the royalty desk sets that expectation early"),
    (r"\bWorld War I\b", "the First World War"),
    (r"\bI ask which county and which window before I ask anything else\b",
     "The royalty desk asks about the county and production window first"),
    (r"\bI spent most of my career on the operating side, and working interest is\b",
     "Operating-side experience makes clear that working interest is"),
    (r"\bOf everything I['’]ve bought over the years\b",
     "Among the interests the royalty desk has evaluated"),
    (r"\bI spent years on the operating side of oil and gas\b",
     "Oil & Gas Royalty Buyer brings years of operating-side oil and gas experience"),
)


def question_to_second_person(text: str) -> str:
    replacements = (
        (r"\bI['’]m\b", "you are"),
        (r"\bI['’]ve\b", "you have"),
        (r"\bI['’]d\b", "you would"),
        (r"\bI['’]ll\b", "you will"),
        (r"\bI\b", "you"),
        (r"\bmyself\b", "yourself"),
        (r"\bmine\b", "yours"),
        (r"\bmy\b", "your"),
        (r"\bme\b", "you"),
    )
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.I)
    cleanups = (
        (r"^You inherited this interest and it['’]s still in a relative['’]s name - what do you need\?$",
         "What paperwork is needed when an inherited interest remains in a relative's name?"),
        (r"^You leased your TMS minerals expecting the play to boom — what happened\?$",
         "What happened after a TMS lease was signed but the play did not boom?"),
        (r"^You still get a small check from an old vertical well from decades ago — is that normal\?$",
         "Is it normal to still receive a small check from an old vertical well?"),
        (r"^Your family['’]s mineral rights were separated from the surface a long time ago — can you still sell the gas rights\?$",
         "Can gas rights still be sold when the minerals were separated from the surface long ago?"),
        (r"^Your check dropped to almost nothing — did the well fail\?$",
         "Did the well fail if the royalty check dropped to almost nothing?"),
        (r"^You own a small fractional interest inherited three generations back — is it worth selling\?$",
         "Is a small fractional interest inherited three generations back worth selling?"),
        (r"^You inherited a small Black Warrior interest and don['’]t know much about it — is it worth anything\?$",
         "Is a small inherited Black Warrior interest worth evaluating?"),
        (r"^You own minerals in more than one Texas play\. Do you buy the whole package\?$",
         "Can minerals in more than one Texas play be evaluated as one package?"),
        (r"^You have Nebraska mineral rights but have never received a check\. Are they worth anything\?$",
         "Are Nebraska mineral rights worth evaluating if they have never produced a check?"),
        (r"^You only own a small fractional interest\. Is it worth selling\?$",
         "Is a small fractional interest worth selling?"),
        (r"^You was force-pooled by the Industrial Commission\. Do you still own your minerals\?$",
         "Do force-pooled owners still retain their minerals?"),
        (r"^You inherited a Michigan interest but never see a statement\. What now\?$",
         "What should an owner do after inheriting a Michigan interest without receiving statements?"),
        (r"^You don['’]t have a deed for your West Virginia mineral rights, just family knowledge\. Can you still help\?$",
         "Can the royalty desk help when an owner has family knowledge but no West Virginia deed?"),
        (r"^You inherited a small fractional interest and don['’]t even know the legal description\. Can you still help\?$",
         "Can the royalty desk help with an inherited fractional interest when the legal description is unknown?"),
        (r"^You have a TMS lease but no producing well\. Can you still sell\?$",
         "Can TMS minerals be sold when leased but not producing?"),
        (r"^You only own a tiny fraction of a unit\. Can you still sell\?$",
         "Can an owner sell a tiny fractional share of a unit?"),
        (r"^You are not sure you own anything - can you help you find out\?$",
         "Not sure whether you own anything—can the royalty desk help confirm it?"),
        (r"^Your family['’]s Tennessee mineral rights haven['’]t been touched in decades\. Can you still research them\?$",
         "Can old family-held Tennessee minerals still be researched?"),
    )
    for pattern, replacement in cleanups:
        text = re.sub(pattern, replacement, text, flags=re.I)
    return text[0].upper() + text[1:] if text else text


def institutionalize(text: str) -> str:
    if text.strip().endswith("?"):
        return question_to_second_person(text)

    for pattern, replacement in NARRATIVE_REPLACEMENTS:
        text = re.sub(pattern, replacement, text, flags=re.I)

    fallbacks = (
        (r"\bI['’]m\b", "the royalty desk is"),
        (r"\bI['’]ve\b", "the royalty desk has"),
        (r"\bI['’]d\b", "the royalty desk would"),
        (r"\bI['’]ll\b", "the royalty desk will"),
        (r"\bmyself\b", "the royalty desk"),
        (r"\bmine\b", "the owner's"),
        (r"\bmy\b", "the owner's"),
        (r"\bme\b", "the royalty desk"),
        (r"\bI\b", "the royalty desk"),
    )
    for pattern, replacement in fallbacks:
        text = re.sub(pattern, replacement, text, flags=re.I)

    grammar = (
        (r"\bthe royalty desk am\b", "the royalty desk is"),
        (r"\bthe royalty desk don['’]t\b", "the royalty desk does not"),
        (r"\bthe royalty desk have\b", "the royalty desk has"),
        (r"\bthe royalty desk do\b", "the royalty desk does"),
        (r"\bthe royalty desk ask\b", "the royalty desk asks"),
        (r"\bthe royalty desk need\b", "the royalty desk needs"),
        (r"\bthe royalty desk work\b", "the royalty desk works"),
        (r"\bthe royalty desk deal\b", "the royalty desk deals"),
        (r"\bthe royalty desk read\b", "the royalty desk reads"),
        (r"\bthe royalty desk look\b", "the royalty desk looks"),
    )
    for pattern, replacement in grammar:
        text = re.sub(pattern, replacement, text, flags=re.I)
    editorial_cleanups = (
        (r"\bsince for decades\b", "for decades"),
        (r"\bthe royalty desk first pull\b", "the royalty desk first pulls"),
        (r"\brather than take anyone['’]s word\b", "rather than taking anyone's word"),
        (r"\bMost of the interests The royalty desk is asked about\b",
         "Most interests brought to the royalty desk"),
        (r"\balmost in other states the royalty desk reviews\b",
         "than in most other states the royalty desk reviews"),
        (r"\bthan than in most other states\b", "than in most other states"),
        (r"\bThe royalty desk states this plainly up front, most\b",
         "The royalty desk states this plainly up front: most"),
        (r"\bstates that up front than waste\b", "states that up front rather than waste"),
        (r"\bstates that up front rather than waste\b", "states that up front rather than wasting"),
        (r"\bsets that expectation early than let\b", "sets that expectation early rather than let"),
        (r"\bsets that expectation early rather than let\b",
         "sets that expectation early rather than allowing"),
        (r"\bwhat['’]s the owner['’]s mineral rights worth\b", "what are mineral rights worth"),
        (r"\bis the owner['’]s check dropping\b", "is the royalty check dropping"),
    )
    for pattern, replacement in editorial_cleanups:
        text = re.sub(pattern, replacement, text, flags=re.I)
    return text


def rewrite(value):
    if isinstance(value, dict):
        return {key: rewrite(child) for key, child in value.items()}
    if isinstance(value, list):
        return [rewrite(child) for child in value]
    if isinstance(value, str):
        return institutionalize(value)
    return value


def main() -> None:
    changed = 0
    failures: list[str] = []
    for path in sorted(CONTENT.rglob("*.json")):
        before = path.read_text()
        revised = rewrite(json.loads(before))
        after = json.dumps(revised, indent=2, ensure_ascii=False) + "\n"
        if after != before:
            path.write_text(after)
            changed += 1
        for match in FIRST_PERSON.finditer(after):
            failures.append(f"{path.relative_to(ROOT)}: {match.group(0)!r}")
    if failures:
        raise SystemExit("Singular first-person copy remains:\n" + "\n".join(failures[:50]))
    print(f"institutionalize_content: {changed} files updated; singular first-person copy = 0")


if __name__ == "__main__":
    main()

import json
import os
import requests

BOT_TOKEN = "8792746318:AAEx1oJuxCa9hVxAMKjcDIE-z7_tAOAOulg"
CHAT_ID = "8962564147"
STATE_FILE = "state.json"

VOCAB_LIST = [
    {"word": "assiduous", "meaning": "very hardworking and persistent", "synonyms": "diligent, industrious, painstaking", "usage": "She was assiduous in her preparation."},
    {"word": "querulous", "meaning": "habitually complaining", "synonyms": "petulant, whining, fretful", "usage": "His querulous tone irritated everyone."},
    {"word": "antithesis", "meaning": "exact opposite/contrast", "synonyms": "converse, opposite, contrary", "usage": "His behaviour is the antithesis of generosity."},
    {"word": "doldrums", "meaning": "state of inactivity/stagnation", "synonyms": "lethargy, stagnation", "usage": "The industry remained in the doldrums."},
    {"word": "motif", "meaning": "recurring idea/design/theme", "synonyms": "theme, pattern", "usage": "Birds are a recurring motif in the poem."},
    {"word": "precis", "meaning": "concise summary", "synonyms": "synopsis, abstract", "usage": "Write a precis of the passage."},
    {"word": "conflate", "meaning": "combine things, often incorrectly", "synonyms": "merge, amalgamate, fuse", "usage": "Do not conflate correlation with causation."},
    {"word": "ubiquitous", "meaning": "present everywhere", "synonyms": "omnipresent, pervasive", "usage": "Mobile phones are ubiquitous."},
    {"word": "premise", "meaning": "basis/assumption of an argument", "synonyms": "proposition, assumption", "usage": "The argument rests on a false premise."},
    {"word": "premised", "meaning": "based on", "synonyms": "founded, based", "usage": "The policy is premised on equality."},
    {"word": "acuity", "meaning": "sharpness, especially mental/sensory", "synonyms": "keenness, sharpness", "usage": "The test measures visual acuity."},
    {"word": "resilience", "meaning": "ability to recover", "synonyms": "toughness, adaptability", "usage": "The community showed resilience."},
    {"word": "therapeutic", "meaning": "having a healing/beneficial effect", "synonyms": "curative, restorative", "usage": "Music can be therapeutic."},
    {"word": "mitigate", "meaning": "make less severe", "synonyms": "alleviate, reduce, moderate", "usage": "Trees mitigate extreme heat."},
    {"word": "prevalence", "meaning": "how widespread something is", "synonyms": "incidence, frequency", "usage": "The prevalence of obesity has increased."},
    {"word": "incidence", "meaning": "occurrence/rate of occurrence", "synonyms": "occurrence, frequency", "usage": "The incidence of accidents declined."},
    {"word": "perpetuate", "meaning": "cause something to continue", "synonyms": "prolong, sustain", "usage": "The stereotype perpetuates inequality."},
    {"word": "foster", "meaning": "encourage development", "synonyms": "nurture, cultivate", "usage": "Education fosters independence."},
    {"word": "provoke", "meaning": "cause a reaction", "synonyms": "trigger, incite, elicit", "usage": "The remark provoked controversy."},
    {"word": "compromise", "meaning": "weaken/endanger", "synonyms": "undermine, jeopardise", "usage": "Stress can compromise immunity."},
    {"word": "impair", "meaning": "damage/weaken", "synonyms": "diminish, hinder", "usage": "Lack of sleep can impair concentration."},
    {"word": "counter", "meaning": "oppose/neutralise", "synonyms": "oppose, offset", "usage": "Exercise can counter some effects of stress."},
    {"word": "generate", "meaning": "produce/cause", "synonyms": "create, produce", "usage": "The campaign generated debate."},
    {"word": "trigger", "meaning": "cause something to begin", "synonyms": "provoke, activate", "usage": "The incident triggered protests."},
    {"word": "endorse", "meaning": "publicly support", "synonyms": "approve, support", "usage": "The committee endorsed the proposal."},
    {"word": "maintain", "meaning": "continue/preserve", "synonyms": "sustain, retain", "usage": "The institution maintains high standards."},
    {"word": "induce", "meaning": "cause/bring about", "synonyms": "cause, provoke", "usage": "The drug may induce sleep."},
    {"word": "inflammation", "meaning": "bodily response causing swelling/irritation", "synonyms": "irritation, swelling", "usage": "The treatment reduces inflammation."},
    {"word": "expedition", "meaning": "organised journey, usually for exploration", "synonyms": "excursion, venture", "usage": "They launched an Arctic expedition."},
    {"word": "contiguity", "meaning": "state of being next to/touching", "synonyms": "proximity, adjacency", "usage": "Contiguity of borders aids trade."},
    {"word": "foraging", "meaning": "searching for food", "synonyms": "hunting, searching", "usage": "Birds spent hours foraging for seeds."},
    {"word": "projected", "meaning": "planned/intended", "synonyms": "proposed, intended", "usage": "The projected earnings look promising."},
    {"word": "enterprise", "meaning": "undertaking/activity", "synonyms": "venture, endeavour", "usage": "Starting a business is a bold enterprise."},
    {"word": "mutual", "meaning": "shared by both sides", "synonyms": "reciprocal, shared", "usage": "They had mutual respect."},
    {"word": "communicate", "meaning": "exchange information", "synonyms": "convey, transmit", "usage": "Whales communicate through song."},
    {"word": "discern", "meaning": "perceive/recognise", "synonyms": "detect, distinguish", "usage": "He could discern subtle differences."},
    {"word": "peculiar", "meaning": "unusual/distinctive", "synonyms": "strange, distinctive", "usage": "The dish had a peculiar smell."},
    {"word": "comprehend", "meaning": "understand", "synonyms": "grasp, apprehend", "usage": "She could not comprehend the decision."},
    {"word": "rhetoric", "meaning": "persuasive language", "synonyms": "oratory, persuasion", "usage": "His speech was full of empty rhetoric."},
    {"word": "spurious", "meaning": "false but apparently genuine", "synonyms": "bogus, fraudulent", "usage": "The report made spurious claims."},
    {"word": "counterpart", "meaning": "corresponding person/thing", "synonyms": "equivalent, parallel", "usage": "He met his foreign counterpart."},
    {"word": "vested interest", "meaning": "personal stake in an outcome", "synonyms": "self-interest, stake", "usage": "They had a vested interest in the vote."},
    {"word": "spectre", "meaning": "threatening possibility", "synonyms": "threat, shadow", "usage": "The spectre of recession loomed."},
    {"word": "propaganda", "meaning": "information designed to influence opinion", "synonyms": "indoctrination", "usage": "The flyer was pure propaganda."},
    {"word": "discourse", "meaning": "formal/public discussion", "synonyms": "debate, discussion", "usage": "Civil discourse is vital for democracy."},
    {"word": "legacy", "meaning": "something inherited from the past", "synonyms": "heritage, inheritance", "usage": "Her legacy lives on."},
    {"word": "reinforce", "meaning": "strengthen", "synonyms": "bolster, fortify", "usage": "Evidence helped reinforce his thesis."},
    {"word": "dubious", "meaning": "doubtful/questionable", "synonyms": "suspect, uncertain", "usage": "The argument rests on dubious facts."},
    {"word": "propagate", "meaning": "spread widely", "synonyms": "disseminate, circulate", "usage": "They propagate information online."},
    {"word": "hijack", "meaning": "take control for an unintended purpose", "synonyms": "seize, appropriate", "usage": "Radicals hijacked the movement."},
    {"word": "bias", "meaning": "unfair preference", "synonyms": "prejudice, partiality", "usage": "The judge showed clear bias."},
    {"word": "contemporary", "meaning": "belonging to the present", "synonyms": "modern, current", "usage": "He studies contemporary art."},
    {"word": "meaningfully", "meaning": "significantly/usefully", "synonyms": "substantially", "usage": "She contributed meaningfully to the team."},
    {"word": "progeny", "meaning": "offspring", "synonyms": "descendants, offspring", "usage": "They protect their progeny from danger."},
    {"word": "pulp", "meaning": "soft fleshy part of fruit", "synonyms": "flesh", "usage": "Mash the fruit pulp thoroughly."},
    {"word": "climacteric", "meaning": "fruit ripening after harvest", "synonyms": "post-harvest ripening", "usage": "Bananas are climacteric fruits."},
    {"word": "ripen", "meaning": "become mature", "synonyms": "mature, develop", "usage": "Apples ripen in late autumn."},
    {"word": "dispersal", "meaning": "spreading/distribution", "synonyms": "dissemination, diffusion", "usage": "Wind aids seed dispersal."},
    {"word": "adaptation", "meaning": "adjustment to conditions", "synonyms": "accommodation, adjustment", "usage": "Camels show remarkable desert adaptation."},
    {"word": "dwelling", "meaning": "living/residing", "synonyms": "inhabiting, residing", "usage": "Cave dwelling creatures adapt to darkness."},
    {"word": "physiological", "meaning": "relating to bodily processes", "synonyms": "biological, bodily", "usage": "Stress creates physiological changes."},
    {"word": "metabolism", "meaning": "chemical processes sustaining life", "synonyms": "biochemical process", "usage": "Exercise increases your metabolism."},
    {"word": "susceptible", "meaning": "easily affected", "synonyms": "vulnerable, prone", "usage": "The elderly are susceptible to flu."},
    {"word": "deprivation", "meaning": "lack/denial of something needed", "synonyms": "shortage, denial", "usage": "Sleep deprivation harms performance."},
    {"word": "restorative", "meaning": "renewing/healing", "synonyms": "rejuvenating, therapeutic", "usage": "Sleep has a restorative effect."},
    {"word": "exacerbate", "meaning": "make worse", "synonyms": "aggravate, intensify", "usage": "Dust will exacerbate allergies."},
    {"word": "chronic", "meaning": "persistent/long-lasting", "synonyms": "prolonged, persistent", "usage": "He suffered from chronic pain."},
    {"word": "adaptive", "meaning": "helping adjustment/survival", "synonyms": "advantageous", "usage": "Feathers provide an adaptive advantage."},
    {"word": "maladaptive", "meaning": "poorly suited to adjustment", "synonyms": "dysfunctional", "usage": "Avoidance is a maladaptive coping habit."},
    {"word": "manifest", "meaning": "become apparent", "synonyms": "emerge, appear", "usage": "Symptoms manifest after 48 hours."},
    {"word": "interplay", "meaning": "interaction between things", "synonyms": "interaction, interrelation", "usage": "The interplay between genetics and diet."},
    {"word": "abominate", "meaning": "hate intensely", "synonyms": "detest, loathe", "usage": "He abominates cruelty."},
    {"word": "abhor", "meaning": "regard with intense hatred", "synonyms": "detest, despise", "usage": "She abhors dishonesty."},
    {"word": "impromptu", "meaning": "unprepared/spontaneous", "synonyms": "spontaneous, extempore", "usage": "He gave an impromptu speech."},
    {"word": "wretched", "meaning": "miserable/poor", "synonyms": "miserable, pitiable", "usage": "They lived in wretched conditions."},
    {"word": "erroneous", "meaning": "incorrect", "synonyms": "inaccurate, mistaken", "usage": "The conclusion was erroneous."},
    {"word": "agog", "meaning": "very excited/eager", "synonyms": "eager, excited", "usage": "The audience was agog with anticipation."},
    {"word": "tantamount", "meaning": "equivalent in effect", "synonyms": "equivalent, comparable", "usage": "Silence was tantamount to agreement."},
    {"word": "audacious", "meaning": "boldly daring", "synonyms": "bold, daring, intrepid", "usage": "It was an audacious proposal."},
    {"word": "fumigate", "meaning": "disinfect using fumes/gas", "synonyms": "disinfect, purify", "usage": "The room was fumigated."},
    {"word": "hypochondria", "meaning": "excessive health anxiety", "synonyms": "health anxiety", "usage": "His hypochondria made him worry."},
    {"word": "jeopardy", "meaning": "danger/risk", "synonyms": "peril, hazard", "usage": "The project is in jeopardy."},
    {"word": "sedative", "meaning": "calming/sleep-inducing substance", "synonyms": "tranquiliser", "usage": "The medicine had a sedative effect."},
    {"word": "benevolent", "meaning": "kind and charitable", "synonyms": "charitable, humane", "usage": "A benevolent leader helps everyone."},
    {"word": "malevolent", "meaning": "wishing harm", "synonyms": "malicious, spiteful", "usage": "He gave a malevolent glance."},
    {"word": "pragmatic", "meaning": "practical rather than theoretical", "synonyms": "practical, realistic", "usage": "She adopted a pragmatic approach."},
    {"word": "meticulous", "meaning": "extremely careful", "synonyms": "painstaking, thorough", "usage": "He kept meticulous records."},
    {"word": "formidable", "meaning": "difficult/impressive", "synonyms": "daunting, intimidating", "usage": "They face a formidable opponent."},
    {"word": "plausible", "meaning": "seeming reasonable/possible", "synonyms": "credible, believable", "usage": "That sounds like a plausible explanation."},
    {"word": "ambiguous", "meaning": "having multiple possible meanings", "synonyms": "unclear, equivocal", "usage": "His reply was ambiguous."},
    {"word": "candid", "meaning": "truthful/frank", "synonyms": "frank, honest", "usage": "She gave a candid assessment."},
    {"word": "complacent", "meaning": "excessively self-satisfied", "synonyms": "smug, self-satisfied", "usage": "Never become complacent after success."},
    {"word": "detrimental", "meaning": "harmful", "synonyms": "damaging, adverse", "usage": "Sugar is detrimental to dental health."},
    {"word": "inevitable", "meaning": "certain to happen", "synonyms": "unavoidable, certain", "usage": "Change is inevitable."},
    {"word": "subtle", "meaning": "difficult to notice/understand", "synonyms": "nuanced, delicate", "usage": "There is a subtle nuance here."},
    {"word": "versatile", "meaning": "capable of many uses", "synonyms": "adaptable, multifaceted", "usage": "She is a versatile artist."},
    {"word": "vulnerable", "meaning": "easily harmed/affected", "synonyms": "susceptible, exposed", "usage": "Young chicks are vulnerable."},
    {"word": "proscribe", "meaning": "officially forbid", "synonyms": "prohibit, ban", "usage": "The law proscribed strikes."},
    {"word": "callous", "meaning": "emotionally insensitive", "synonyms": "insensitive, hard-hearted", "usage": "His callous remarks hurt feelings."},
    {"word": "entreat", "meaning": "ask earnestly", "synonyms": "implore, beseech", "usage": "They entreated the judge for mercy."},
    {"word": "colossal", "meaning": "extremely large", "synonyms": "enormous, gigantic", "usage": "It was a colossal monument."},
    {"word": "ephemeral", "meaning": "lasting a very short time", "synonyms": "fleeting, transient", "usage": "Fame is ephemeral."},
    {"word": "loquacious", "meaning": "very talkative", "synonyms": "garrulous, talkative", "usage": "The loquacious host kept chatting."},
    {"word": "impetuous", "meaning": "acting without thought", "synonyms": "rash, impulsive", "usage": "He made an impetuous bet."},
    {"word": "fastidious", "meaning": "very particular/careful", "synonyms": "meticulous, demanding", "usage": "She is fastidious about hygiene."},
    {"word": "innocuous", "meaning": "harmless", "synonyms": "benign, safe", "usage": "The joke was innocuous."},
    {"word": "desultory", "meaning": "lacking a plan/purpose", "synonyms": "aimless, random", "usage": "He read in a desultory way."},
    {"word": "piqued", "meaning": "aroused interest/curiosity", "synonyms": "intrigued, stimulated", "usage": "The mystery piqued his interest."},
    {"word": "grim", "meaning": "serious/unpleasant", "synonyms": "bleak, sombre", "usage": "The forecast looked grim."},
    {"word": "pedagogy", "meaning": "method/practice of teaching", "synonyms": "teaching methodology", "usage": "Modern pedagogy values participation."},
    {"word": "palpable", "meaning": "clearly noticeable", "synonyms": "tangible, perceptible", "usage": "The tension was palpable."},
    {"word": "melancholy", "meaning": "deep/sombre sadness", "synonyms": "sadness, gloom", "usage": "Rain induced a sense of melancholy."},
    {"word": "irrevocable", "meaning": "impossible to change/reverse", "synonyms": "irreversible, final", "usage": "The decision was irrevocable."},
    {"word": "sedition", "meaning": "incitement against authority", "synonyms": "subversion, incitement", "usage": "He was tried for sedition."},
    {"word": "obscure", "meaning": "unclear/not well known", "synonyms": "vague, unknown", "usage": "An obscure author wrote this."},
    {"word": "equitable", "meaning": "fair and impartial", "synonyms": "just, fair", "usage": "We need an equitable division."},
    {"word": "tranquil", "meaning": "calm and peaceful", "synonyms": "serene, placid", "usage": "The garden remained tranquil."},
    {"word": "apathetic", "meaning": "lacking interest/concern", "synonyms": "indifferent, unconcerned", "usage": "Voters became apathetic."},
    {"word": "soliloquy", "meaning": "speech to oneself", "synonyms": "monologue", "usage": "Hamlet's soliloquy is famous."},
    {"word": "aviary", "meaning": "enclosure for birds", "synonyms": "birdhouse", "usage": "The birds are in an aviary."},
    {"word": "almanac", "meaning": "annual calendar publication", "synonyms": "yearbook", "usage": "Check the almanac for tides."},
    {"word": "autocracy", "meaning": "government by one person", "synonyms": "dictatorship", "usage": "The ruler imposed an autocracy."},
    {"word": "theology", "meaning": "study of religion/God", "synonyms": "religious studies", "usage": "He holds a degree in theology."},
    {"word": "abundant", "meaning": "plentiful", "synonyms": "plentiful, copious", "usage": "Water is abundant in the tropics."},
    {"word": "amicable", "meaning": "friendly", "synonyms": "cordial, friendly", "usage": "They settled amicably."},
    {"word": "arduous", "meaning": "difficult", "synonyms": "laborious, strenuous", "usage": "Climbing Everest is an arduous task."},
    {"word": "coherent", "meaning": "logical and clear", "synonyms": "consistent, articulate", "usage": "Give a coherent explanation."},
    {"word": "conspicuous", "meaning": "noticeable", "synonyms": "prominent, salient", "usage": "The bright sign was conspicuous."},
    {"word": "credible", "meaning": "believable", "synonyms": "trustworthy, reliable", "usage": "He provided credible witnesses."},
    {"word": "diligent", "meaning": "hardworking", "synonyms": "industrious, assiduous", "usage": "Diligent practice yields results."},
    {"word": "elaborate", "meaning": "detailed", "synonyms": "intricate, complex", "usage": "They prepared an elaborate plan."},
    {"word": "feasible", "meaning": "possible to achieve", "synonyms": "viable, attainable", "usage": "Is this project feasible?"},
    {"word": "futile", "meaning": "useless", "synonyms": "fruitless, pointless", "usage": "Resistance proved futile."},
    {"word": "obsolete", "meaning": "outdated", "synonyms": "archaic, antiquated", "usage": "Floppy disks are obsolete."},
    {"word": "prudent", "meaning": "wise/cautious", "synonyms": "judicious, sensible", "usage": "Save money for prudent planning."},
    {"word": "reluctant", "meaning": "unwilling", "synonyms": "hesitant, loath", "usage": "He was reluctant to commit."},
    {"word": "scarce", "meaning": "rare/insufficient", "synonyms": "meager, deficient", "usage": "Fresh water became scarce."},
    {"word": "trivial", "meaning": "insignificant", "synonyms": "unimportant, frivolous", "usage": "Do not fight over trivial matters."}
]

IDIOMS_AND_PHRASES = [
    {"phrase": "at the eleventh hour", "meaning": "at the last possible moment", "usage": "They submitted the application at the eleventh hour."},
    {"phrase": "burn one's boats", "meaning": "make retreat impossible", "usage": "He burned his boats by rejecting the alternative."},
    {"phrase": "curry favour", "meaning": "try to gain someone's approval", "usage": "He tried to curry favour with the manager."},
    {"phrase": "chip in", "meaning": "contribute/help", "usage": "Everyone chipped in to solve the problem."},
    {"phrase": "gift of the gab", "meaning": "ability to speak fluently/persuasively", "usage": "She has the gift of the gab."},
    {"phrase": "slip of the tongue", "meaning": "accidental verbal mistake", "usage": "It was merely a slip of the tongue."},
    {"phrase": "tooth and nail", "meaning": "with great determination", "usage": "They fought tooth and nail."},
    {"phrase": "at loggerheads", "meaning": "in strong disagreement", "usage": "The two sides were at loggerheads."},
    {"phrase": "by and large", "meaning": "generally", "usage": "By and large, the plan worked."},
    {"phrase": "in the long run", "meaning": "eventually", "usage": "The investment will help in the long run."},
    {"phrase": "in lieu of", "meaning": "instead of", "usage": "He received leave in lieu of overtime pay."},
    {"phrase": "in the wake of", "meaning": "following an event", "usage": "Reforms followed in the wake of the crisis."},
    {"phrase": "at the expense of", "meaning": "sacrificing something else", "usage": "Growth came at the expense of equality."},
    {"phrase": "in light of", "meaning": "considering", "usage": "The policy was changed in light of new evidence."},
    {"phrase": "a double-edged sword", "meaning": "something with both advantages and disadvantages", "usage": "Technology is a double-edged sword."},
    {"phrase": "blessing in disguise", "meaning": "apparent misfortune that proves beneficial", "usage": "The rejection was a blessing in disguise."},
    {"phrase": "throw in the towel", "meaning": "give up", "usage": "The team refused to throw in the towel."},
    {"phrase": "bark up the wrong tree", "meaning": "pursue a mistaken idea", "usage": "You're barking up the wrong tree."},
    {"phrase": "cut corners", "meaning": "take shortcuts, often sacrificing quality", "usage": "Don't cut corners on research."},
    {"phrase": "hit the nail on the head", "meaning": "identify something exactly", "usage": "You hit the nail on the head."},
    {"phrase": "bring about", "meaning": "cause", "usage": "The reform brought about major changes."},
    {"phrase": "bring up", "meaning": "raise/mention", "usage": "She brought up an important issue."},
    {"phrase": "bring down", "meaning": "reduce/defeat", "usage": "The policy brought down inflation."},
    {"phrase": "call off", "meaning": "cancel", "usage": "The meeting was called off."},
    {"phrase": "break down", "meaning": "stop functioning / analyse", "usage": "The machine broke down."},
    {"phrase": "break up", "meaning": "separate/end", "usage": "The meeting broke up at noon."},
    {"phrase": "carry out", "meaning": "execute", "usage": "The researchers carried out an experiment."},
    {"phrase": "come across", "meaning": "encounter", "usage": "I came across an interesting article."},
    {"phrase": "come up with", "meaning": "devise", "usage": "She came up with a solution."},
    {"phrase": "cut down on", "meaning": "reduce", "usage": "We should cut down on unnecessary spending."},
    {"phrase": "do away with", "meaning": "abolish", "usage": "The law did away with the old system."},
    {"phrase": "fall through", "meaning": "fail to happen", "usage": "The deal fell through."},
    {"phrase": "give rise to", "meaning": "cause", "usage": "The decision gave rise to controversy."},
    {"phrase": "hold back", "meaning": "restrain", "usage": "Fear held him back."},
    {"phrase": "hold off", "meaning": "delay", "usage": "They held off making a decision."},
    {"phrase": "look into", "meaning": "investigate", "usage": "The committee will look into the complaint."},
    {"phrase": "look through", "meaning": "examine quickly", "usage": "She looked through the documents."},
    {"phrase": "put off", "meaning": "postpone", "usage": "The meeting was put off."},
    {"phrase": "put up with", "meaning": "tolerate", "usage": "I won't put up with dishonesty."},
    {"phrase": "rule out", "meaning": "eliminate as possibility", "usage": "The evidence rules out that explanation."},
    {"phrase": "take away", "meaning": "remove", "usage": "The experience took away his fear."},
    {"phrase": "take up", "meaning": "begin/occupy", "usage": "She took up painting."},
    {"phrase": "turn down", "meaning": "reject/reduce", "usage": "He turned down the offer."},
    {"phrase": "turn up", "meaning": "appear/increase", "usage": "She turned up unexpectedly."},
    {"phrase": "work out", "meaning": "solve/develop successfully", "usage": "They worked out a solution."}
]

batches = [VOCAB_LIST[i:i + 5] for i in range(0, len(VOCAB_LIST), 5)]

def get_current_day():
    if not os.path.exists(STATE_FILE):
        with open(STATE_FILE, "w") as f:
            json.dump({"currentDay": 1}, f)
        return 1
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f).get("currentDay", 1)
    except Exception:
        return 1

def advance_day(day):
    with open(STATE_FILE, "w") as f:
        json.dump({"currentDay": day + 1}, f)

def generate_payload(day):
    curr_idx = day - 1
    msg = f"🎯 *IPMAT DAILY VA DRILL — DAY {day}*\n\n"

    # 1. 5 New Words with Synonyms & Bold styling
    if curr_idx < len(batches):
        msg += "*🆕 TODAY'S 5 NEW WORDS:*\n"
        for i, item in enumerate(batches[curr_idx], 1):
            msg += f"{i}. *{item['word'].upper()}*\n"
            msg += f"   • Meaning: {item['meaning']}\n"
            msg += f"   • Synonyms: _{item['synonyms']}_\n"
            msg += f"   • Example: \"{item['usage']}\"\n\n"

    # 2. 5-4-3-2-1 Spaced Repetition Reviews
    reps = [
        (1, 4, "4 Words (Day -1)"),
        (2, 3, "3 Words (Day -2)"),
        (3, 2, "2 Words (Day -3)"),
        (4, 1, "1 Word (Day -4)")
    ]

    review_text = ""
    for offset, count, label in reps:
        prev_idx = curr_idx - offset
        if 0 <= prev_idx < len(batches):
            review_text += f"*🔁 Review {label}:*\n"
            for item in batches[prev_idx][:count]:
                review_text += f"• *{item['word']}* — {item['meaning']} (_{item['synonyms']}_)\n"
            review_text += "\n"

    if review_text:
        msg += "*--- 5-4-3-2-1 SPACED REVIEW ---*\n\n" + review_text

    # 3. Daily Idiom / Phrasal Verb
    idiom = IDIOMS_AND_PHRASES[(day - 1) % len(IDIOMS_AND_PHRASES)]
    msg += f"*💡 DAILY IDIOM / PHRASE:*\n• *{idiom['phrase']}*\n  Meaning: {idiom['meaning']}\n  Example: \"{idiom['usage']}\""

    return msg

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        resp = requests.post(url, json=payload, timeout=10)
        return resp.json()
    except Exception as e:
        print(f"Network error: {e}")
        return None

if __name__ == "__main__":
    day = get_current_day()
    drill = generate_payload(day)
    print(f"Sending Day {day} drill to Telegram...")
    res = send_telegram(drill)
    if res and res.get("ok"):
        print("✅ Sent successfully! Check your Telegram.")
        advance_day(day)
    else:
        print("❌ Telegram API returned error:", res)
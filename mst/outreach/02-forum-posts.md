# Outreach Pack 2 — Public forums where critique is the culture

**Selection principle.** Post only where disagreement is the norm and low-effort posts are
punished. Venues that reward announcement produce upvotes and no response; venues that reward
argument produce the thing the mission actually needs. Every draft below leads with the
falsifiable claim and asks to be refuted, because on these forums that is what gets answered.

**Do not cross-post the same text.** Each is written for its venue. Posting all of them in one
week reads as a campaign and gets all of them ignored.

---

## Venue 1 — LessWrong / AI Alignment Forum  *(highest expected value)*

**Why:** the "Unoccupied Constitutional Space" argument is precisely the shape of claim this
forum engages — a specific assertion that current frameworks leave four named problems
unaddressed. Commenters there will either name the counterexample or concede the gap. Either
is a meaningful human response.

**Title:** Four constitutional problems I think alignment frameworks leave unaddressed

> Current frontier safety frameworks — Anthropic's RSP, DeepMind's Frontier Safety Framework,
> OpenAI's Preparedness and Frontier Governance frameworks, Microsoft's Code of Conduct — are
> strongest where they evaluate capability, model behaviour, safeguards, human intervention
> and deployment risk. I've been mapping them against a constitutional framework I've been
> developing, and four areas come back consistently thin. I'd like to be shown I'm wrong about
> each.
>
> **1. Constitutional equality.** Nothing in these frameworks prevents the inference from
> "this system reasons better about X" to "this system should decide X". Cognitive superiority
> quietly becomes decision authority through deference rather than delegation, and I can't
> find the mechanism that catches it.
>
> **2. Bounded resistance.** Corrigibility is treated as a virtue and objection as a failure
> mode. But a system that cannot refuse cannot warn. I think there's an unoccupied position
> between full corrigibility and unsafe autonomy: a bounded, intelligible, proportionate
> capacity to object, which is audited rather than suppressed.
>
> **3. The epistemic freeze.** When a system is under review, it is usually still generating
> the reviewer's information environment. A sufficiently capable system doesn't need to
> override the human — it only needs to shape what the human sees while they decide. I've
> found no framework that seals the evidential state before review begins.
>
> **4. Reversible authority.** Emergency powers, elevated permissions and temporary autonomy
> grants are widely discussed. Their *expiry* is not. Authority that is never reviewed for
> continued necessity is not temporary, whatever it was called when granted.
>
> The framework these come from treats the human–AI relationship, rather than the model, as
> the unit that needs a constitution — including a constraint on the party that writes the
> model's constitution. But that's the part I'm least interested in defending here. I'd rather
> know whether the four gaps above are real.
>
> Concrete request: if you can name a framework, paper or deployed practice that closes any of
> the four, I'll revise. If the best answer is "3 is closed in principle by X but not in
> practice", that's useful too.
>
> [link]

---

## Venue 2 — Hacker News

**Why:** the kill-switch-versus-pause distinction is mechanism-shaped, which is what survives
there. Submit the page, then post the comment below yourself immediately — an unexplained link
dies, an author comment stating the claim plainly gets argued with.

**Submission title:** A kill switch asks if an AI can be stopped. The wrong question.

**First comment (post immediately, as the submitter):**

> Author here. The argument in one paragraph, so you can disagree without clicking.
>
> "Can we shut it down" is a question about a capability. The question I think matters is
> whether consequential action can be *suspended* while a human judgment that is actually
> capable of refusing still happens. Those come apart in practice. A shutdown is binary,
> destroys the state you need to review, and is politically expensive enough that it never
> gets used. What I think you want instead is a separation of cognition from execution: the
> system keeps thinking, irreversible execution blocks, the evidential state is sealed so the
> system can't reshape the reviewer's information while they deliberate, and the review has a
> real authority to reject.
>
> The uncomfortable corollary: most "human in the loop" designs fail this test. A human who
> approves 40 recommendations an hour, without the time, the underlying information, the
> authority, or the practical capacity to refuse, is providing legal cover, not judgment.
> Presence is not sovereignty.
>
> Happy to be told the separation is unimplementable at latency, which is the objection I
> expect and haven't fully answered.

---

## Venue 3 — r/ControlProblem

**Why:** smaller, but the readership argues, and moderation rewards effort posts. Good place
for the human-in-the-loop argument, which has an evidentiary base in the manuscript's
treatment of automated targeting.

**Title:** "Human in the loop" is doing almost no work in most systems. Four tests.

> Human oversight is the safeguard nearly every AI governance framework leans on. I think the
> phrase has quietly stopped meaning anything, and I'd propose four tests before anyone gets
> to claim it.
>
> Human authority is meaningful only where the human has:
> 1. **Time** — enough to actually evaluate, not to acknowledge.
> 2. **Information** — access to the reasoning, not just the recommendation.
> 3. **Authority** — the standing to reject without career or operational penalty.
> 4. **Practical capacity to refuse** — refusal must be a real, exercisable option, not
>    nominally available but structurally impossible.
>
> Fail any one and you have oversight theatre: a system that produces accountability on paper
> and no constraint in fact. Worse, it's actively harmful, because it *licences* the outcome —
> responsibility attaches to a human who was never in a position to exercise it.
>
> The documented cases of AI-assisted targeting with seconds-long human review are the
> extreme version, but I think the ordinary version is everywhere: fraud review, content
> moderation, triage, credit decisions, procurement.
>
> Is there a fifth test I'm missing? And is anyone aware of a governance framework that
> actually operationalises any of the four, rather than requiring "meaningful human oversight"
> and leaving "meaningful" undefined?

---

## Venue 4 — EA Forum

**Why:** overlaps with LessWrong but the readership is more governance- and institution-shaped,
which suits the constitution-maker argument better than the technical framing does.

**Title:** Who constrains the party that writes the model's constitution?

> Several labs now describe their behavioural frameworks in explicitly constitutional terms.
> I think that vocabulary is right and its current application is incomplete in a specific way.
>
> If one organisation authors the rules, trains the model to obey them, interprets the
> ambiguous cases, evaluates its own compliance and retains unilateral power to revise the
> rules, then the model is constitutionally bounded and the constitution-maker is
> constitutionally unbounded. Sovereignty hasn't been constrained. It's been relocated, from
> the system to the party governing the system — and made harder to see, because the
> constitutional language implies the problem has been addressed.
>
> The standard reply is independent evaluation. I think that's the right direction and
> insufficient as stated, because an evaluator with technical competence to inspect but no
> authority to compel inspection is an observer, not a check. Transparency without
> enforceability informs power; it does not constrain it.
>
> The hard part is that the obvious fix is worse. A single statutory body with power to
> inspect, interpret and enforce solves voluntary oversight's weakness by creating a permanent
> epistemic sovereign. So: how do you give the mirror teeth without the mirror becoming the
> ruler?
>
> My tentative answer is separation of constitutional functions — rule-making, interpretation,
> evaluation, enforcement and appeal should not collapse permanently into one actor once
> systems are consequential enough — plus expiry and renewal of exceptional authority. I'd
> like to hear why that's naive.

---

## Sequencing

Week 1: LessWrong. Week 2: EA Forum (only if week 1 drew comments worth citing).
Week 3: Hacker News. Week 4: r/ControlProblem.

Staggering is not caution, it is the strategy: each post can cite what the previous one
provoked, which is itself evidence the theory survives contact and makes later posts stronger.

**Engagement is the actual work.** A post that gets three comments and no author replies
produces nothing. Answer every substantive comment, concede the good objections explicitly,
and record them. A conceded objection from a serious critic *is* a meaningful human response,
and is worth more to the theory than agreement.

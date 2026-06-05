# Research Foundations and Acknowledgements

OpenRelief is informed by prior research in disaster informatics, crisis computing, social media analysis, AI-assisted disaster response, emergency message classification, crowdsourcing, and automated reporting. We acknowledge these works as research foundations for the project.

This document is not a claim that OpenRelief implements the exact methods from these papers. It records what the project learns from them and where the ideas need localization for Chinese-language, NGO-led, human-in-the-loop disaster response.

## AIDR: Artificial Intelligence for Disaster Response

**Contribution:** AIDR demonstrates a disaster-response workflow where social media posts are collected, labeled by humans, and classified by machine learning into crisis-relevant categories.

**OpenRelief learning:**

- Human labeling is a core system capability, not an afterthought.
- Disaster-specific categories must be configurable.
- AI outputs need confidence and review queues.
- Maps, reports, and APIs are downstream outputs of the same classification pipeline.

## CrisisSense-LLM

**Contribution:** CrisisSense-LLM shows that instruction-tuned large language models can improve multi-label disaster social media classification, while also showing that general-purpose LLMs are unreliable without domain adaptation and consistent prompts.

**OpenRelief learning:**

- Classify information across multiple dimensions, not just one label.
- Treat prompt definitions and schemas as durable project assets.
- Accumulate reviewed, anonymized Chinese-language examples before model adaptation.
- Evaluate invalid outputs, missing fields, and prompt drift.

## Using Social Media to Enhance Emergency Situation Awareness

**Contribution:** This work frames social media analysis as a situation awareness pipeline: data capture, burst detection, classification, clustering, geotagging, and visualization.

**OpenRelief learning:**

- Build a full situation awareness pipeline rather than a single classifier.
- Detect sudden changes in needs, hazards, and locations.
- Cluster reports into affected areas and event topics.
- Connect maps and briefs to the same structured evidence base.

## Deep Learning for Tweet Classification and Rescue Scheduling

**Contribution:** This paper connects disaster tweet classification to rescue priority scoring and scheduling, including vulnerable groups, hazards, and resource constraints.

**OpenRelief learning:**

- Move from information visibility toward action support.
- Separate priority scoring from final dispatch.
- Use vulnerable groups, people count, hazards, and location as triage factors.
- Keep scheduling recommendations under human confirmation.

## Socially Enhanced Situation Awareness from Microblogs Using AI: A Survey

**Contribution:** This survey organizes AI-based situation awareness into perception, comprehension, projection, and visualization, while highlighting bias, privacy, multilingual issues, ground truth scarcity, and data fusion.

**OpenRelief learning:**

- Treat OpenRelief as situation awareness infrastructure.
- Combine mini-program data, public information, official data, and volunteer verification.
- Track bias, coverage, provenance, and data quality.
- Design privacy and trust controls early.

## Harnessing Prompt-Based LLMs for Disaster Monitoring and Automated Reporting

**Contribution:** This paper shows how prompt-based LLMs can classify disaster feedback, detect sub-events, extract locations, aggregate by time and place, and draft disaster reports.

**OpenRelief learning:**

- Brief generation should be source-grounded and reviewable.
- Reports should aggregate classified and located evidence.
- Drafts must label verification status and uncertainty.
- Humans should edit and approve any public-facing brief.

## Intelligent Disaster Response via Social Media Analysis: A Survey

**Contribution:** This survey connects social media analysis to disaster stages: warning, impact, response, and relief. It highlights extraction, filtering, rumor control, bot/spam risks, crowdsourcing, Ushahidi, AIDR, and TweetTracker.

**OpenRelief learning:**

- Data filtering is foundational.
- Rumor, spam, and bot-like behavior must be considered safety risks.
- Digital volunteers can support translation, geotagging, map creation, and verification.
- Systems should distinguish big-picture situation awareness from actionable insight.

## Using AI to Identify Emergency Messages on Social Media During a Natural Disaster

**Contribution:** This paper separates relevance classification from urgency classification and emphasizes recall for emergency response because missing true life-safety cases can be more harmful than reviewing extra false positives.

**OpenRelief learning:**

- Triage should first decide relevance, then urgency.
- Evaluation should prioritize recall and F1 over raw accuracy.
- Urgent cases are rare and need careful sampling and review.
- The project should build human-labeled evaluation cases over time.

## Local Practice Foundations

OpenRelief also acknowledges the practical foundation from:

- NCP Relief's experience in online medical support, community assistance, volunteer coordination, and public help channels.
- Zhuoming Info Aid's disaster information service methodology, including needs assessment, situation briefs, maps, volunteer coordination, and HEINA-style analysis.
- The existing emergency help mini-program workflow, including public help requests, resource offers, field information, organization updates, situation briefs, affected-area views, and social force statistics.

## Citation Maintenance

Future versions should add full bibliographic metadata for each paper:

- title;
- authors;
- year;
- venue;
- DOI or stable URL;
- license or access notes where relevant.


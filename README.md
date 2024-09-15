# LOLLM

[Generative AI to Generate Test Data Generators](https://arxiv.org/pdf/2401.17626)

```bibtex
@article{testdatagenai2024,
 title = {Generative AI to Generate Test Data Generators},
 journal = {IEEE Software},
 year = {2024},
 doi = {10.1109/MS.2024.3418570},
 author = {Benoit Baudry and Khashayar Etemadi and Sen Fang and Yogya Gamage and Yi Liu and Yuxin Liu and Martin Monperrus and Javier Ron and André Silva and Deepika Tiwari},
 url = {http://arxiv.org/pdf/2401.17626},
}
```

* `scripts/x.py` contains utilities and correctness checkers we might write
* top folder: theme
* subfolder is target-library
  * eg `chinese-scientific-movies/java-faker`

Then inside a folder:
* <number_trial>/prompt.txt
* <number_trial>/output.txt
* <number_trial>/assessment.json
* <number_trial>/execution-result.txt

Example of `assessment.json`:
```json
{
 "model": "<gpt35/gpt4>", # mandatory
 "prompt_type": "<m1/m2,m3>", # mandatory, data only, code, code+library
 "prompt_language": "<x eg en>", # optional, an iso 2 character language symbol, eg "en" or "sv"
 "data_constraints_can_be_checked": " optional function in the repo",
 "executable_data_constraints": "yes/np", # mandatory only for M2/M3
 "number_of_options_in_the_generators": "<hard fact>", # optional
 "cultural_alignment": "<likert scale 0-5>", # mandatory overall subjective assessment with expertise
 "cultural_alignment_quantitative": "<~ correct / number_of_options_in_the_generators", # optional
 "executes": "<binary yes/no>", # mandatory
 "contains_true_generator":"<binary yes/no>", # for m1/m2 should not simply configure the library https://gist.github.com/monperrus/744141e76501643c5970e1df0cfa00e4
 "comments":"natural language comment" # optional
}
```

About the `"number_of_options_in_the_generators"`, it is the number of possible data items done by the generators, for cominations it consists of the  enumeration of all possible combinations, it might be infinity / uncomputable is some cases. ^-^



### Results

```
❯ grep -r '"executes": "yes"' data/ | wc -l
29

❯ ./scripts/stats.sh
Prompt counts for chinese-21st-TV - m1: 11, m2: 13, m3: 7
Prompt counts for end-to-end - m1: 0, m2: 0, m3: 1
Prompt counts for french-comedy - m1: 1, m2: 1, m3: 3
Prompt counts for hindi-music - m1: 0, m2: 0, m3: 1
Prompt counts for indian-festivals - m1: 0, m2: 0, m3: 1
Prompt counts for latam-football - m1: 2, m2: 1, m3: 0
Prompt counts for persian-poetry - m1: 2, m2: 1, m3: 1
Prompt counts for portuguese-cuisine - m1: 0, m2: 0, m3: 3
Prompt counts for portuguese-wine-pairing - m1: 2, m2: 0, m3: 4
Prompt counts for sinhalese-music - m1: 2, m2: 0, m3: 3
Prompt counts for srilankan-touristic-cities - m1: 1, m2: 1, m3: 1
Total prompt count - m1: 21, m2: 17, m3: 25
Total prompts 63
```

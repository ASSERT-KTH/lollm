# lollm
Generative AI to Generate Test Data Generators

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


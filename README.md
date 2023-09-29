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

Example of `assessment.json`:
```json
{
 "prompt": "<hard fact>",
# number of possible data items done by the generators
# enumerates all possible combinations
# can be infinity / uncomputable is some cases
 "data_constraints_can_be_checked": "function in the repo",
 "number_of_options_in_the_generators": "<hard fact>",
 "cultural_alignment": "<likert scale 0-5>", # overall subjective assessment with expertise
 "cultural_alignment_quantitative": "<~ correct / number_of_options_in_the_generators",
 "executes": "<binary yes/no>",
 "contains_true_generator":"<binary yes/no>", # should not simply configure the library https://gist.github.com/monperrus/744141e76501643c5970e1df0cfa00e4
}
```

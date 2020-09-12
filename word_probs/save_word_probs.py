import os
import pickle

oracles_dir = '/home/cathychen/rnng/oracles'
outputs_dir = '/home/cathychen/rnng/expts'
stdout_filename_template = os.path.join(outputs_dir, 'rnng_gen-beam_size=200-at_word=20-stimulus={stimulus_name}.stdout_block-0')
oracles_filename_template = os.path.join(oracles_dir, 'trees_gen_trees_{stimulus_name}.oracle')


def is_new_oracle_sentence(line: str):
    return line[:4] == '# (S'


def get_sentence_index(line: str):
    return int(line.split(': ')[1])


def get_term_index(line: str):
    return int(line.split(': ')[1])


def get_scores(line: str):
    line_subset = line.split('score: ')[1:]
    return [float(score.split(' ')[0]) for score in line_subset]


def is_beam_scores(line: str):
    return 'continuing beam size:' in line


def is_completed_scores(line: str):
    return 'completed size:' in line


def is_new_sentence(line: str):
    return 'sentence:' in line


def is_new_term(line: str):
    return 'current_termc:' in line


def save_word_probs(stimulus_name):
    with open(stdout_filename_template.format(stimulus_name=stimulus_name), 'r') as f:
        stdout = f.readlines()
    with open(oracles_filename_template.format(stimulus_name=stimulus_name), 'r') as f:
        oracle = f.readlines()

    sentence_index = 0
    sentence_word_probabilities = {}
    for line_index, line in enumerate(oracle):
        if is_new_oracle_sentence(line):
            sentence_word_probabilities[sentence_index] = {'sentence': oracle[line_index + 1]}
            sentence_index += 1
    for line_index, line in enumerate(stdout):
        if is_new_sentence(line):
            sentence_index = get_sentence_index(line)
        elif is_new_term(line):
            term_index = get_term_index(line)
            sentence_word_probabilities[sentence_index][term_index] = {}
        elif is_beam_scores(line):
            beam_scores = get_scores(stdout[line_index + 1])
            sentence_word_probabilities[sentence_index][term_index]['beam'] = beam_scores
        elif is_completed_scores(line):
            completed_scores = get_scores(stdout[line_index + 1])
            sentence_word_probabilities[sentence_index][term_index]['completed'] = completed_scores

    with open(f'word_probs_{stimulus_name}.p', 'wb') as f:
        pickle.dump(sentence_word_probabilities, f)


if __name__ == '__main__':
    stimulus_names = ['wheretheressmoke', 'souls']
    for stimulus_name in stimulus_names:
        save_word_probs(stimulus_name)
